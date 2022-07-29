from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
# Create your models here.

class Admin1(models.Model):
    Admin=models.AutoField(primary_key=True)
    Admin_Name=models.CharField(max_length=20)
    Psw=models.CharField(max_length=20)
    Status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.Id


class Farmer1(models.Model):
    Farmer_id=models.AutoField(primary_key=True)
    Farmer_Name=models.CharField(max_length=20,unique=True)
    Farmer_Psw=models.CharField(max_length=20)
    Farmer_Email=models.CharField(max_length=30,null=True)
    Farmer_Status=models.BooleanField(default=True)
    Farmer_loc=models.CharField(max_length=100,null=True)
    Id=models.ForeignKey(Admin1,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return  self.Farmer_Name



class Doctor1(models.Model):
    Doctor_ID=models.AutoField(primary_key=True)
    Doctor_Name=models.CharField(max_length=20)
    Doctor_Desgination=models.CharField(max_length=30)
    Doctor_Exp=models.CharField(max_length=50)
    Doctor_Loc=models.CharField(max_length=30)
    Doctor_Slot=models.TimeField(max_length=20)
    Doctor_Image=models.ImageField(upload_to="static/")
    Doctor_Status=models.BooleanField(default=True)
    Admin_Id=models.ForeignKey(Admin1 ,on_delete=models.CASCADE)
    Doctor_Psw=models.CharField(max_length=20)

    def __str__(self)->str :
        return  self.Doctor_Name
    
    
class Animal1(models.Model):
    Animal_Id=models.AutoField(primary_key=True)
    Animal_Name=models.CharField(max_length=20)
    Animal_Image=models.ImageField(upload_to="static/")
    Animal_Age=models.CharField(max_length=3)
    Animal_Symptom=models.CharField(max_length=50)
    Animal_Amount=models.IntegerField()
    Animal_Loc=models.CharField(max_length=100)
    Farmer_ID=models.ForeignKey(Farmer1,on_delete=models.CASCADE)
    Doctor_ID=models.ForeignKey(Doctor1,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return  self.Animal_Name

class Details1(models.Model):
   Payment_Id=models.CharField(max_length=20,primary_key=True)
   Details_Status=models.CharField(max_length=100)
   Details_Amount=models.IntegerField(null=True)
   Details_Amount=models.CharField(max_length=200)
  # Details_Date=models.CharField(max_length=200)
   Details_Doctor=models.ForeignKey(Doctor1,on_delete=models.CASCADE)
   Details_Farmer=models.ForeignKey(Farmer1,on_delete=models.CASCADE)
   Details_Animal=models.ForeignKey(Animal1,on_delete=models.CASCADE)
   
   def __str__(self) -> str:
        return  self.Details_Status
        