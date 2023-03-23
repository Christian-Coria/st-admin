from django import forms
    

class FormCliente(forms.Form):
    nombre_completo = forms.CharField(max_length=40)
    telefono = forms.PhoneNumberField(nique = True, null = False, blank = False)
    documento = forms.CharField(max_length=40,  null = False, blank = False)

    
class FormProveedores(forms.Form):
    nombre = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)

class Formulario_reparacion(forms.Form):
    fecha = forms.DateTimeField(auto_now_add=True)
    
    equipo = forms.CharField(max_length=40)
    falla = forms.CharField(max_length=40)
    tipo_rep = forms.CharField(max_length=40)
    estado = forms.CharField(max_length=40)
    


