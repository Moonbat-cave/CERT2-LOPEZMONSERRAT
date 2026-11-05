"""
URL configuration for CER2_LOPEZMONSERRAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views # Obtener la forma automática de conectar el inicio de sesión con la BD.
from core import views

urlpatterns = [
    path('admin/', admin.site.urls), #Sitio admin
    path("", views.principal), #Sitio principal
    path("catalogo/", views.catalogo, name="catalogo"), # Sitio Catálogo
    path('login/', auth_views.LoginView.as_view(template_name='core/principal.html'), name='login'), #Inicio de sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Cerrar sesión
    path("detalle/", views.detalle, name="detalle"), # Ver detalle patrimonio.
    path("register/", views.registrar, name="register"), # Registrarse.
    path("gestion/", views.gestion, name="gestion"), # Sitio gestión de la página.
    path("lugar/", views.crear_lugar, name="crear_lugar"),
    path("categoria/", views.crear_categoria, name="crear_categoria"),
    path('lugar/modificar/<str:cod>/', views.modificar_lugar, name='modificar_lugar'),
    path('lugar/eliminar/<str:cod>/', views.eliminar_lugar, name='eliminar_lugar'),
    path('categoria/modificar/<str:cod>/', views.modificar_categoria, name='modificar_categoria'),
    path('categoria/eliminar/<str:cod>/', views.eliminar_categoria, name='eliminar_categoria'),
]
