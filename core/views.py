from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User # Acceder a los usuarios en la base de datos.
from django.contrib import messages # Dejar mensajes, útil para mensajes de error
from .models import LugarPatrimonial
from .models import Categoria

# Create your views here.
def principal(request):
    lugares = LugarPatrimonial.objects.all()
    categorias = Categoria.objects.all()
    
    contexto = {
        "lugares": lugares,
        "categorias": categorias
    }
    
    return render(request, "core/principal.html", contexto)

def catalogo(request):
    categoria_cod = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    
    # Filtramos los lugares según la categoría o mostramos todos
    if categoria_cod:
        lugares = LugarPatrimonial.objects.filter(categoria__cod=categoria_cod)
    else:
        lugares = LugarPatrimonial.objects.all()
        
    context = {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_activa': categoria_cod
    }
    return render(request, 'core/catalogo.html', context)

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
            
    return redirect("/")

def gestion(request):
    contexto = {
        'usuarios': User.objects.all(),
        'lugares': LugarPatrimonial.objects.all(),
        'categorias': Categoria.objects.all()
    }
    return render(request, 'core/gestion.html', contexto)


def crear_lugar(request):
    if request.method == "POST":
        codP = request.POST.get("codeP")
        nombreP = request.POST.get("nombreP")
        descripcionP = request.POST.get("descripcionP")
        anioP = request.POST.get("anioConstruccion")
        ubicacionP = request.POST.get("ubicacionP")
        imagenP = request.POST.get("imagenP")
        categoriaP = request.POST.get("Categoria")
        
        if LugarPatrimonial.objects.filter(cod=codP).exists():
            messages.error(request, "El Código del lugar ya existe en la base de datos.")
        else:
            categoria_obj = get_object_or_404(Categoria, cod=categoriaP)
            LugarPatrimonial.objects.create(cod=codP, nombre=nombreP, descripcion=descripcionP, anio_construccion=int(anioP), ubicacion=ubicacionP, imagen=imagenP, categoria=categoria_obj)
            messages.success(request, "Lugar creado con éxito")
    
    return redirect("/")

def crear_categoria(request):
    if request.method == "POST":
        codCat = request.POST.get("codeCat")
        nombreCat = request.POST.get("nombreCat")
        descripcionCat = request.POST.get("descripcionCat")

        # 1. Validar si el código de la categoría ya existe en la base de datos
        if Categoria.objects.filter(cod=codCat).exists():
            messages.error(request, "El código de la categoría ya existe.")
        else:
            # 2. Crear y guardar la nueva categoría
            Categoria.objects.create(
                cod=codCat,
                nombre=nombreCat,
                descripcion=descripcionCat
            )
            messages.success(request, "¡Categoría creada con éxito!")
            
    return redirect("/")

def eliminar_lugar(request, cod):
    lugar = get_object_or_404(LugarPatrimonial, cod=cod)
    lugar.delete()
    messages.success(request, "Lugar patrimonial eliminado con éxito.")
    return redirect('gestion')

def eliminar_categoria(request, cod):
    categoria = get_object_or_404(Categoria, cod=cod)
    categoria.delete()
    messages.success(request, "Categoría eliminada con éxito.")
    return redirect('gestion')

# --- MODIFICAR ---
def modificar_lugar(request, cod):
    lugar = get_object_or_404(LugarPatrimonial, cod=cod)
    if request.method == "POST":
        lugar.nombre = request.POST.get("nombreP")
        lugar.descripcion = request.POST.get("descripcionP")
        lugar.anio_construccion = int(request.POST.get("anioConstruccion") or 0)
        lugar.ubicacion = request.POST.get("ubicacionP")
        lugar.imagen = request.POST.get("imagenP")
        
        categoria_cod = request.POST.get("Categoria")
        categoria_obj = Categoria.objects.filter(cod=categoria_cod).first()
        if categoria_obj:
            lugar.categoria = categoria_obj
            
        lugar.save()
        messages.success(request, "Lugar modificado con éxito.")
    return redirect('gestion')

def modificar_categoria(request, cod):
    categoria = get_object_or_404(Categoria, cod=cod)
    if request.method == "POST":
        categoria.nombre = request.POST.get("nombreCat")
        categoria.descripcion = request.POST.get("descripcionCat")
        categoria.save()
        messages.success(request, "Categoría modificada con éxito.")
    return redirect('gestion')