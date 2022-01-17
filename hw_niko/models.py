from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f'{self.id}'


class Supplier(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f'{self.id}'
