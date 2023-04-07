from django.db import models
from user.models import UserModel
# Create your models here.

class Products(models.Model):

    class Meta:
        db_table="products"

    username = models.CharField(max_length=30, unique=True)