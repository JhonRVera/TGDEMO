from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.Home),
    path('registroVehiculo/', views.RegistroVehiculo)
]