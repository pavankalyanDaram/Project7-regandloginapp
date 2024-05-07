from django.db import models

# Create your models here.
class Reg(models.Model):
    fname = models.CharField(max_length =30)
    lname = models.CharField(max_length =30)
    email = models.EmailField()
    mobile = models.CharField(max_length =15)
    dob = models.CharField(max_length =20)
    username = models.CharField(max_length =30, primary_key=True)
    password = models.CharField(max_length =30)
    cpassword = models.CharField(max_length =30)
