from django import forms
from .models import inventario,empleado,venta,detallefactura
from django.forms import ModelForm

class inventarioForm(ModelForm):

	class Meta:
		model = inventario

		fields = [
				'codigo_inventario',
				'nombre_inventario',
				'marca_invetario',
				'existencia_inventario',
				'precio_inventario',
		]
		labels = {

				'codigo_inventario': 'Codigo del inventario',
				'nombre_inventario': 'Nombre del producto',
				'marca_invetario': 'Marca del producto',
				'existencia_inventario': 'Existencia del producto',
				'precio_inventario': 'Precio unitario',
		}
		widgets = {

				'codigo_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'nombre_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'marca_invetario': forms.TextInput(attrs={'class':'form-control'}),
				'existencia_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'precio_inventario' : forms.TextInput(attrs={'class':'form-control'}),
		}


class empleadoForm(ModelForm):

	class Meta:
		model = empleado
		fields = [
				'codigo_empleado',
				'nombre_empleado',
				'email_empleado',
				'fecha_empleado',

		]
		labels = {
				'codigo_empleado': 'Codigo del empleado',
				'nombre_empleado': 'Nombre del empleado',
				'email_empleado': 'E-mail',
				'fecha_empleado': 'Fecha de inicio',
		
		}
		widgets = {
				  'codigo_empleado': forms.TextInput(attrs={'class':'form-control'}),
				  'nombre_empleado': forms.TextInput(attrs={'class': 'form-control'}),
				  'email_empleado': forms.TextInput(attrs={'class': 'form-control'}),
				  'fecha_empleado': forms.SelectDateWidget(years=range(2019,2050)),


		}


class ventaForm(ModelForm):

	class Meta:
		model = venta
		fields =[
				'codigo_empleado',
				'codigo_venta',
				'fecha_venta',
				'total_venta',
		]
		labels= {
				'codigo_empleado': 'Codigo del empleado',
				'codigo_venta': 'Codigo de venta',
				'fecha_venta': 'Fecha de venta',
				'total_venta': 'Total de la venta',

		}
		widgets = {
				  'codigo_empleado': forms.Select(attrs={'class':'form-control'}),
				  'codigo_venta': forms.TextInput(attrs={'class': 'form-control'}),
				  'fecha_venta': forms.SelectDateWidget(years=range(2019,2050)),
				  'total_venta': forms.TextInput(attrs={'class': 'form-control'}),
		}
class detallefacturaForm(ModelForm):

	class Meta:
		model = detallefactura
		fields = [
				'codigo_venta',
				'codigo_inventario',
				'cantidad_producto',
				'Precio_unitario',
				'precio_total',
				'fecha_detalle',
		]
		labels ={
				'codigo_venta': 'Empleado',
				'codigo_inventario': 'Codigo de venta',
				'cantidad_producto': 'Cantidad',
				'Precio_unitario': 'Precio del producto',
				'precio_total': 'Total',
				'fecha_detalle': 'Fecha',

		}
		widgets = {
			'codigo_inventario': forms.Select(attrs={'id':'idproducto'}),
			 'fecha_detalle': forms.SelectDateWidget(years=range(2019,2050)),
		}

	def __init__(self, *args, **kwargs):
		super(detallefacturaForm, self).__init__(*args, **kwargs)
		#self.fields['codigo_inventario'].widget.attrs\
        #    .update({
        #        'id': 'codigo'
        #    })
		self.fields['Precio_unitario'].widget.attrs\
            .update({
                'id': 'precio'
            })



