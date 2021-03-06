# Generated by Django 2.2.12 on 2020-06-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacsfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacsfile',
            name='PatientAge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacsfile',
            name='PatientBirthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacsfile',
            name='PatientSex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='PatientID',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='PatientName',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='SeriesDescription',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='SeriesInstanceUID',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='StudyDescription',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='StudyInstanceUID',
            field=models.CharField(db_index=True, max_length=150),
        ),
    ]
