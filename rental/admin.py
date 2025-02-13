from django.contrib import admin
from .models import Vehicle, Booking, Profile, Payment, Review, Notification, LoyaltyProgram

admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(LoyaltyProgram)
