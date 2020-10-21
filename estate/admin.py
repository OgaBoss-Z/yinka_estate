from django.contrib import admin
from . models import *
# Register your models here.
# Define inline image fields for the admin  
class ImageInline(admin.TabularInline):
   model = PropertyImage
   extra = 3
   
# Register Product and ProductAdmin
class PropertiesAdmin(admin.ModelAdmin):
   list_display = ['name', 'price', 'discount_price', 'is_featured', 'created']
   list_filter = ['name', 'created']
   list_editable = ['discount_price', 'is_featured']
   prepopulated_fields = {'slug': ('name',)}
   inlines = [ImageInline]
admin.site.register(Properties, PropertiesAdmin)

