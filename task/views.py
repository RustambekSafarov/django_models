from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Person
import json

# Create your views here.
def index(request):
    persons = list(Person.objects.all().values())  # Convert queryset to list
    products = list(Product.objects.all().values())

    person_json = json.dumps(persons)  
    product_json = json.dumps(products)
    # return HttpResponse(f"Person: {json.dumps(person_json)}\nProduct: {json.dumps(product_json)}")
    return render(request, 'home.html', {'person': person_json, 'product': product_json})
