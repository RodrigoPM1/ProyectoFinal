from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from models import Biblioteca
from forms import BibliotecaForm

# Create your views here.

def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'biblioteca/listar_bibliotecas.html', {'bibliotecas': bibliotecas})

def buscar_biblioteca_nombre(request, nombre):
    bibliotecas = Biblioteca.objects.filter(nombre__icontains=nombre)
    return render(request, 'biblioteca/buscar_biblioteca_nombre.html', {'bibliotecas': bibliotecas, 'nombre': nombre})

def buscar_biblioteca_ciudad(request, ciudad):
    bibliotecas = Biblioteca.objects.filter(ciudad__icontains=ciudad)
    return render(request, 'biblioteca/buscar_biblioteca_ciudad.html', {'bibliotecas': bibliotecas, 'ciudad': ciudad})

def agregar_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm()
    return render(request, 'biblioteca/agregar_biblioteca.html', {'form': form})

def editar_biblioteca(request, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'biblioteca/editar_biblioteca.html', {'form': form, 'biblioteca': biblioteca})

def borrar_biblioteca(request, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    if request.method == 'POST':
        biblioteca.delete()
        return redirect('listar_bibliotecas')
    return render(request, 'biblioteca/borrar_biblioteca.html', {'biblioteca': biblioteca})



