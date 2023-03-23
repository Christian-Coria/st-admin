from django.forms import ModelForm
from .models import Producto
from django import forms


class SearchProducto(forms.Form):
    querycom = forms.CharField(label='Ingresa Producto a buscar ', widget=forms.TextInput(attrs={'size': 32, 'class': 'form- control'}))


class CargarForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["producto", "fecha_publicacion", "imagen"]

        error_messages = {
            "producto": {
                "required": ("Se debe agregar un nombre de producto"),
            },
            "fecha_publicacion": {
                "required": (
                    "Se debe agregar la fecha de publicación en el formato adecuado"
                ),
            },
        }

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)