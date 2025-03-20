from django.urls import path

from .views import *


urlpatterns = [
    path('all/',allItem, name='all-Items'),
    path('products/', product_list, name='product-list'),
    path('persons/', person_list, name='person-list'),
    path('addperson/', createPerson),
    path('addproduct/', createProduct),
]