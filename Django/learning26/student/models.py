from django.db import models

# Create your models here.
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=50)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"
    def __str__(self):
        return self.studentName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    productDescription = models.TextField(null=True)

    class Meta:
        db_table = "product"
    def __str__(self):
        return self.productName


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseDuration = models.CharField(max_length=50) #e.g., 3 month
    courseFee = models.IntegerField()
    courseMode = models.CharField(max_length=20,choices=[("online","Online"),("ofline","Ofline")])
    courseActive = models.BooleanField(default=True)


    class Meta:
        db_table = "Course"
    def __str__(self):
        return self.courseName


class StudentProfile(models.Model):
    hobbies = (("reading","reading"),("travelling","travelling"),("dancing","dancing"))
    studentID = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=400,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGeender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table = "StudentProfile"
    def __str__(self):
        return self.studentID.studentName
    

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"
    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName
    

 #ONE TO ONE EXAMPLE   
class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField()

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.customerName


class CustomerProfile(models.Model):
    customerId = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=15)

    class Meta:
        db_table = "customer profile"

    def __str__(self):
        return self.customerId.customerName
    
    #ONE TO MANY EXAMPLE
class BookCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "book_category"

    def __str__(self):
        return self.categoryName


class Book(models.Model):
    bookName = models.CharField(max_length=100)
    bookPrice = models.IntegerField()
    categoryId = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.bookName
    
#MANY TO MANY EXAMPLE
class Actor(models.Model):
    actorName = models.CharField(max_length=100)

    class Meta:
        db_table = "actor"

    def __str__(self):
        return self.actorName


class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    releaseYear = models.IntegerField()

    actors = models.ManyToManyField(Actor)

    class Meta:
        db_table = "movie"

    def __str__(self):
        return self.movieName


