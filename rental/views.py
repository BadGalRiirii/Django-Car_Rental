from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

from .models import Vehicle  # Import models at the top if needed
from .serializers import VehicleSerializer  # Make sure your serializers exist
from rest_framework import generics

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# Move api_root here to avoid circular import issues
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rental_car_list': reverse('rental_car-list-create', request=request, format=format),
    })
