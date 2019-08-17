from django.db import models

# Create your models here.
class Registration(models.Model):
    FirstName =  models.CharField(max_length=100, blank=True,null=True)
    LastName  =  models.CharField(max_length=200,blank=True,null=True)
    Username  =  models.CharField(max_length=100)
    Contact   =  models.CharField(max_length=20, blank=True,null=True)
    Age       =  models.IntegerField(default=0, blank=True,null=True)
    Joining_date=models.DateTimeField(auto_now=True)
    CompanyName= models.CharField(max_length=200,blank=True,null=True)
    Position   = models.CharField(max_length=100, blank=True,null=True)
    Salary    =  models.CharField(max_length=20,blank=True,null=True)
    Address   =  models.CharField(max_length=200,blank=True,null=True)
    City      =  models.CharField(max_length=20,blank=True,null=True)
    State     =  models.CharField(max_length=20,blank=True,null=True)
    Pincode   =  models.CharField(max_length=20,blank=True,null=True)
    Email     =  models.EmailField(max_length=150)
    Password1 =  models.CharField(max_length=50)
    Password2 =  models.CharField(max_length=50)

    class Meta:
        db_table='registration'