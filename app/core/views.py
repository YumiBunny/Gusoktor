
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.core.forms import RegistroDesocupado, RegistroEmpresa
from app.core.forms import RegistroOferta
from app.core.models import *

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})

def registro_oferta(request):
    if request.method == "GET":
        return get_registro_oferta_form(request)
    elif request.method == 'POST':
        return handle_registro_oferta_form(request)

def get_registro_oferta_form(request):
    form = RegistroOferta()
    return render(request, 'registrar_oferta.html', {'form': form})

def handle_registro_oferta_form(request):
    form = RegistroOferta(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'registrar_oferta.html', {'form': form})


def eliminar(request):
	id_eliminar = request.user.user_id
	User.objects.get(id=id_eliminar).delete()
	return render(request, 'eliminar.html', {'id': user_id})

def modificar_desocupado(request):
    if request.method == "GET":
        return get_modificar_desocupado_form(request)
    elif request.method == 'POST':
        return handle_modificar_desocupado_form(request)

def modificar_empresa(request):
    if request.method == "GET":
        return get_modificar_empresa_form(request)
    elif request.method == 'POST':
        return handle_modificar_empresa_form(request)

def handle_modificar_desocupado(request):
    form = ModificarDesocupado(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'modificar_desocupado.html', {'form': form})

def handle_modificar_empresa(request):
    form = ModificarEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'modificar_Empresa.html', {'form': form})






