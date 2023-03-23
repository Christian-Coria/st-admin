from django.shortcuts import render
from usuarios.forms import CreateUserForm
from django.shortcuts import redirect

def pagina_registro(request):
    params={}
    form=CreateUserForm()
    params["form"]=form

    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "usuarios/registro.html", params)

    return render(request, "usuarios/registro.html", params)