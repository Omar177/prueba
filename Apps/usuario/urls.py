from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import url,include
from .views import * 
urlpatterns = [
	
url(r'^registrar/$', Registro_usuario.as_view(),name='registrar'),
 #path('registrar/',(Registro_usuario.as_view()),name='registrar'),
 ]