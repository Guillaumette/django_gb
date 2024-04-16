from random import choices

from django.core.management import BaseCommand
from myapp.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ex ligula, pretium quis justo quis," \
        "tempus hendrerit urna. Maecenas ut vestibulum erat. Proin aliquam nibh ac purus pellentesque dignissim." \
        "Nam id risus eleifend nisl auctor fermentum. Curabitur eros eros, suscipit eget rhoncus nec, tincidunt a neque." \
        "Nulla porta lacus ipsum, sagittis ullamcorper orci tristique quis. Mauris ut ligula gravida," \
        "tempus augue sit amet, ultrices urna. Integer imperdiet urna purus. Lorem ipsum dolor sit amet," \
        "consectetur adipiscing elit. Quisque sapien orci, consectetur eu elit eu, scelerisque scelerisque ex." \
        "Mauris sodales mattis dolor. Nunc lacinia urna nibh, at porttitor mauris elementum at."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of users')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=30)),
                    author=author
                )
                post.save()
