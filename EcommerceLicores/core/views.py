from django.shortcuts import render, HttpResponse

html_base = """
    "<h1>Locura's Beers</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/categoria/">licores</a></li>
        <li><a href="/about/">acerca de</a></li>
        <li><a href="/Quienes_somos/">QUIENES SOMOS</a></li>
    </ul>
"""

# Create your views here.

def home(request):
    return render(request, "core/home.html")
    

def Quienes_somos (request):
    return render(request, "core/Quienes_somos.html")



