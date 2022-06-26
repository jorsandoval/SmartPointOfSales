from http import client
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

#Formularios de ingreso

def form_cliente(request):
    datos = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Cliente guardado correctamente"
    return render(request, 'core/form_cliente.html',datos)

def form_venta(request):
    datos = {
        'form': VentaForm()
    }
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Venta registrada Correctamente"
    return render(request, 'core/form_venta.html',datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Producto registrado correctamente"
    return render(request, 'core/form_producto.html',datos)    

def form_detalle_venta(request):
    datos = {
        'form': DetalleVentaForm()
    }
    if request.method == 'POST':
        formulario = DetalleVentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Detalle de venta registrado correctamente"
    return render(request, 'core/form_detalle_venta.html',datos)  

def form_mediopago(request):
    datos = {
        'form': MedioPagoForm()
    }
    if request.method == 'POST':
        formulario = MedioPagoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Medio de pago registrado correctamente"
    return render(request, 'core/form_medio_pago.html',datos)

#Formularios de modificación

def form_mod_cliente(request,id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    datos = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Cliente modificado correctamente"
    return render(request, 'core/form_mod_cliente.html',datos)

def form_mod_producto(request,id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Producto modificado correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_mod_medio_pago(request,id_medio_pago):
    medio_pago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    datos = {
        'form': MedioPagoForm(instance=medio_pago)
    }
    if request.method == 'POST':
        formulario = MedioPagoForm(data=request.POST, instance=medio_pago)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Medio de pago modificado correctamente"
    return render(request, 'core/form_mod_medio_pago.html',datos)
