# app_Delrio/admin.py
from django.contrib import admin
from .models import Cliente, Producto, Venta

# Registra los modelos aquí.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
