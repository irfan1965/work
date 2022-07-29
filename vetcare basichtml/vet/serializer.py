from rest_framework import serializers
from .models import  *


class Admin(serializers.ModelSerializer):

    class Meta:
        model = Admin1
        fields = ['Admin', 'Admin_Name', 'Psw']


class Farmer(serializers.ModelSerializer):
    class Meta:
        model=Farmer1
        fields=['Farmer_id','Farmer_Name','Farmer_Psw','Farmer_Email','Farmer_Status','Farmer_loc','Id']

class Doctor(serializers.ModelSerializer):

    class Meta :
        model=Doctor1
        fields=['Doctor_ID', 'doctor_Image','Doctor_Name', 'Doctor_Loc', 'Doctor_Designation', 'Doctor_image','Doctor_Slot','Dcotor_Status','Doctor_Exp','Admin_Id','Doctor_Psw']

class Details(serializers.ModelSerializer):
    class Meta:
        model=Details1
        fields=['Payment_Id',"Details_Prescription","Details_Amount","Details_Amount","Details_Doctor","Details_Farmer","Details_Animal"]
class Animal(serializers.ModelSerializer):
    class Meta:
        model=Animal1
        fileds=['Animal_id',"Animal_Name","Animal_Image","Animal_Age","Animal_Symptoms","Animal_Amount","Animal_Loc",'Farmer_ID',"Doctor_ID"]