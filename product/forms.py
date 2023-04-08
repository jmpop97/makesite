from django import forms
from .models import Products

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['description','prise','amount',]
        labels = {'description':'설명',
                  'prise':'가격',
                  'amount':'수량',}
