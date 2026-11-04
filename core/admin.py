from django.contrib import admin
from .models import Categoria
from .models import LugarPatrimonial

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):  #Admin de categoria, para que se muestre en el mnú de la Base de Datos.
    list_display = ["cod", "nombre", "descripcion"]
    ordering = ["cod"]
    
class PatrimoniosAdmin(admin.ModelAdmin):
    list_display = ["cod","nombre","descripcion", "ubicacion", "anio_construccion"]
    ordering = ["nombre"]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(LugarPatrimonial, PatrimoniosAdmin)