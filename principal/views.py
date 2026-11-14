from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from .serializers import LibroSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Libro, Prestamo, Ejemplar, Socio


def catalogo(request):
    prestamos_activos = Prestamo.objects.filter(
        fecha_devolucion__isnull=True
    ).values("ejemplar_id")

    libros = Libro.objects.annotate(
        disponibles=Count(
            "ejemplar",
            filter=(
                Q(ejemplar__estado="activo")
                & ~Q(ejemplar__id__in=prestamos_activos)
            ),
            distinct=True
        )
    )
    return render(request, "catalogo.html", {"libros": libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    prestamos_activos = Prestamo.objects.filter(
        fecha_devolucion__isnull=True
    ).values("ejemplar_id")

    disponibles = Ejemplar.objects.filter(
        libro=libro,
        estado="activo"
    ).exclude(
        id__in=prestamos_activos
    ).count()

    return render(request, "detalle_libro.html", {
        "libro": libro,
        "disponibles": disponibles
    })

@login_required
def mis_prestamos(request):
    if request.user.is_staff:
        raise PermissionDenied

    socio = get_object_or_404(Socio, usuario=request.user)

    prestamos = Prestamo.objects.filter(
        socio=socio
    ).select_related("ejemplar__libro").order_by("-fecha_prestamo")

    return render(request, "mis_prestamos.html", {
        "prestamos": prestamos
    })

class LibroListAPIView(ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroDetailAPIView(RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer