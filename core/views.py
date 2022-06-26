from django.shortcuts import render
from .models import Cliente, DetalleVenta, MedioPago, Producto, Venta
from .forms import ClienteForm, VentaForm, ProductoForm, DetalleVentaForm, MedioPagoForm

# Create your views here.
#Home de los modelos
def home(request):
    return render(request, 'core/home.html')

def home_cliente(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'core/home_cliente.html',datos)

def home_detalle_venta(request):
    detalle_ventas = DetalleVenta.objects.all()
    datos = {
        'detalle_ventas': detalle_ventas
    }
    return render(request, 'core/home_detalle_venta.html', datos)

def home_medio_pago(request):
    medio_pago = MedioPago.objects.all()
    datos = {
        'medio_pago': medio_pago
    }
    return render(request, 'core/home_medio_pago.html', datos)

def home_producto(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home_producto.html', datos)

def home_venta(request):
    ventas = Venta.objects.all()
    datos = {
        'ventas': ventas
    }
    return render(request, 'core/home_venta.html', datos)

#Formularios

def form_cliente(request):
    datos = {
        'form': ClienteForm()
    }
    return render(request, 'core/form_cliente.html',datos)

def form_venta(request):
    datos = {
        'form': VentaForm()
    }
    return render(request, 'core/form_venta.html',datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    return render(request, 'core/form_producto.html',datos)    

def form_producto(request):
    datos = {
        'form': DetalleVentaForm()
    }
    return render(request, 'core/form_producto.html',datos)  

def form_mediopago(request):
    datos = {
        'form': MedioPagoForm()
    }
    return render(request, 'core/form_medio_pago.html',datos)

