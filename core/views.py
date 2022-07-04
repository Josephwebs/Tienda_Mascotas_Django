from urllib.request import Request
from django.shortcuts import render, redirect
from .models import Fundacion, Mascota, Producto
from .forms import FormularioCliente, ProductosForm
import requests
# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def index(request):
    return render(request, 'core/index.html')


def nosotros(request):
    return render(request, 'core/nosotros.html')


def contacto(request):
    return render(request, 'core/contacto.html')


def tienda(request):
    return render(request, 'core/tienda.html')


def Gatos(request):
    return render(request, 'core/Gatos.html')


def Mas(request):
    return render(request, 'core/Mas.html')


def Perros(request):
    return render(request, 'core/Perros.html')


def BeBrave(request):
    fundacion = Fundacion.objects.all

    datos = {
        'fundaciones': fundacion
    }

    return render(request, 'core/adopciones.html', datos)


def form_productos(request):
    datos = {
        'form':  ProductosForm()
    }
    if request.method == 'POST':
        formulario = ProductosForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("listado_productos")
    return render(request, 'core/form_productos.html', datos)


def form_mod_productos(request, id):
    producto = Producto.objects.get(idproducto=id)
    print(producto)
    datos = {
        'form': ProductosForm(instance=producto)
    }
    print("entro a la funcion")
    print(datos)
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST,  instance=producto)
        print(formulario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'
            print("me modifico")

    return render(request, 'core/form_mod_productos.html', datos)


def form_del_productos(request, id):
    producto = Producto.objects.get(idproducto=id)
    producto.delete()
    if request.method == 'DELETE':
        formulario = ProductosForm(data=request.DELETE, instance=producto)

        if formulario.is_valid:
            formulario.save()

    return redirect(to="listado_productos")


def listado_productos(request):
    r = requests.get('http://127.0.0.1:8000/api/lista-productos')

    datos = {
        'productos': r.json()
    }

    return render(request, 'core/listado_productos.html', datos)


def vista_productos(request):
    r = requests.get('http://127.0.0.1:8000/api/lista-productos')

    datos = {
        'productos': r.json()
    }

    return render(request, 'core/tienda.html', datos)


def Adopciones(request):
    r = requests.get('http://127.0.0.1:8000/api/lista-mascotas')

    datos = {
        'mascotas': r.json()
    }

    return render(request, 'core/adopciones.html', datos)


def Form_cliente(request):
    cliente = FormularioCliente(request.POST)

    if cliente.is_valid():
        cliente.save()
        cliente = FormularioCliente()
    return render(request, "contacto.html", {"form": cliente, "mensaje": "ok"})


def Lista_donaciones(request):
    r = requests.get('http://127.0.0.1:8000/api/lista-fundaciones')

    datos = {
        'fundaciones': r.json()
    }

    return render(request, 'core/donaciones.html', datos)
