from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, "core/principal.html")

def catalogo(request):
    return render(request, "core/catalogo.html")

def login(request):
    return render(request, "core/login.html")

def detalle(request):
    return render(request, "core/lugarDetalle.html")