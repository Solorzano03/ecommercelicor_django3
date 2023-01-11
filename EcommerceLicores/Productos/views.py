from django.shortcuts import render,HttpResponse
from .models import product
from .models import Category
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


def categorias(request):
    productos=product.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 8)
        productos = paginator.page(page)
    except:
        raise Http404
    data={
        "productos":productos, 
        'paginator': paginator
    }
    return render(request, "core/categorias.html",data)

"""def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 7)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : productos,
        'paginator': paginator
    }

    return render(request, "producto/listar.html", data)"""


def productos(request):
    return render(request, "core/categorias.html")
def cervezas(request):
    cervezas=Category.objects.get(name="cervezas")
    productos=product.objects.filter(categoria=cervezas)
    data={
        "cervezas":productos }
    return render(request, "productos/cervezas.html",data)
def whisky(request):
    whisky=Category.objects.get(name="whisky")
    productos=product.objects.filter(categoria=whisky)
    data={
        "whisky":productos }
    return render(request, "productos/whisky.html",data)

def vodka(request):
    vodka=Category.objects.get(name="vodka")
    productos=product.objects.filter(categoria=vodka)
    data={
        "vodka":productos }
    return render(request, "productos/vodka.html",data)

def champagne(request):
    champagne=Category.objects.get(name="champagne")
    productos=product.objects.filter(categoria=champagne)
    data={
        "champagne":productos }
    return render(request, "productos/champagne.html",data)

def vinos(request):
    vinos=Category.objects.get(name="vinos")
    productos=product.objects.filter(categoria=vinos)
    data={
        "vinos":productos }
    return render(request, "productos/vinos.html",data)    

def ron(request):
    ron=Category.objects.get(name="ron")
    productos=product.objects.filter(categoria=ron)
    data={
        "ron":productos }
    return render(request, "productos/ron.html",data) 

def tequila(request):
    tequila=Category.objects.get(name="tequila")
    productos=product.objects.filter(categoria=tequila)
    data={
        "tequila":productos }
    return render(request, "productos/tequila.html",data) 

def aguardiente(request):
    aguardiente=Category.objects.get(name="aguardiente")
    productos=product.objects.filter(categoria=aguardiente)
    data={
        "aguardiente":productos }
    return render(request, "productos/aguardiente.html",data) 

def coctel(request):
    coctel=Category.objects.get(name="coctel")
    productos=product.objects.filter(categoria=coctel)
    data={
        "coctel":productos }
    return render(request, "productos/coctel.html",data) 