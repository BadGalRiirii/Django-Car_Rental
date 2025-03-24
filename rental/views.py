from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

from .models import Vehicle  
from .serializers import VehicleSerializer  
from rest_framework import generics

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# Fix the incorrect reverse() usage
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rental_car_list': request.build_absolute_uri(reverse('rental_car-list-create'))
    })
