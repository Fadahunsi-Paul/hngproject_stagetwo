from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150,blank =False,default='')
    email = models.EmailField(max_length= 100)
    country = models.CharField(max_length=150) 

    def __str__(self):
        return self.name
    