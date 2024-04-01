import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page of first homework accessed')
    html = '''<!DOCTYPE html>
<html lang="ru">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hw_01</title>
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
