from django.db import models

# Create your models here.

class member(models.Model):
  users = models.CharField(max_length=50)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  username = models.CharField(max_length=250)
  email = models.EmailField()
  picture=models.ImageField(null= True,blank=True,upload_to="images/")
  phonenumber=models.CharField(max_length=10)
  password=models.CharField(max_length=50)
  confirmpassword=models.CharField(max_length=50)
  address=models.CharField(max_length=550)
  
  
  
