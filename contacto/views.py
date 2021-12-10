from django.shortcuts import render,redirect
from .forms import FormularioContacto

# Create your views here.
def contacto(request):

    formulario_contacto=FormularioContacto() #Contenido del formulario de contacto

    if request.method=="POST":
            formulario_contacto=FormularioContacto(data=request.POST) 
            if formulario_contacto.is_valid():
                nombre=request.POST.get("nombre")
                email=request.POST.get("email")
                comentario=request.POST.get("comentario")

                return redirect("/contacto/?valido")

    return render(request,"contacto/contacto.html",{'formulario':formulario_contacto})