from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from servicio_tecnico.models import  Task, Proveedores,Cliente,Reparacion, PedidoEspecial, Transferencia, Pyme
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.core.paginator import Paginator
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import pdf_decorator
from datetime import datetime
import datetime


def buscar(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        print(request.user)
        all_reparacion_list = Reparacion.objects.filter(Q(cliente__nombre_completo__icontains=q)).order_by('cliente')
        
    else:
        all_reparacion_list = Reparacion.objects.filter(
            Q(estado='Pendiente'), Q(tecnico=request.user)
            )                
        
    return render(request, 'servicio_tecnico/buscar.html', {"all_reparacion_list":all_reparacion_list})


class Templatetags1(View):
    template = "servicio_tecnico/verificar_remito.html"

    def get(self, request):
        params={}
        print(request.user)
        reparacion_list = Reparacion.objects.filter(
            Q(estado='Pendiente'), Q(tecnico=request.user)
            )

        params["all_reparacion_list"]=reparacion_list
        params["row1"]="row1"

        return render(request, self.template, params)


class ListarProveedores(LoginRequiredMixin,ListView):
    model = Proveedores
    template_name = "servicio_tecnico/listar_proveedores.html"
    context_object_name = 'proveedores'

    # def get(self):
    #     params={}
    #     user_id=request.user.id

    #     proveedores = Proveedores.objects.filter(
    #         Q(user_id='user_id')
    #         )

    #     params["proveedores"]=proveedores


class ClienteMin(TemplateView):
    template_name = "servicio_tecnico/presupuesto.html"

class Actualizacion(TemplateView):
    template_name = "servicio_tecnico/actualizacion.html"


class CheckImei(TemplateView):
    template_name = "servicio_tecnico/creck_imei.html"


class CursoTecnico(TemplateView):
    template_name = "servicio_tecnico/curso_tecnico.html"


class Curso(LoginRequiredMixin, TemplateView):
    template_name = "servicio_tecnico/curso.html"


class ListarClientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "servicio_tecnico/listar_clientes.html"


class CrearCliente(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "servicio_tecnico/crear_cliente.html"
    success_url = 'listar-clientes'
    fields = ['nombre_completo','telefono','documento']


class EditarCliente(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name ='servicio_tecnico/editar_cliente.html'
    success_url = reverse_lazy('listar_clientes')
    fields = ['nombre_completo','telefono','documento']   


class EliminarCliente(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "servicio_tecnico/eliminar_cliente.html"
    success_url = reverse_lazy('listar_clientes')


class ListarIngresos(LoginRequiredMixin, ListView):
    model = Reparacion
    template_name = "servicio_tecnico/listar_ingresos.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(user=self.request.user)

    
    # def get_queryset(self, *args,**kwargs):
    #     return Reparacion.objects.filter(user=self.request.user)

    # def get_queryset(self, *args,**kwargs):
    #     return request.user.objects.all()


class CrearIngreso(LoginRequiredMixin,CreateView):
    model = Reparacion
    template_name = "servicio_tecnico/crear_ingreso.html"
    success_url = 'buscar'
    fields = ['cliente','whatsApp','marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'pago_seña','precio', 'estado','tecnico']


class CrearProveedor(LoginRequiredMixin,CreateView):
    model = Proveedores
    template_name = "servicio_tecnico/crear_proveedor.html"
    success_url = 'listar-proveedores'
    fields = ['nombre','telefono','tecnico']


class CrearPedidoEspecial(LoginRequiredMixin,CreateView):
    model = PedidoEspecial
    template_name = "servicio_tecnico/bajo_pedido.html"
    success_url = 'index'
    fields = ['nombre','telefono','solicitud','imagen']


class CrearTransferencia(LoginRequiredMixin,CreateView):
    model = Transferencia
    template_name = "cuentas_bancarias.html"
    success_url = 'index'
    fields = ['nombre','telefono','pedido_numero','foto']


class EditarIngreso(LoginRequiredMixin,UpdateView):
    model = Reparacion
    template_name = 'servicio_tecnico/editar_ingreso.html'
    success_url = reverse_lazy('buscar')
    fields = ['cliente','marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'pago_seña','precio', 'estado','tecnico', 'accion']


class EditarRemito(UpdateView):
    model = Reparacion
    template_name = 'servicio_tecnico/editar_remito.html'
    success_url = reverse_lazy('verificar_remito')
    fields = ['estado']

class EliminarIngreso(LoginRequiredMixin,DeleteView):
    model = Reparacion
    template_name = "servicio_tecnico/eliminar_ingreso.html"
    success_url = reverse_lazy('listar_ingresos')


class MostrarCliente(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = 'servicio_tecnico/mostrar_cliente.html'
    

class MostrarProveedor(LoginRequiredMixin,DetailView):
    model = Proveedores
    template_name = "servicio_tecnico/mostrar_proveedor.html"
    

class MostrarIngreso(LoginRequiredMixin,DetailView):
    model = Reparacion
    template_name = "servicio_tecnico/mostrar_ingreso.html"


class PdfIngreso(PdfMixin,DetailView):
    model = Reparacion
    template_name = "servicio_tecnico/pdf_ingreso.html"


class EditarProveedor(LoginRequiredMixin,UpdateView):
    model = Proveedores
    template_name = "servicio_tecnico/editar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')
    fields = ['nombre','telefono','tecnico']


class EliminarProveedor(LoginRequiredMixin,DeleteView):
    model = Proveedores
    template_name = "servicio_tecnico/eliminar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')


class CrearPyme(LoginRequiredMixin,CreateView):
    model = Pyme
    template_name = "servicio_tecnico/pyme.html"
    success_url = 'empresa'
    fields = ['nombre','telefono','direccion','foto', 'descripcion']

@login_required
def empresa(request):
    return render(request, 'servicio_tecnico/empresa.html')


class EditarOrden(UpdateView):
    model = Reparacion
    template_name = 'servicio_tecnico/estado_edicion.html'
    success_url = reverse_lazy('estado_orden')
    fields = ['accion']


def buscar_documento(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        print(request.user)
        all_reparacion_list = Reparacion.objects.filter(Q(cliente__documento__icontains=q)).order_by('cliente')
        
    else:
        all_reparacion_list = Reparacion.objects.filter(
            Q(estado='Pendiente'), Q(tecnico=request.user)
            )                
        
    return render(request, 'servicio_tecnico/estado_orden.html', {"all_reparacion_list":all_reparacion_list})