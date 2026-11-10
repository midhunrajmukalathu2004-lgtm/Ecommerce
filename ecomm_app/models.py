from django.db import models

# Create your models here.
class Tb_user(models.Model):
    full_name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='')
    phone_no = models.CharField(max_length=15, default='')
    password = models.CharField( max_length=100, default='')
    user_role = models.CharField(default='user')

class admin_product(models.Model):
    product_name = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=200,default='')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/',null=True,blank='')
    def __str__(self):
        return self.product_name
    