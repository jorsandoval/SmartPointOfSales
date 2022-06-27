from urllib.parse import urlparse
from django.urls import path
from Rest_SmartPointOfSales.views import lista_clientes

urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
]

