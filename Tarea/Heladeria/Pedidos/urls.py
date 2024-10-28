from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),     # Ruta para la página de inicio
    path('login/', views.login, name='login'), # Ruta para la página de iniciar sesión (login)

    #Empleados
    path('empleado/', views.empleado, name='empleado'),  
    path('empleado/general/', views.general_empleado, name='general_empleado'),
    path('empleado/ver_pedidos/', views.ver_pedidos_empleado, name='ver_pedidos_empleado'),        
    path('empleado/ver_sabor_empleado/', views.ver_sabor_empleado, name='ver_sabor_empleado'),
    path('empleado/crear_helado/', views.crear_helado, name='crear_helado'),
    path('empleado/crear_salsa/', views.crear_salsa, name='crear_salsa'), 
    path('empleado/borrar_pedido/<int:id>/', views.borrar_pedido, name='borrar_pedido'),
    path('empleado/helado/borrar/<int:id>/', views.borrar_helado, name='borrar_helado'),
    path('empleado/salsa/borrar/<int:id>/', views.borrar_salsa, name='borrar_salsa'),    
    path('empleado/helado/editar/<int:id>/', views.editar_helado, name='editar_helado'),
    path('empleado/salsa/editar/<int:id>/', views.editar_salsa, name='editar_salsa'), 
    path('empleado/crear_pedido/', views.crear_pedido, name='crear_pedido'),

    #Clientes
    path('cliente/', views.cliente, name='cliente'),
    path('cliente/crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('cliente/crear_pedido_cliente/<int:cliente_id>/', views.crear_pedido_cliente, name='crear_pedido_cliente'),
    path('cliente/ver_mis_pedidos/<int:cliente_id>/', views.ver_mis_pedidos, name='ver_mis_pedidos'),
    path('cliente/general/<int:cliente_id>/', views.general_cliente, name='general_cliente'),
]
