import datetime
from random import choice, randint, uniform

from django.core.management.base import BaseCommand
from homeworks_app.models import Category, Products


class Command(BaseCommand):
    help = "Genrate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Products(
                name=f'продукт номер {i}',
                category=choice(categories),
                descr='Самое продающее описание продукта',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                arrived_date=datetime.datetime.now()
            ))
        Products.objects.bulk_create(products)
