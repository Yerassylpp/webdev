from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.name()

    def json(self):
        return {
            'id':self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    salary = models.FloatField()
    company = models.ForeignKey(Company, models.CASCADE, 'vacancies', blank = True)

    def __str__(self):
        return self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }
