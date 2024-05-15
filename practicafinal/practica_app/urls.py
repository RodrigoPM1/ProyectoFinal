from django.urls import path
from . import views

urlpatterns = [
    path('listar_bibliotecas/', views.listar_bibliotecas, name='listar_bibliotecas'),
    path('buscar_biblioteca_nombre/<str:nombre>/', views.buscar_biblioteca_nombre, name='buscar_biblioteca_nombre'),
    path('buscar_biblioteca_ciudad/<str:ciudad>/', views.buscar_biblioteca_ciudad, name='buscar_biblioteca_ciudad'),
    path('listar_libros_biblioteca/<int:biblioteca_id>/', views.listar_libros_biblioteca, name='listar_libros_biblioteca'),
    path('buscar_libro_titulo_biblioteca/<int:biblioteca_id>/<str:titulo>/', views.buscar_libro_titulo_biblioteca, name='buscar_libro_titulo_biblioteca'),
    path('buscar_libro_autor_biblioteca/<int:biblioteca_id>/<str:autor>/', views.buscar_libro_autor_biblioteca, name='buscar_libro_autor_biblioteca'),
    path('buscar_libro_editorial_biblioteca/<int:biblioteca_id>/<str:editorial>/', views.buscar_libro_editorial_biblioteca, name='buscar_libro_editorial_biblioteca'),
    path('buscar_libro_titulo/<str:titulo>/', views.buscar_libro_titulo, name='buscar_libro_titulo'),
    path('buscar_libro_titulo_disponibilidad/<str:titulo>/', views.buscar_libro_titulo_disponibilidad, name='buscar_libro_titulo_disponibilidad'),
    path('agregar_biblioteca/', views.agregar_biblioteca, name='agregar_biblioteca'),
    path('editar_biblioteca/<int:biblioteca_id>/', views.editar_biblioteca, name='editar_biblioteca'),
    path('borrar_biblioteca/<int:biblioteca_id>/', views.borrar_biblioteca, name='borrar_biblioteca'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('borrar_libro/<int:libro_id>/', views.borrar_libro, name='borrar_libro'),
]
