import email
from pyexpat import model
from django.db import models


# Create your models here.
class Login(models.Model):
    first_name=models.CharField(max_length=20, null=True)
    last_name=models.CharField(max_length=15,null=True)
    GENDER_CHOICES=(
            ("M", "Male"),
       ("F", "Female"),
   )
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)

class Registration(models.Model):
    firstname=models.CharField(max_length=20,null=True)
    lastName=models.CharField(max_length=20,null=True)
    GENDER_CHOICES=(
            ("M", "Male"),
       ("F", "Female"),
   )
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
   
    nationality=models.CharField(max_length=15,null=True)
    Id_number=models.CharField(max_length=15,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=40,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)

class Clinic(models.Model):
    CLINICS_CHOICES=(
        ("M", "Maweni"),
        ("B", "Babtist"),
        ("U", "Upendo"),
    )
    clinic=models.CharField(max_length=20,choices=CLINICS_CHOICES, null=True)
    

        
    