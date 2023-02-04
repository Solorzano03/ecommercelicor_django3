from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Productos.models import product
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.models import User
from .carrito import Carrito


# Create your views here.
@login_required
def carrito(request):
    productos = product.objects.all()
    

    data = {
        'productos' : productos
    }

    return render(request, "carrito/carrito.html", data)


def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = product.objects.get(id=id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = product.objects.get(id=id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = product.objects.get(id=id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")