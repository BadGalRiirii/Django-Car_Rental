from django.db import models
from django.contrib.auth.models import User

# Extend User model to add extra fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Luxury', 'Luxury'),
    ]

    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    features = models.TextField(blank=True, null=True)  # GPS, Child seat, etc.
    location = models.CharField(max_length=100, default="Main Branch")  # City of the car
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_STATUSES = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    dropoff_location = models.CharField(max_length=100, default="Same as pickup")
    pickup_location = models.CharField(max_length=100, default="Main Branch")
    pickup_date = models.DateField()
    return_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, default='Pending') 

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.name} ({self.status})"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Digital Wallet', 'Digital Wallet'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Payment for {self.booking} - {self.amount}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.name}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

class LoyaltyProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.points} Points"