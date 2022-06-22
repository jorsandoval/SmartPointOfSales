from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm, VentaForm, ProductoForm, DetalleVentaForm

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'home_cliente.html',datos)

def form_cliente(request):
    datos = {
        'form': ClienteForm()
    }
    return render(request, 'form_cliente.html',datos)

def form_venta(request):
    datos = {
        'form': VentaForm()
    }
    return render(request, 'form_venta.html',datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    return render(request, 'form_producto.html',datos)    

def form_producto(request):
    datos = {
        'form': DetalleVentaForm()
    }
    return render(request, 'form_producto.html',datos)  

