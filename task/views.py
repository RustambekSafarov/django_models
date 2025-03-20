from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Person
from .serializers import ProductSerializer, PersonSerializer

@api_view(['GET'])
def allItem(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    persons = Person.objects.all()
    serializer1 = PersonSerializer(persons, many=True)
    serobject = {"products":serializer.data,"persons":serializer1.data}
    return Response(serobject)

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)