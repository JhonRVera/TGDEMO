from django.shortcuts import render ,redirect
from .models import Registros
from django.contrib import messages

# Create your views here.

def Home(request):
    registrosAutos = Registros.objects.all()
    return render(request,"gestionRegistro.html",{"registro":registrosAutos})


def RegistroVehiculo(request):
    placa=request.POST['txtplaca']
    fecha=request.POST['txtfecha']
    tipo_auto=request.POST['txttipo']
    valor=request.POST['txttotal']
    costos=request.POST['txtcostos']
    arreglos=request.POST['txtarreglos']
    
    registro=Registros.objects.create (
        placa=placa,fecha=fecha,tipo_auto=tipo_auto,valor=valor,costos=costos,arreglos=arreglos
    )
    messages.success(request,"!Vehiculo registrado!")
    return redirect('/')

