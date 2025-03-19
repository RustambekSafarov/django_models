from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    owner = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, blank=True)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
