from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

#class  registrousuario(CreateView):

class Registro_usuario(CreateView):
	model = User
	template_name ='crearusuario.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('app2:registrar')



	