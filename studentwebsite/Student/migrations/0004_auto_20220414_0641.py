# Generated by Django 2.2.12 on 2022-04-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20220414_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile1',
            fields=[
                ('name', models.CharField(blank=True, db_column='Name', max_length=25, null=True)),
                ('branch_name', models.CharField(blank=True, db_column='branch_Name', max_length=25, null=True)),
                ('duration', models.CharField(blank=True, db_column='Duration', max_length=255, null=True)),
                ('degree_type', models.CharField(blank=True, db_column='Degree_Type', max_length=25, null=True)),
                ('roll_no', models.CharField(db_column='Roll_No', max_length=25, primary_key=True, serialize=False)),
                ('father_name', models.CharField(blank=True, db_column='Father_name', max_length=25, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(upload_to='media/')),
            ],
            options={
                'db_table': 'Student_Profile1',
                'managed': True,
            },
        ),
        migrations.RenameModel(
            old_name='Student_Marks',
            new_name='Student_Marks1',
        ),
        migrations.RenameModel(
            old_name='Student_Subjects',
            new_name='Student_Subjects1',
        ),
        migrations.DeleteModel(
            name='Student_Profile',
        ),
        migrations.AlterModelTable(
            name='student_marks1',
            table='Student_Marks1',
        ),
        migrations.AlterModelTable(
            name='student_subjects1',
            table='Student_Subjects1',
        ),
    ]
