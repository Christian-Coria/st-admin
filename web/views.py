from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request,'index.html')


class About(TemplateView):
    template_name = "about.html"


class Construccion(TemplateView):
    template_name = "en_construccion.html"


def preguntas_frecuentes(request):
    return render(request,'preguntas_frecuentes.html')

def reglamento(request):
    return render(request,'reglamento.html')

