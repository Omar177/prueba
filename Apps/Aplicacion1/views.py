from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .forms import inventarioForm,empleadoForm,ventaForm,detallefacturaForm
from .models import inventario,empleado,venta,detallefactura
from django.urls import reverse_lazy
from django.http import JsonResponse


# Create your views here.
class IndexView(TemplateView):
		template_name='index.html'

class NuevaFacturaView(TemplateView):
		template_name='factura.html'


class prueba1View(TemplateView):
		template_name='prueba1.html'


class creditosView(TemplateView):
		template_name='creditos.html'

class crearinventarioView(CreateView):
		template_name = 'crearinventario.html'
		model = inventario
		form_class = inventarioForm
		success_url = reverse_lazy ('app1:listadoinventario')

class crearempleadoView(CreateView):
		template_name = 'crearempleado.html'
		model = empleado
		form_class = empleadoForm
		success_url = reverse_lazy ('app1:listadoempleado')

class crearventaView(CreateView):
		template_name = 'crearventa.html'
		model = venta
		form_class = ventaForm
		success_url = reverse_lazy ('app1:detalleventa')

class creardetalleView(CreateView):
		template_name = 'creardetallefactura.html'
		model = detallefactura
		form_class = detallefacturaForm
		success_url = reverse_lazy ('app1:listadodetallefactura')

class listainventarioView(ListView):
	template_name = 'listadoinventario.html'
	model = inventario
get_queryset= inventario.objects.filter(estado=True)

class listaempleadoView(ListView):
	template_name = 'listadoempleado.html'
	model = empleado
	def get_queryset(self):
		return empleado.objects.all()

class listadetallefacturaView(ListView):
	template_name = 'listadodetallefactura.html'
	model = detallefactura
	def get_queryset(self):
		return detallefactura.objects.all()

class inventarioeditar(UpdateView):
	model = inventario
	form_class = inventarioForm
	template_name ='crearinventario.html'
	success_url = reverse_lazy ('app1:listadoinventario')


class empleadoeditar(UpdateView):
	model = empleado
	form_class = empleadoForm
	template_name ='crearempleado.html'
	success_url = reverse_lazy ('app1:listadoempleado')


class eliminar_inventario(DeleteView):
	model = inventario
	form_class = inventarioForm
	template_name ='inventario_confirm_delete.html'
	success_url = reverse_lazy ('app1:listadoinventario')
	

class eliminar_empleado(DeleteView):
	model = empleado
	form_class = empleadoForm
	template_name ='inventario_confirm_delete.html'
	success_url = reverse_lazy ('app1:listadoempleado')
	

#def editarinventarioView(request, codigo_inventario):
	#inventarios = inventario.objects.get(codigo_inventario=codigo_inventario)
	#if request.method =='GET':
		#form = inventarioForm(instance = inventarios)
	#else: 
		#form = inventarioForm(request.POST, instance = inventarios)
		#if form.is_valid():
		#	form.save()
		#	return redirect('app1:listadoinventario')
		#	return render (request, 'app1/crearinventario.html', {'form':form})

def precio_detalleV (request):
	codigo = request.GET['codigo']
	data = {
	'existencia': inventario.objects.only('precio_inventario').get(codigo_inventario=codigo).precio_inventario
	}

	return JsonResponse(data)

	#if request.method == 'POST':
	#	precio_b = request.POST['idproducto']
	#else :
	#	precio_b = ''

	#inventarios = inventario.objects.filter(codigo_inventario=precio_b)

	#return render_to_response('ajax_precio.html',{'inventarios':inventarios})

