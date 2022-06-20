from django.shortcuts import render
from .models import Cliente

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'core/form_cliente.html',datos)
