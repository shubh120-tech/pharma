from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Medicines(models.Model):
    MedicineName = models.CharField(max_length=50)
    describe = models.CharField(max_length=400, default="")
    date= models.DateField()
    category = models.CharField(max_length=40,default="")
    picture = models.ImageField(upload_to="MathuraMed/Images", default="")
    price =models.IntegerField()

    def __str__(self):
        return self.MedicineName



