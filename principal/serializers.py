from rest_framework import serializers
from .models import Libro, Ejemplar, Prestamo


class LibroSerializer(serializers.ModelSerializer):
    disponibles = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = [
            "id",
            "titulo",
            "isbn",
            "editorial",
            "anio_publicacion",
            "autores",
            "categorias",
            "portada",
            "disponibles",
        ]

    def get_disponibles(self, obj):
        prestamos_activos = Prestamo.objects.filter(
            fecha_devolucion__isnull=True
        ).values("ejemplar_id")

        return Ejemplar.objects.filter(
            libro=obj,
            estado="activo"
        ).exclude(
            id__in=prestamos_activos
        ).count()