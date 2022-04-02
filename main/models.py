from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    prise = models.FloatField()
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
