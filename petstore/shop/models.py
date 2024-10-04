from django.db import models

# Create your models here.

class Products(models.Model):
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=30)
    prod_type = models.CharField(max_length=30)
    prod_image = models.ImageField(upload_to='image',default='')
    