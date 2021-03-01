from django.contrib import admin
from tienda import models

# Register your models here.


class CategoriaProdAmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(models.CategoriaProd, CategoriaProdAmin)
admin.site.register(models.Producto, ProductoAdmin)
