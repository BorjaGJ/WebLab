from django.contrib import admin
from evaluables import models

admin.site.register(models.Proveedor)
admin.site.register(models.Cliente)
admin.site.register(models.Trabajador)
admin.site.register(models.Pedido)
admin.site.register(models.Analisis)
admin.site.register(models.Documento)


