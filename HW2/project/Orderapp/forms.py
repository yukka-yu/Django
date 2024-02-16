from django import forms
from .models import ClientModel, ProductModel, OrderModel

class ProductForm(forms.ModelForm):
    class Meta:  
        model = ProductModel
        fields = ['name', 'description', 'price', 'amount', 'image']

        widgets = {
            
                }