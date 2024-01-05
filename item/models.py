from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
# Create your models here.
class Item(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    category = models.ForeignKey(Category,related_name = 'items', on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    sizes = models.CharField(max_length = 255)
    price = models.FloatField()
    image = models.ImageField(null = True, blank  = True, upload_to = 'images/')
    description = models.CharField(max_length=255, default='Default Description')


    def __str__(self):  
        return self.name
    