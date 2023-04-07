from django.db import models

# Create your models here.

class Product(models.Model):
    code ="a"
    name ="a"
    description ="A"
    price ="A"
    sizes = {'S':'Small',
             'M':'Medium',
             'L':'Large',
             'F':'Free'}
