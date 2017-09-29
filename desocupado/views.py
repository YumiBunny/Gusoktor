from django.shortcuts import render
from .forms import DesocupadoForm

def registrar_desocupado(request):
    return render(request, 'registrar_desocupado.html', {})

def post_new(request):
    form = DesocupadoForm()
    return render(request, 'registrar_desocupado.html', {'form': form})

# Create your views here.
