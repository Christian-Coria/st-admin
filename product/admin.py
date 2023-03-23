from django.contrib import admin
from product.models import Producto 
from product.models import Categoria
from django .http import HttpResponse
from django.core import serializers
from django.shortcuts import render 


class ProductoInLine(admin.TabularInline):
    model = Producto
    extra = 0 #indicamos la cantidad de productos que podemos agregar


class CategoriaAdmin(admin.ModelAdmin): #esta clase customiza ... asocia las clases
    inlines = [ProductoInLine]


# def publicar(modeladmin, request, queryset):             fuera de la clase es una rutina...
#     queryset.update(estado="publicado")


# publicar.short_description = "Pasar a publicado"


#@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):   #Filtro para el panel de administracion y mostrar lo que se decida en el orden que se elija
    #fields = ['fecha_publicacion', 'producto', 'estado' ,'imagen']
     fieldsets = [
         ("Relacion", {"fields": ["categoria"]}),
         (
            "Datos generales", 
              {"fields": 
                  ['fecha_publicacion', 'producto',  'descripcion', 'estado' ,'imagen','condicion']}

         ),
         ("Detalle", 
              {"fields": 
                  ['stock', 'precio','descuento']}

         )
         
     ]
     list_display = ['tipo_de_producto','producto','fecha_publicacion', 'imagen'] #visualizamos en forma de columnas 
     ordering = ['-fecha_publicacion']    #ordenamos por fecha de publicacion en este caso el signo menos es para alterar el orden natural
     list_filter = ('producto', 'fecha_publicacion',) # list_filter es una tupla que permite filtrar
     search_fields = ('producto', 'estado',) # search_fields agrega opciones de busquedas
     list_display_links = ('producto', 'fecha_publicacion',) #agrega links a cada columna para ingreso por click
     actions=["publicar", "exportar_a_json", "ver_productos"]
     
     @admin.display(description='Name')  #customizamos el panel con una logica ... en este caso cambia a mayuscula los objetos
     def upper_case_name(self, obj):
         return ("%s %s" % (obj.producto, obj.estado)).upper() # pasamos a mayuscula el producto y el estado

     def publicar(self, request, queryset):             #fuera de la clase es una rutina... cambiaos modeladmin por self  y e actions a publicar lo ponemos entre " " /convirtiendo asi un metodo de la clase 
        registro = queryset.update(estado="publicado")

        if registro == 1:
            mensage = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
            self.message_user(request, "%s exitosamente" % mensaje)
        publicar.short_description = "Pasar a publicado"

     def exportar_a_json(self, request, queryset):
        response = HttpResponse(content_type = "application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

     def ver_productos(self, request, queryset):
        params={}
        productos=Producto.objects.all
        params["productos"]=productos
        return render(request, "admin/productos/productos.html", params)

     ver_productos.short_description = "Ver Productos"
admin.site.register(Producto,ProductoAdmin) #en lugar de esta linea podemos replazar por el decorador @admin.register(Producto)
admin.site.register(Categoria,CategoriaAdmin)
#admin.site.register(Producto)
#admin.site.register(Categoria)
