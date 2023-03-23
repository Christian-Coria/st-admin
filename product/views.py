from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from product.models import Producto



def product(request):
    params = {}
    params['nombre_sitio'] = 'EnLinea'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto
    print(producto)
    return render(request, 'product/product.html', params)


# def get_buscar_producto(self, request):
    
        #     if 'q' in request.GET:
        #         q = request.GET['q']
        #         all_producto_list = Producto.objects.filter(Q(producto__icontains=q)).order_by('producto'),
                
        #     else:
        #         all_producto_list = Producto.objects.all().order_by('producto')                
                
        #     return render(request, self.template, {"all_Producto_list":all_producto_list})
