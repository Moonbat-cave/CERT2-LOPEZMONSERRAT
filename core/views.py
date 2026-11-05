from django.shortcuts import render
from django.contrib.auth.models import User # Acceder a los usuarios en la base de datos.
from django.contrib import messages # Dejar mensajes, útil para mensajes de error

# Create your views here.
def principal(request):
    return render(request, "core/principal.html")

def catalogo(request):
    return render(request, "core/catalogo.html")

def cuentaConfig(request):
    dicc = {}
    if request.user.is_authenticated:
        dicc = {
            "nombre": request.user.username,
            "correo": request.user.email    
            }
    return render(request, "core/cuentaConf.html", dicc)

def detalle(request):
    return render(request, "core/lugarDetalle.html")

def registrar(request):
    if request.method == "POST": #Verificar que el request sea POST, ver en form del HTML
        username = request.POST.get("username")
        contraseña = request.POST.get("password")
        correo = request.POST.get("email")
        
        #Verificar si existe el nombre de usuario.
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nombre de usuario ya en uso.") #Mensaje de error
        else:
            user = User.objects.create_user(username=username, password=contraseña, email=correo)
            user.save()
            messages.success(request, "Cuenta registrada con éxito, ya puede iniciar sesión.") #Mensaje de éxito
            
    return render(request, "core/principal.html")

def gestion(request):
    return render(request, "core/gestion.html")