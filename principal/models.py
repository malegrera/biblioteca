from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import timedelta

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    editorial = models.CharField(max_length=150)
    anio_publicacion = models.PositiveIntegerField()
    autores = models.ManyToManyField(Autor)
    categorias = models.ManyToManyField(Categoria)
    portada = models.ImageField(
        upload_to="portadas/",
        blank=True
    )

    def __str__(self):
        return self.titulo



class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    codigo_inventario = models.CharField(max_length=50, unique=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('fuera_servicio', 'Fuera de servicio'),
        ],
        default='activo'
    )

    def __str__(self):
        return f"{self.libro.titulo} ({self.codigo_inventario})"

class Socio(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    fecha_alta = models.DateField()

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"

class Prestamo(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.PROTECT)
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.PROTECT)
    fecha_prestamo = models.DateField()
    fecha_vencimiento = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ejemplar"],
                condition=models.Q(fecha_devolucion__isnull=True),
                name="un_prestamo_activo_por_ejemplar"
            )
        ]

    def clean(self):
        super().clean()

        if self.ejemplar_id and self.ejemplar.estado == "fuera_servicio":
            raise ValidationError(
                "No se puede prestar un ejemplar fuera de servicio."
            )
        if self.socio_id and self.fecha_devolucion is None:
            prestamos_socio = Prestamo.objects.filter(
                socio=self.socio,
                fecha_devolucion__isnull=True
            ).exclude(pk=self.pk)

            if prestamos_socio.count() >= 3:
                raise ValidationError(
                    "Este socio ya tiene 3 préstamos activos."
                )
        if self.fecha_devolucion is None:
            prestamos_activos = Prestamo.objects.filter(
                ejemplar=self.ejemplar,
                fecha_devolucion__isnull=True
            ).exclude(pk=self.pk)

            if prestamos_activos.exists():
                raise ValidationError(
                    "Este ejemplar ya tiene un préstamo activo."
                )
        if self.fecha_prestamo and self.fecha_vencimiento:
            if self.fecha_vencimiento < self.fecha_prestamo:
                raise ValidationError(
                    "La fecha de vencimiento no puede ser anterior "
                    "a la fecha del préstamo."
                )
        if self.fecha_prestamo and self.fecha_devolucion:
            if self.fecha_devolucion < self.fecha_prestamo:
                raise ValidationError(
                    "La fecha de devolución no puede ser anterior "
                    "a la fecha del préstamo."
                )

    def __str__(self):
        return f"{self.socio} - {self.ejemplar.libro.titulo} ({self.ejemplar.codigo_inventario})"
