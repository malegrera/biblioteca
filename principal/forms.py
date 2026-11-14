from django import forms
from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = "__all__"
        widgets = {
            "fecha_prestamo": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
            "fecha_vencimiento": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
            "fecha_devolucion": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            ),
        }