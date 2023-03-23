from django.forms import ModelForm
from product.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model=Producto
        fields = ['producto', 'fecha_publicacion', 'imagen', 'descripcion', 'precio', 'categoria', 'condicion']
    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)
