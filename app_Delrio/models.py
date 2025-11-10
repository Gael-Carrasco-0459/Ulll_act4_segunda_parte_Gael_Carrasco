# app_Delrio/models.py
from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nom_clie = models.CharField(max_length=100)
    apellido_clie = models.CharField(max_length=100)
    C_E_clie = models.CharField(max_length=100)  # Correo electrónico
    tel_clie = models.CharField(max_length=20)
    direc_clie = models.TextField()
    fech_compra = models.DateField()

    def __str__(self):
        return f"{self.nom_clie} {self.apellido_clie}"


# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    nom_prod = models.CharField(max_length=100)
    desc_prod = models.TextField(blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fech_creacion = models.DateTimeField(auto_now_add=True)
    id_prov = models.IntegerField()  # Si existiera tabla 'proveedor', sería ForeignKey

    def __str__(self):
        return self.nom_prod


# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    fech_venta = models.DateTimeField(auto_now_add=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)

    # Relaciones foráneas
    id_clie = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ventas")
    id_empl = models.IntegerField()  # Si tuvieras tabla Empleado, usarías ForeignKey

    def __str__(self):
        return f"Venta #{self.id} - Cliente: {self.id_clie.nom_clie} - Total: ${self.total_venta}"