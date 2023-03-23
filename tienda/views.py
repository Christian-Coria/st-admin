from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import View
from tienda.forms import CargarForm
from product.models import Producto
from product.forms import SearchProducto
import json
from django.http import HttpResponse

#from django.middleware.csrf import get_token

def cargar_imagen(request):
    params={}

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form']=form
        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            imagen = form.cleaned_data['imagen']
            descripcion = form.cleaned_data['descripcion']
            precio = form.cleaned_data['precio']
            categoria = form.cleaned_data['categoria']
            condicion = form.cleaned_data['condicion']

            nuevo_producto = Producto(producto=producto, fecha_publicacion = fecha_publicacion, 
                imagen=imagen, descripcion = descripcion, precio = precio, categoria = categoria, condicion = condicion)
            nuevo_producto.save()
            return redirect('ver_imagenes')

    else:
        form=CargarForm
        params['form']= form
        return render(request, 'tienda/cargar_producto.html', params)


class VerImagenes(View):
    template = "tienda/ver_imagenes.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"]= productos

        return render(request, self.template, params)

    def post(self, request):
        params={}
        producto=request.POST.get("producto")
        el_pedido=request.session.get("el_pedido")
        if el_pedido:
            cantidad = el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]=cantidad+1
            else:
                el_pedido[producto]=1
        else:
            el_pedido={}
            el_pedido[producto]=1

        request.session["el_pedido"]=el_pedido
        print(request.session["el_pedido"])

        return redirect('ver_imagenes')

        

def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto

    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        raise Http404
    params["productos"]= productos

    
    return render(request, "tienda/ver_imagen.html", params)

    

class Carrito(View):
    template = "tienda/carrito.html"

    def get(self, request):
        params={}
        print(request.user)
        producto = Producto.objects.filter(
            Q(estado="Publicado"),
            )

        params["los_productos"]=producto
       
        return render(request, self.template, params)
 

class EjemploLocalStorage(View):
    template = "tienda/localstorage.html"
    
    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        """
        PARA INICIAR LA VARIABLE DE SESSION
        """
        try:
            request.session["carro"] 
        except:
            request.session["carro"] = {}

        return render(request, self.template, params)


def para_ajax(request):
    params={}
    search = SearchProducto()
    params["search"]=search
    return render(request, "tienda/ver_ajax.html", params)


class BuscarProducto(View):
    def get(self, request):
        if request.is_ajax:
            palabra=request.GET.get('term', '')
            print(palabra)
            busqueda=Producto.objects.filter(producto__icontains=palabra)
            result=[]
            for an in busqueda:
                data={}
                data['label']=an.producto
                result.append(data)
            data_json=json.dumps(result)
        else:
            data_json="fallo"
        mimetype="application/json"
        return HttpResponse(data_json, mimetype)


class BuscarProducto2(View):
    def get(self, request):
        #csrf_token = get_token(request)
        if request.is_ajax:
            q = request.GET
            ['valor']
            busqueda2 = Producto.objects.filter(producto__icontains=q)
            results = []
            for rec in busqueda2:
                print(rec.producto)
                print(rec.estado)
                print(rec.imagen)

                data = {}
                data['producto'] = rec.producto
                data['estado'] = rec.estado
                data['ruta_imagen'] = str(rec.imagen)
                results.append(data)
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
        

