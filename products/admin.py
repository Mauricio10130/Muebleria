from django.contrib import admin

from .models import Product #Importando el modelo

class ProductAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'price', 'image')
	list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Product, ProductAdmin) #Dándole permisos para que solo el administrador, inserte, elimine u modifique algún producto
