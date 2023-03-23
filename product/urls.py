from django.urls import path
from product.views import product


from web.views import preguntas_frecuentes

urlpatterns = [
    path('procuct',product, name="product"),
    
]