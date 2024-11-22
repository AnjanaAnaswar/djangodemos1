from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name
    


class Products(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to='products')
    price=models.PositiveIntegerField()
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category_object=models.ForeignKey(Category,on_delete=models.CASCADE)


