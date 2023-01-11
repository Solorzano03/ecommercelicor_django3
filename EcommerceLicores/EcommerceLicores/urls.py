"""EcommerceLicores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views as views_core
from Productos import views as views_Productos
from user.views import *
from user.forms import *
from django.contrib.auth import  views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('',views_core.home, name="home"),
    path('Quienes_somos/', views_core.Quienes_somos, name="Quienes_somos"),
    path('categorias/',views_Productos.categorias, name="categorias"),
    path('categorias/cervezas',views_Productos.cervezas,name='cervezas'),
    path('categorias/whisky',views_Productos.whisky,name='whisky'),
    path('categorias/vodka',views_Productos.vodka,name='vodka'),
    path('categorias/champagne',views_Productos.champagne,name='champagne'),
    path('categorias/vinos',views_Productos.vinos,name='vinos'),
    path('categorias/ron',views_Productos.ron,name='ron'),
    path('categorias/tequila',views_Productos.tequila,name='tequila'),
    path('categorias/aguardiente',views_Productos.aguardiente,name='aguardiente'),
    path('categorias/coctel',views_Productos.coctel,name='coctel'),
    path('register/', register.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name = 'user/login.html',authentication_form=loginForm) , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
