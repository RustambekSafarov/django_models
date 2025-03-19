from django.contrib import admin

from task.models import Product, Person

# Register your models here.
admin.site.register(Product)
admin.site.register(Person)