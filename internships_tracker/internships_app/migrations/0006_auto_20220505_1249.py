# Generated by Django 3.2.9 on 2022-05-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships_app', '0005_auto_20220504_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='department_1',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='department_2',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='department_3',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='department_4',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('NON', 'Νone')], max_length=3),
        ),
    ]
