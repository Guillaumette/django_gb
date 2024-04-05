import decimal
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from random import randint
from homeworks_app.models import Client, Product, Order


class Command(BaseCommand):
    CLIENTS_NUM = 99
    PRODUCTS_NUM = 99
    help = "Create order."

    def handle(self, *args, **kwargs):
        client = Client.objects.all()[1]
        days = 0
        for i in range(3):
            days = days * 6
            days += 1
            order = Order(
                client=client,
                order_date=datetime.now() - timedelta(days=days + 1),
            )
            order.save()
            for j in range(randint(0, self.PRODUCTS_NUM) // 5):
                product = Product.objects.order_by('?').first()
                order.products.add(product)
                order.total_price = decimal.Decimal(order.total_price) + product.price
            order.save()
