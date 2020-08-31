from django.db import models
from datetime import timedelta,datetime

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    height = models.IntegerField(default=500)
    width = models.IntegerField(default=500)
    images1 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images2 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images3 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images4 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images5 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images6 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    images7 = models.ImageField(upload_to="Products",height_field='height', width_field='width')
    price = models.IntegerField()
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.product_name

