from django.db import models
from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models



#
# class Farmer(models.Model):
#     farmer_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20, unique=True)
#     farmer_psw = models.CharField(max_length=20)
#     farmer_email = models.CharField(max_length=30, null=True)
#     farmer_Status = models.CharField(default=1)
#     farmer_loc = models.CharField(max_length=100, null=True)
#     Id = models.ForeignKey(Admin1, on_delete=models.CASCADE)
#
#     def __str__(self) -> str:
#         return self.farmer_name
#
#
# class Doctor(models.Model):
#     doctor_iD = models.AutoField(primary_key=True)
#     doctor_name = models.CharField(max_length=20)
#     doctor_desgination = models.CharField(max_length=30)
#     email=models.EmailField(nul=False)
#     doctor_exp = models.CharField(max_length=50)
#     doctor_status=models.CharField(default=2)
#     doctor_loc = models.CharField(max_length=30)
#     doctor_slot = models.TimeField(max_length=20)
#     doctor_image = models.ImageField(upload_to="static/")
#     doctor_status = models.BooleanField(default=True)
#     doctor_psw = models.CharField(max_length=20)
#
#     def __str__(self) -> str:
#         return self.doctor_name


class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)

    animal_name = models.CharField(max_length=20, null=True, blank=True)
    animal_image = models.ImageField(upload_to="media/", null=True, blank=True)
    animal_age = models.CharField(max_length=3, null=True, blank=True)
    animal_symptom = models.CharField(max_length=50, null=True, blank=True)
    animal_amount = models.IntegerField()
    animal_loc = models.CharField(max_length=100, null=True, blank=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    doctor_email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.animal_name


class Details(models.Model):
    payment_id = models.CharField(max_length=20, primary_key=True)

    details_status = models.CharField(max_length=100, null=True, blank=True)
    details_amount = models.IntegerField(null=True, blank=True)
    details_prescription = models.CharField(max_length=200, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    doctor_email = models.EmailField(null=True, blank=True)
    animal_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.payment_id
