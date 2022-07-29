from distutils.command.upload import upload
from django.db import models
class Student_Marks1(models.Model):
    ind= models.CharField(db_column='Ind_No', primary_key=True, max_length=25)  # Field name made lowercase.
    roll_no = models.CharField(db_column='Roll_No', max_length=25)  # Field name made lowercase.
    sem_id = models.CharField(db_column='Sem_Id', max_length=10)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pass_fail = models.CharField(db_column='Pass_Fail', max_length=25, blank=True, null=True)  # Field name made lowercase.
    credits = models.CharField(db_column='Credits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cgpa = models.FloatField(blank=True, null=True)
    total_marks = models.FloatField(db_column='total_Marks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Student_Marks1'


class Student_Profile1(models.Model):
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='branch_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    degree_type = models.CharField(db_column='Degree_Type', max_length=25, blank=True, null=True)  # Field name made lowercase.
    roll_no = models.CharField(db_column='Roll_No', primary_key=True, max_length=25)  # Field name made lowercase.
    father_name = models.CharField(db_column='Father_name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=255, blank=True, null=True)
    img=models.ImageField(upload_to="media/", null=False)
    class Meta:
        managed = True
        db_table = 'Student_Profile1'


class Student_Subjects1(models.Model):
    sem_id = models.CharField(db_column='Sem_Id', primary_key=True, max_length=255)  # Field name made lowercase.
    sub_name1 = models.CharField(max_length=20, blank=True, null=True)
    sub_name2 = models.CharField(max_length=20, blank=True, null=True)
    sub_name3 = models.CharField(max_length=20, blank=True, null=True)
    roll_no = models.CharField(db_column='Roll_No', max_length=25) 

    class Meta:
        managed = True
        db_table = 'Student_Subjects1'

