from django.core.management.base import BaseCommand
from Authorapp.models import AuthorModel

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        author = AuthorModel(name='John', surname='Steinbeck', email='john@example.com', bio='was born', birthdate='1934-10-08')
        author.save()
        self.stdout.write(f'{author}')