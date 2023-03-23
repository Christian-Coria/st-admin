from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Consulta
        exclude = ('estado_respuesta','fecha') #verificar este agregado para que no diera error por la falta de fields
        field=[
            'nombre',
            'descripcion',
            'email',
            'telefono',
           
        ]

    def send_email(self, ):
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        email = self.cleaned_data['email']
        telefono = self.cleaned_data['telefono']

        #apartir de aqui logica de envio de email
