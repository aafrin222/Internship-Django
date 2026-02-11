from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date =  models.DateField()
    post = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

    