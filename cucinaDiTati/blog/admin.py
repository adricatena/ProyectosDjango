from django.contrib import admin
from blog import models

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Post, PostAdmin)
