# app_Delrio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, Cliente, Producto # Importa los modelos

# ==========================================
# VISTAS PARA VENTA
# ==========================================

def inicio_Delrio(request):
    """
    Vista principal del sistema.
    """
    return render(request, 'inicio.html')

def ver_ventas(request):
    """
    Muestra una lista de todas las ventas.
    """
    ventas = Venta.objects.all().order_by('-fech_venta')
    return render(request, 'Ventas/ver_venta.html', {'ventas': ventas})


def agregar_venta(request):
    """
    Permite agregar una nueva venta.
    """
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            cliente_obj = get_object_or_404(Cliente, id=id_clie)
            producto_obj = get_object_or_404(Producto, id=id_prod)

            Venta.objects.create(
                id_clie=cliente_obj,
                id_prod=producto_obj,
                total_venta=total_venta,
                estado=estado,
                id_empl=id_empl,
            )
            return redirect('ver_ventas')
        except Exception as e:
            # Aquí puedes manejar errores si los datos no son válidos
            print(f"Error al agregar venta: {e}")
            # Puedes añadir un mensaje de error al contexto para mostrar en la plantilla
            return render(request, 'Ventas/agregar_venta.html', {
                'clientes': clientes,
                'productos': productos,
                'error_message': f"Hubo un error al guardar la venta: {e}"
            })

    return render(request, 'Ventas/agregar_venta.html', {'clientes': clientes, 'productos': productos})


def actualizar_venta(request, pk):
    """
    Muestra el formulario para actualizar una venta existente.
    """
    venta = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'Ventas/actualizar_venta.html', {
        'venta': venta,
        'clientes': clientes,
        'productos': productos
    })


def realizar_actualizacion_venta(request, pk):
    """
    Procesa la actualización de una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            venta.id_clie = get_object_or_404(Cliente, id=id_clie)
            venta.id_prod = get_object_or_404(Producto, id=id_prod)
            venta.total_venta = total_venta
            venta.estado = estado
            venta.id_empl = id_empl
            venta.save()
            return redirect('ver_ventas')
        except Exception as e:
            print(f"Error al actualizar venta: {e}")
            clientes = Cliente.objects.all()
            productos = Producto.objects.all()
            return render(request, 'Ventas/actualizar_venta.html', {
                'venta': venta,
                'clientes': clientes,
                'productos': productos,
                'error_message': f"Hubo un error al actualizar la venta: {e}"
            })
    return redirect('ver_ventas') # Redirige si se accede por GET


def borrar_venta(request, pk):
    """
    Borra una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    # Opcional: puedes renderizar una página de confirmación de borrado
    return render(request, 'Ventas/borrar_venta.html', {'venta': venta})
#-----------------------------------------------------------------------------------------------------------------------------------
# Cliente
#-----------------------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.db.models import Q # Importar Q para búsquedas

# Función de inicio para Delrio
def inicio_delrio(request):
    return render(request, 'inicio.html') # Asumiendo que tendrás una página de inicio general

# Función para agregar un nuevo cliente
def agregar_cliente(request):
    if request.method == 'POST':
        nom_clie = request.POST.get('nom_clie')
        apellido_clie = request.POST.get('apellido_clie')
        C_E_clie = request.POST.get('C_E_clie')
        tel_clie = request.POST.get('tel_clie')
        direc_clie = request.POST.get('direc_clie')
        fech_compra = request.POST.get('fech_compra') # Asegúrate de que el formato sea YYYY-MM-DD

        Cliente.objects.create(
            nom_clie=nom_clie,
            apellido_clie=apellido_clie,
            C_E_clie=C_E_clie,
            tel_clie=tel_clie,
            direc_clie=direc_clie,
            fech_compra=fech_compra
        )
        return redirect('ver_clientes') # Redirigir a la lista de clientes después de agregar
    return render(request, 'clientes/agregar_clientes.html')

# Función para ver todos los clientes
def ver_clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(
            Q(nom_clie__icontains=query) |
            Q(apellido_clie__icontains=query) |
            Q(C_E_clie__icontains=query)
        ).order_by('apellido_clie')
    else:
        clientes = Cliente.objects.all().order_by('apellido_clie')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

# Función para mostrar el formulario de actualización de un cliente
def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

# Función para procesar la actualización de un cliente
def realizar_actualizacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nom_clie = request.POST.get('nom_clie')
        cliente.apellido_clie = request.POST.get('apellido_clie')
        cliente.C_E_clie = request.POST.get('C_E_clie')
        cliente.tel_clie = request.POST.get('tel_clie')
        cliente.direc_clie = request.POST.get('direc_clie')
        cliente.fech_compra = request.POST.get('fech_compra')
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', cliente_id=cliente.id) # En caso de que se acceda directamente sin POST

# Función para borrar un cliente
def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})