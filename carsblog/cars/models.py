from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    generation = models.CharField(max_length=30)
    year_of_prod = models.DateField()
    displacement = models.IntegerField()
    power = models.IntegerField()
    body_type = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    description = models.TextField()

# Create your models here.
