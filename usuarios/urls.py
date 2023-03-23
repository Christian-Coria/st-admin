from django.urls import path
from usuarios import views
from usuarios.views_login import pagina_login
from usuarios.views_logout import pagina_logout
from usuarios.views_registro import pagina_registro
from usuarios.views_perfil import perfil
from usuarios.views_perfil import EditarPerfil

urlpatterns = [
    path('login', pagina_login, name="login"),
    path('logout', pagina_logout, name="logout"),
    path('registro', pagina_registro, name="registro"),
    path("perfil", perfil, name="perfil"),
    path("editar_perfil/<int:pk>/", EditarPerfil.as_view(), name="editar_perfil"),

]