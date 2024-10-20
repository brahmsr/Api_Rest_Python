from django.contrib import admin
from .models import Produtos, Pedidos, Clientes

admin.site.register(Produtos)
admin.site.register(Pedidos)
admin.site.register(Clientes)
