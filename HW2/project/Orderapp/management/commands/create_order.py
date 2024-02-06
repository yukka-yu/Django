from django.core.management.base import BaseCommand
from Orderapp.models import OrderModel, ProductModel, ClientModel

class Command(BaseCommand):
    help = "Create order."

    

    def handle(self, *args, **kwargs):
        tom = ClientModel.objects.get(name="Tom")

        products = list()
        products.append(ProductModel.objects.get(name='pineapple'))
        products.append(ProductModel.objects.get(name='apple'))

        summa = 0
        for product in products:
            summa += product.amount * product.price

        order = OrderModel(client=tom, summa=summa)
        
        order.save()
        order.products.set(products)
        self.stdout.write(f'{order} added')