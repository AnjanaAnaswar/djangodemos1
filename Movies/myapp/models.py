from django.db import models

# Create your models here.


class Movies(models.Model):
    name=models.TextField(max_length=50)
    year=models.IntegerField()
    image=models.ImageField(upload_to='images')
    details=models.TextField(max_length=100,null=True)
