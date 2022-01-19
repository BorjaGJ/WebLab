from django.contrib import admin

from productos import models

admin.site.register(models.Patron)
admin.site.register(models.Disolvente)
admin.site.register(models.Reactivo)
