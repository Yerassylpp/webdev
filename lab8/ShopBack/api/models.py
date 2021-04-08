from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    description = models.TextField(null = False, max_length= 1000)
    count = models.IntegerField(default = 0)
    is_active = models.BooleanField()
    # category = models.ForeignKey('Category', models.CASCADE)
    def __str__(self):
        return self.name
    def json(self):
        return {
            'id': self.id,
            'name': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
            # 'category':Category
        }

class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    def json(self):
        return{ 
            'id':self.id,
            'name':self.name
        }