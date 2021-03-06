# Generated by Django 3.2.9 on 2022-04-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0005_alter_traineeposition_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationperiod',
            name='department',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='assignmentperiod',
            name='department',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='carrierassignmentperiod',
            name='department',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='internshipreportperiod',
            name='department',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3, unique=True),
        ),
    ]
