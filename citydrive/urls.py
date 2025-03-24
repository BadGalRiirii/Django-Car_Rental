from django.contrib import admin
from django.urls import path, include
from rental.views import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView, api_root

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_root, name="api-root"),  
    path("api/v1/rental_car/", CarListCreateAPIView.as_view(), name="rental_car-list-create"),
    path("api/v1/rental_car/<int:pk>/", CarRetrieveUpdateDestroyAPIView.as_view(), name="rental_car-retrieve-update-destroy"),
    
    
]
