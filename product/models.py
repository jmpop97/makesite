from django.db import models
from user.models import UserModel
# Create your models here.

class Products(models.Model):

    class Meta:
        db_table="products"

    producter = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.BigAutoField(primary_key=True)
    description = models.TextField()
    prise = models.PositiveBigIntegerField()
    amount= models.PositiveBigIntegerField()
    sizes =(('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),)
    size=models.CharField(choices=sizes, max_length=1)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.code
