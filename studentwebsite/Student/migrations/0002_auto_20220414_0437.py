# Generated by Django 2.2.12 on 2022-04-14 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_Marks',
            new_name='Student_Marks1',
        ),
        migrations.RenameModel(
            old_name='Student_Profile',
            new_name='Student_Profile1',
        ),
        migrations.RenameModel(
            old_name='Student_Subjects',
            new_name='Student_Subjects1',
        ),
        migrations.AlterModelTable(
            name='student_marks1',
            table='Student_Marks1',
        ),
        migrations.AlterModelTable(
            name='student_profile1',
            table='Student_Profile11',
        ),
        migrations.AlterModelTable(
            name='student_subjects1',
            table='Student_Subjects1',
        ),
    ]
