from django.db import models
class inventario(models.Model):
	codigo_inventario = models.IntegerField(primary_key=True)
	nombre_inventario = models.CharField(max_length=25)
	marca_invetario = models.CharField(max_length=25)
	existencia_inventario = models.IntegerField()
	precio_inventario = models.FloatField()
	estado = models.BooleanField(default=True, verbose_name='estado')

	def __str__(self):
		return '%s %s %s %s %s %s' % (self.codigo_inventario,self.nombre_inventario,self.marca_invetario,self.existencia_inventario,self.precio_inventario,self.estado)


class empleado(models.Model):
	codigo_empleado =models.IntegerField(primary_key =True)
	nombre_empleado =models.CharField(max_length=25)
	email_empleado =models.EmailField(max_length=25)
	fecha_empleado =models.DateField()

	def __str__(self):
		return '%s %s %s %s' % (self.codigo_empleado,self.nombre_empleado,self.email_empleado,self.fecha_empleado)

class venta(models.Model):
	codigo_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)
	codigo_venta = models.AutoField(primary_key = True)
	fecha_venta = models.DateField()
	total_venta = models.FloatField()
	


	def __str__(self):
		return '%s %s %s %s' % (self.codigo_empleado,self.codigo_venta,self.fecha_venta,self.total_venta)

class detallefactura(models.Model):
	codigo_detalle = models.AutoField(primary_key = True)
	codigo_venta = models.ForeignKey(venta, on_delete=models.CASCADE)
	codigo_inventario = models.ForeignKey(inventario, on_delete=models.CASCADE)
	cantidad_producto = models.IntegerField()
	Precio_unitario = models.FloatField()
	precio_total = models.FloatField()
	fecha_detalle = models.DateField()


	def __str__(self):
		return '%s %s %s %s %s %s %s' % (self.codigo_detalle,self.codigo_venta,self.codigo_inventario,self.cantidad_producto,self.Precio_unitario,self.precio_total,self.fecha_detalle)







