#Certamen 2

Paso a paso de la Terminal para crear proyecto:
>pip install django
>cd CERT2-LOPEZMONSERRAT
>django-admin startproject CER2_LOPEZMONSERRAT
>cd CER2_LOPEZMONSERRAT
>py manage.py startapp core
>py manage.py runserver

Paso a paso para crear super usuario:
>py manage.py createsuperuser
*Crear nombre de usuario*
*Ingresar correo (opcional)*
*Crear contraseña*

Paso a paso para hacer migrations:
>py manage.py makmigrations (Revisa cambios o nuevos módulos)
>py mangae.py migrations (Liga los módulos con la base de datos)

Se requiere de:
Python versión 3 en adelate
Django instalado
Pip instalado

Se crearon dos usuarios para probar el sistema de administración, uno de los ususarios tiene permisos totales (Puede borrar, modificar y crear cualquier entidad), y un usuario común (Solo puede registrar lugares), los usuarios invitados no pueden ni crear ni modificar nada.
