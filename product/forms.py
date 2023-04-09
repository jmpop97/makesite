from django import forms
from .models import Products

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','description','prise','amount',]
        labels = {'name':'제품명',
                    'description':'설명',
                  'prise':'가격',
                  'amount':'수량',}
