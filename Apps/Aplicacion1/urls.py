"""primerproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import login
from django.conf.urls import url,include
from .views import * 

#IndexView,crearinventarioView,crearempleadoView,crearventaView,creardetalleView,listainventarioView,listaempleadoView,listadetallefacturaView,precio_detalleV,inventarioeditar

urlpatterns = [
url(r'^$',IndexView.as_view(),name='index'),
url(r'^inventario/$',crearinventarioView.as_view(),name='inventario'),
url(r'^empleado/$',crearempleadoView.as_view(),name='empleado'),
url(r'^venta/$',crearventaView.as_view(),name='venta'),
url(r'^detalleventa/$',creardetalleView.as_view(),name='detalleventa'),
url(r'^listadoinventario/$',listainventarioView.as_view(),name='listadoinventario'),
url(r'^listadoempleado/$',listaempleadoView.as_view(),name='listadoempleado'),
url(r'^listadodetallefactura/$',listadetallefacturaView.as_view(),name='listadodetallefactura'),
url(r'^precio/$',precio_detalleV,name='precio_detalle'),
#url(r'^$',login,{'base':'index.html'}, name='login'),
#path('login', LoginView.as_view(template_name='registration/login.html'), name="login"),
#path('login/', LoginView.as_view(template_name='crearempleado.html'), name="login"),
#url(r'^editar/<int:codig>$',editarinventarioView, name= 'editarinventario')
path('editar_inventario/<pk>',(inventarioeditar.as_view()),name='editar_inventario'),
path('editar_empleado/<pk>',(empleadoeditar.as_view()),name='editar_empleado'),
path('eliminar_inv/<pk>/',(eliminar_inventario.as_view()),name='eliminar_inv'),
path('eliminar_empleado/<pk>/',(eliminar_empleado.as_view()),name='eliminar_empleado'),
#url(r'^editar_inventario/(?P<pk>\d+>)/$', inventarioeditar.as_view(), name='editar_inventario'),
#url(r'^eliminar_inv/(?P<pk>\d+>)/$', eliminar_inventario.as_view(),name='eliminar_inv'),
]
