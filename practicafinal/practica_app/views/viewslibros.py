from django.shortcuts import render, get_object_or_404, redirect
from models import Biblioteca, Libro
from forms import LibroForm

# Create your views here.

def listar_libros_biblioteca(request, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    libros = biblioteca.libro_set.all()
    return render(request, 'biblioteca/listar_libros_biblioteca.html', {'biblioteca': biblioteca, 'libros': libros})

def buscar_libro_titulo_biblioteca(request, biblioteca_id, titulo):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    libros = biblioteca.libro_set.filter(titulo__icontains=titulo)
    return render(request, 'biblioteca/buscar_libro_titulo_biblioteca.html', {'biblioteca': biblioteca, 'libros': libros, 'titulo': titulo})

def buscar_libro_autor_biblioteca(request, biblioteca_id, autor):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    libros = biblioteca.libro_set.filter(autor__icontains=autor)
    return render(request, 'biblioteca/buscar_libro_autor_biblioteca.html', {'biblioteca': biblioteca, 'libros': libros, 'autor': autor})

def buscar_libro_editorial_biblioteca(request, biblioteca_id, editorial):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    libros = biblioteca.libro_set.filter(editorial__icontains=editorial)
    return render(request, 'biblioteca/buscar_libro_editorial_biblioteca.html', {'biblioteca': biblioteca, 'libros': libros, 'editorial': editorial})

# Otras vistas para buscar libros
def buscar_libro_titulo(request, titulo):
    libros = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, 'biblioteca/buscar_libro_titulo.html', {'libros': libros, 'titulo': titulo})

def buscar_libro_titulo_disponibilidad(request, titulo):
    libros = Libro.objects.filter(titulo__icontains=titulo, num_ejemplares__gt=0)
    return render(request, 'biblioteca/buscar_libro_titulo_disponibilidad.html', {'libros': libros, 'titulo': titulo})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/editar_libro.html', {'form': form, 'libro': libro})

def borrar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'biblioteca/borrar_libro.html', {'libro': libro})