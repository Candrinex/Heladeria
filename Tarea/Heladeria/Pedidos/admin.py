from django.contrib import admin
from django import forms  # Importamos forms para los formularios personalizados
from django.forms import TextInput
from .models import Admin as AdminModel, Cliente, Empleado, Helado, Cantidad, Salsa, Pedido, DIAS_CHOICES

# Registro Empleado
class EmpleadoAdminForm(forms.ModelForm):
    dias_trabaja = forms.MultipleChoiceField(
        choices=DIAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,  # O puedes usar un MultipleSelect si prefieres
    )

    class Meta:
        model = Empleado
        fields = '__all__'

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoAdminForm
    list_display = ('nombre_completo', 'turno_entrada', 'turno_salida', 'dias_trabaja')


# Registro del modelo Admin
@admin.register(AdminModel)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Registro del modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario',)

# Personalización del modelo Helado para usar el selector de color
class HeladoAdminForm(forms.ModelForm):
    class Meta:
        model = Helado
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

@admin.register(Helado)
class HeladoAdmin(admin.ModelAdmin):
    form = HeladoAdminForm
    list_display = ('helado', 'color')
    search_fields = ('helado',)

# Personalización del modelo Salsa para usar el selector de color
class SalsaAdminForm(forms.ModelForm):
    class Meta:
        model = Salsa
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

@admin.register(Salsa)
class SalsaAdmin(admin.ModelAdmin):
    form = SalsaAdminForm
    list_display = ('salsa', 'color')
    search_fields = ('salsa',)

# Registro del modelo Cantidad
@admin.register(Cantidad)
class CantidadAdmin(admin.ModelAdmin):
    list_display = ('cantidad',)
    search_fields = ('cantidad',)

# Registro del modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cantidad', 'helado', 'salsa')
    search_fields = ('cliente__usuario',)
    list_filter = ('helado', 'salsa')
