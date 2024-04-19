from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.TextField()
    registered_date = models.DateField()

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone: {self.phone}, registered: {self.registered_date}'


class Product(models.Model):
    name = models.CharField(max_length=128)
    descr = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}, added: {self.added_date}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_date = models.DateField()

    def __str__(self):
        result = f'Client: {self.client.name}, total price: {self.total_price}, order date: {self.order_date}'
        result += '\nProducts:'
        counter = 1
        for product in self.products.all().order_by('name'):
            result += f'\n\t{counter}. {product.name}, price: {product.price}'
            counter += 1
        return result
