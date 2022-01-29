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


class Author(models.Model):
    name = models.CharField(max_length=150)
    biography = models.TextField(max_length=100000, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name, self.biography, self.date_of_birth


class Quote(models.Model):
    text_quota = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_quota
