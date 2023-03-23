from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.views.generic import DetailView
from usuarios.models import DatosUsuario
from usuarios.forms import MyUserEditForm
from django.urls import reverse_lazy



@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')


class EditarPerfil(LoginRequiredMixin,UpdateView):
    model = DatosUsuario
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('perfil')
    fields = ['nombre','apellido','pais', 'provincia', 'ciudad',
    'domicilio', 'codigo_postal', 'telefono' ,'celular','documento', 'cuit','avatar']


     


        
        
