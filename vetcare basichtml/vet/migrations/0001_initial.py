# Generated by Django 2.2.12 on 2022-05-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin1',
            fields=[
                ('Admin', models.AutoField(primary_key=True, serialize=False)),
                ('Admin_Name', models.CharField(max_length=20)),
                ('Psw', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animal1',
            fields=[
                ('Animal_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Animal_Name', models.CharField(max_length=20)),
                ('Animal_Image', models.ImageField(upload_to='static/')),
                ('Animal_Age', models.CharField(max_length=3)),
                ('Animal_Symptom', models.CharField(max_length=50)),
                ('Animal_Amount', models.IntegerField()),
                ('Animal_Loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer1',
            fields=[
                ('Farmer_id', models.AutoField(primary_key=True, serialize=False)),
                ('Farmer_Name', models.CharField(max_length=20, unique=True)),
                ('Farmer_Psw', models.CharField(max_length=20)),
                ('Farmer_Email', models.CharField(max_length=30, null=True)),
                ('Farmer_Status', models.BooleanField(default=True)),
                ('Farmer_loc', models.CharField(max_length=100, null=True)),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Admin1')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor1',
            fields=[
                ('Doctor_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Doctor_Name', models.CharField(max_length=20)),
                ('Doctor_Desgination', models.CharField(max_length=30)),
                ('Doctor_Exp', models.CharField(max_length=50)),
                ('Doctor_Loc', models.CharField(max_length=30)),
                ('Doctor_Slot', models.TimeField(max_length=20)),
                ('Doctor_Image', models.ImageField(upload_to='static/')),
                ('Doctor_Status', models.BooleanField(default=True)),
                ('Doctor_Psw', models.CharField(max_length=20)),
                ('Admin_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Admin1')),
            ],
        ),
        migrations.CreateModel(
            name='Details1',
            fields=[
                ('Payment_Id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Details_Status', models.CharField(max_length=100)),
                ('Details_Amount', models.IntegerField(null=True)),
                ('Details_Prescription', models.CharField(max_length=200)),
                ('Details_Animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Animal1')),
                ('Details_Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Doctor1')),
                ('Details_Farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Farmer1')),
            ],
        ),
        migrations.AddField(
            model_name='animal1',
            name='Doctor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Doctor1'),
        ),
        migrations.AddField(
            model_name='animal1',
            name='Farmer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.Farmer1'),
        ),
    ]