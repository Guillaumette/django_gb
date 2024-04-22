from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from homeworks_app.models import Clients


class Command(BaseCommand):
    CLIENTS_NUM = 99
    help = "Create client."

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Clients(
                name=f'Клиент#{i}',
                email=f'client{i}@mail.ru',
                phone=f'+7(999)000-00-{i:02}',
                address=f'Неизвестный край, г. Дефолт-Сити, ул. Анонимуса, д.{i}',
                registered_date=datetime.now() - timedelta(days=(self.CLIENTS_NUM - i))
            )
            client.save()
