import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Order


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page of first homework accessed')
    html = '''<!DOCTYPE html>
<html lang="ru">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>homeworks</title>
</head>

<body>
    <div class="header">
        <h1>Главная страница</h1>
    </div>
    <div class="content">
        <p>Это главная страница моего первого Django-проекта</p>
    </div>
    <div class="footer">

    </div>
</body>
    '''
    return HttpResponse(html)


def about(request):
    logger.info('About page of first homework accessed')
    html = '''<!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homework 01</title>
    </head>

    <body>
        <div class="header">
            <h1>Это страница обо мне</h1>
        </div>
        <div class="content">
            <p>Я только начинаю изучать Django :3</p>
        </div>
        <div class="footer">

        </div>
    </body>
    '''
    return HttpResponse(html)


def client_ordered_products(request, client_id):
    client = Client.objects.get(pk=client_id)

    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    orders_last_week = client.order_set.filter(order_date__gte=last_week, order_date__lte=today)
    orders_last_month = client.order_set.filter(order_date__gte=last_month, order_date__lte=today)
    orders_last_year = client.order_set.filter(order_date__gte=last_year, order_date__lte=today)

    products_last_week = get_unique_products(orders_last_week)
    products_last_month = get_unique_products(orders_last_month)
    products_last_year = get_unique_products(orders_last_year)

    return render(request, 'homeworks_app/client_ordered_products.html', {
        'client': client,
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year,
    })


def get_unique_products(orders):
    products = set()
    for order in orders:
        products.update(order.products.all())
    return products
