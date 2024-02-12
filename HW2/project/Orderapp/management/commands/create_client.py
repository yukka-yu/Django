from django.core.management.base import BaseCommand
from Orderapp.models import ClientModel

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = ClientModel(name='Tom', email='tome@example.com', phone='+1(256)87657', address='LA', reg_date='2020-03-26')
        #client = ClientModel(name='Dave', email='dave@example.com', phone='+1(234)4567', address='NY', reg_date='2018-03-26')
        #client = ClientModel(name='Julia', email='jul@example.com', phone='+1(455668)5477', address='Miami', reg_date='2023-03-26')
        client.save()
        self.stdout.write(f'{client} added')