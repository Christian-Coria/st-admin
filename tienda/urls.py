from django.urls import path
from tienda import views
from tienda.views_agregar import agregar
from tienda.views import VerImagenes
from tienda.views import Carrito
from tienda.views import EjemploLocalStorage
from tienda.views import para_ajax
from tienda.views import BuscarProducto
from tienda.views import BuscarProducto2

urlpatterns = [
    path('cargar_producto/', views.cargar_imagen, name='cargar_producto'), 
    path('<int:producto_id>/ver_imagen/', views.ver_imagen, name='ver_imagen'),
    path('ver_imagenes/', VerImagenes.as_view(), name='ver_imagenes'),
    path('carrito/', Carrito.as_view(), name='carrito'),
    path('localstorage/', EjemploLocalStorage.as_view(), name="localstorage"),
    path("agregar/", agregar, name="agregar"),
    path("ver_ajax/", para_ajax, name="ver_ajax"),
    path('buscar_producto/' , BuscarProducto.as_view(), name="buscar_producto"),
    path('buscar_producto2/', BuscarProducto2.as_view(), name="buscar_producto2"),
]