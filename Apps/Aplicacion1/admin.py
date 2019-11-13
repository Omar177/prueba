from django.contrib import admin

from .models import inventario,empleado,venta,detallefactura


admin.site.register(inventario)
admin.site.register(empleado)
admin.site.register(venta)
admin.site.register(detallefactura)
