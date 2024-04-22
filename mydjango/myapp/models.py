from datetime import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'

    def __str__(self):
        return f'Title is {self.title}'
