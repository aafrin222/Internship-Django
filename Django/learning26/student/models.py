from django.db import models

# Create your models here.
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=50)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    productDescription = models.TextField(null=True)

    class Meta:
        db_table = "product"


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseDuration = models.CharField(max_length=50) #e.g., 3 month
    courseFee = models.IntegerField()
    courseMode = models.CharField(max_length=20,choices=[("online","Online"),("ofline","Ofline")])
    courseActive = models.BooleanField(default=True)


    class Meta:
        db_table = "Course"
