from django.contrib import admin
from .models import Autor, Categoria, Libro, Ejemplar, Socio, Prestamo
from .forms import PrestamoForm

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Socio)
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    form = PrestamoForm

    class Media:
        js = ("js/prestamos.js",)