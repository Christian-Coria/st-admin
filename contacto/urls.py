from django.urls import path
from contacto.views import Contacto
from contacto.views import MensajeEnviado

urlpatterns=[
    path('contato', Contacto.as_view(), name='contacto'),
    path('mensaje_enviado', MensajeEnviado.as_view(), name='mensaje_enviado'),
]