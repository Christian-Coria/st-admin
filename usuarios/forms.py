from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1", "password2"]


class MyUserEditForm(forms.Form):

    email = forms.EmailField(required=False)
    nombre = forms.CharField(label='Nombre', max_length=30, required=False)
    apellido = forms.CharField(label='Apellido', max_length=30, required=False)
    pais = forms.CharField(label='Pais', max_length=30, required=False)
    provincia = forms.CharField(label='Provincia', max_length=30, required=False)
    ciudad = forms.CharField(label='Ciudad', max_length=30, required=False)
    domicilio = forms.CharField(label='Domicilio', max_length=30, required=False)
    codigo_postal = forms.CharField(label='Codigo Postal', max_length=30, required=False)
    telefono = forms.CharField(label='Telefono', max_length=30, required=False)
    celular = forms.CharField(label='Celular', max_length=30, required=False)
    documento = forms.CharField(label='Documento', max_length=30, required=False)
    cuit = forms.CharField(label='Cuit', max_length=30, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Repetir Password', widget=forms.PasswordInput, required=False)
    avatar = forms.ImageField(required=False)


# class EditarPerfil(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ["username","email",'nombre','apellido','pais', 'provincia', 'ciudad',
#         'domicilio', 'codigo_postal', 'telefono' ,'celular','documento', 'cuit','avatar']