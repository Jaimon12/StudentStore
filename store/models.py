from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True) 
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Information(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [
        ('Enquiry', 'For Enquiry'),
        ('Order', 'Place Order'),
        ('Return', 'Return'),
    ]
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    materials_provide = models.ManyToManyField('Material')
    def __str__(self):
        return self.name
class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name