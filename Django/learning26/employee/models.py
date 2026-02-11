from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date =  models.DateField()
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        ordering = ["name"] 

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.PositiveIntegerField()
    duration_months = models.PositiveIntegerField()

    class Meta:
        db_table = "course"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    head = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    deadline = models.DateField()

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name


    