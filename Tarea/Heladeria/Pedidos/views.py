from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Pedido, Helado, Salsa, Cliente, Cantidad
from django.contrib import messages

# Vista general para cliente
def general_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'Cliente/general_cliente.html', {'cliente': cliente})

# Vista para ver los pedidos de un cliente
def ver_mis_pedidos(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    pedidos = Pedido.objects.filter(cliente=cliente)
    return render(request, 'Cliente/ver_mis_pedidos.html', {
        'cliente': cliente,
        'pedidos': pedidos
    })

# Vista para que el cliente cree un pedido
def crear_pedido_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cantidad_id = request.POST.get('cantidad')
        helado_id = request.POST.get('helado')
        salsa_id = request.POST.get('salsa')

        cantidad = Cantidad.objects.get(id=cantidad_id)
        helado = Helado.objects.get(id=helado_id)
        salsa = Salsa.objects.get(id=salsa_id)

        nuevo_pedido = Pedido(cliente=cliente, cantidad=cantidad, helado=helado, salsa=salsa)
        nuevo_pedido.save()

        return redirect('ver_mis_pedidos', cliente_id=cliente.id)

    cantidades = Cantidad.objects.all()
    helados = Helado.objects.all()
    salsas = Salsa.objects.all()

    return render(request, 'Pedido/crear_pedido_cliente.html', {
        'cliente': cliente,
        'cantidades': cantidades,
        'helados': helados,
        'salsas': salsas
    })

# Vista de inicio de sesión para cliente
def cliente(request):
    error_message = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        try:
            cliente = Cliente.objects.get(usuario=usuario)
            if cliente.contrasena == contrasena:
                return redirect('general_cliente', cliente_id=cliente.id)
            else:
                error_message = "Usuario o contraseña incorrecta"
        except Cliente.DoesNotExist:
            error_message = "Usuario o contraseña incorrecta"

    return render(request, 'cliente.html', {'error_message': error_message})

# Vista para crear un cliente
def crear_cliente(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        if Cliente.objects.filter(usuario=usuario).exists():
            error_message = "El usuario ya existe. Por favor, elige otro."
            return render(request, 'crear_cliente.html', {'error_message': error_message})

        nuevo_cliente = Cliente(usuario=usuario, contrasena=contrasena)
        nuevo_cliente.save()

        return redirect('cliente')

    return render(request, 'Cliente/crear_cliente.html')

# Vista para crear un pedido
def crear_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cantidad_id = request.POST.get('cantidad')
        helado_id = request.POST.get('helado')
        salsa_id = request.POST.get('salsa')

        cliente = Cliente.objects.get(id=cliente_id)
        cantidad = Cantidad.objects.get(id=cantidad_id)
        helado = Helado.objects.get(id=helado_id)
        salsa = Salsa.objects.get(id=salsa_id)

        nuevo_pedido = Pedido(cliente=cliente, cantidad=cantidad, helado=helado, salsa=salsa)
        nuevo_pedido.save()

        return redirect('ver_pedidos_empleado')

    clientes = Cliente.objects.all()
    cantidades = Cantidad.objects.all()
    helados = Helado.objects.all()
    salsas = Salsa.objects.all()

    return render(request, 'Pedido/crear_pedido.html', {
        'clientes': clientes,
        'cantidades': cantidades,
        'helados': helados,
        'salsas': salsas
    })

# Vista para borrar un helado
def borrar_helado(request, id):
    helado = get_object_or_404(Helado, id=id)
    helado.delete()
    return redirect('ver_sabor_empleado')

# Vista para borrar una salsa
def borrar_salsa(request, id):
    salsa = get_object_or_404(Salsa, id=id)
    salsa.delete()
    return redirect('ver_sabor_empleado')

# Vista para borrar un pedido
def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('ver_pedidos_empleado')

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de login
def login(request):
    return render(request, 'login.html')

# Vistas para empleados
def general_empleado(request):
    return render(request, 'Empleado/general_empleado.html')

def ver_sabor_empleado(request):
    helados = Helado.objects.all()
    salsas = Salsa.objects.all()
    return render(request, 'Empleado/ver_sabor_empleado.html', {'helados': helados, 'salsas': salsas})

def ver_pedidos_empleado(request):
    pedidos = Pedido.objects.all()
    return render(request, 'Empleado/ver_pedidos_empleado.html', {'pedidos': pedidos})

# Vista para crear helado
def crear_helado(request):
    if request.method == 'POST':
        nombre_helado = request.POST.get('helado')
        color = request.POST.get('color')

        nuevo_helado = Helado(helado=nombre_helado, color=color)
        nuevo_helado.save()

        return redirect('ver_sabor_empleado')

    return render(request, 'Helado/crear_helado.html')

# Vista para crear salsa
def crear_salsa(request):
    if request.method == 'POST':
        nombre_salsa = request.POST.get('salsa')
        color = request.POST.get('color')

        nueva_salsa = Salsa(salsa=nombre_salsa, color=color)
        nueva_salsa.save()

        return redirect('ver_sabor_empleado')

    return render(request, 'Salsa/crear_salsa.html')

# Vista para editar un helado
def editar_helado(request, id):
    helado = get_object_or_404(Helado, id=id)
    if request.method == 'POST':
        helado.helado = request.POST.get('helado')
        helado.color = request.POST.get('color')
        helado.save()

        return redirect('ver_sabor_empleado')

    return render(request, 'Helado/editar_helado.html', {'helado': helado})

# Vista para editar una salsa
def editar_salsa(request, id):
    salsa = get_object_or_404(Salsa, id=id)
    if request.method == 'POST':
        salsa.salsa = request.POST.get('salsa')
        salsa.color = request.POST.get('color')
        salsa.save()

        return redirect('ver_sabor_empleado')

    return render(request, 'Salsa/editar_salsa.html', {'salsa': salsa})

# Vista de login para empleados
def empleado(request):
    empleados = Empleado.objects.all()
    error_message = None

    if request.method == "POST":
        nombre_completo = request.POST.get('nombre_completo')
        contrasena = request.POST.get('contrasena')

        try:
            empleado = Empleado.objects.get(nombre_completo=nombre_completo)
            if empleado.contrasena == contrasena:
                return redirect('general_empleado')
            else:
                error_message = "Contraseña incorrecta"
        except Empleado.DoesNotExist:
            error_message = "Usuario no encontrado"

    return render(request, 'empleado.html', {'empleados': empleados, 'error_message': error_message})
