from django.db import models


class Clients(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    name = models.CharField(
        max_length=128,
        verbose_name='Имя',
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
    )
    phone = models.CharField(
        max_length=32,
        verbose_name='Телефон',
    )
    address = models.TextField(
        verbose_name='Почтовый адрес',
    )
    registered_date = models.DateField(
        verbose_name='Дата регистрации',
    )

    def __str__(self):
        return f'Client: {self.name}, '\
               'email: {self.email}, '\
               'phone: {self.phone}, '\
               'registered: {self.registered_date}'


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Наименование категории',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Category: {self.name}'


class Products(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(
        max_length=128,
        verbose_name='Наименование продукта',
    )
    descr = models.TextField(
        verbose_name='Описание продукта',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    quantity = models.IntegerField(
        verbose_name='Остаток на складе',
    )
    arrived_date = models.DateField(
        verbose_name='Дата поставки',
    )
    image = models.ImageField(
        null=True,
        verbose_name='Изображение товара',
    )
    category = models.ForeignKey(
        Category,
        default=None,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория товара',
    )

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, '\
               'quantity: {self.quantity}, arrived: {self.arrived_date}'

    @property
    def total_quantity(self):
        return sum(product.quantity for product in Products.objects.all())


class Orders(models.Model):
    client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
    )
    products = models.ManyToManyField(
        Products,
        verbose_name='Товары в заказе',
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Сумма чека',
    )
    order_date = models.DateField(
        verbose_name='Дата заказа',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        result = f'Client: {self.client.name}, '\
                 'total price: {self.total_price}, '\
                 'order date: {self.order_date}'
        result += '\nProducts:'
        counter = 1
        for product in self.products.all().order_by('name'):
            result += f'\n\t{counter}. {product.name}, price: {product.price}'
            counter += 1
        return result
