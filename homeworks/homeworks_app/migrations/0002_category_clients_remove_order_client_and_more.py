# Generated by Django 5.0.3 on 2024-04-22 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(max_length=32, verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Почтовый адрес')),
                ('registered_date', models.DateField(verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование продукта')),
                ('descr', models.TextField(verbose_name='Описание продукта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Остаток на складе')),
                ('arrived_date', models.DateField(verbose_name='Дата поставки')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение товара')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homeworks_app.category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Сумма чека')),
                ('order_date', models.DateField(verbose_name='Дата заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworks_app.clients', verbose_name='Клиент')),
                ('products', models.ManyToManyField(to='homeworks_app.products', verbose_name='Товары в заказе')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
