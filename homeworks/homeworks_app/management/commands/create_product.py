from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from random import randint
from homeworks_app.models import Product


class Command(BaseCommand):
    PRODUCTS_NUM = 99
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(
                name=f'Товар_{i}',
                descr=f'Это товар "{i}"\n Товар прекрасного качества.',
                price=randint(1, 999) + 0.99,
                quantity=randint(1, 999),
                added_date=datetime.now() - timedelta(days=(self.PRODUCTS_NUM - i*3))
            )
            product.save()
