# Generated by Django 3.2.9 on 2022-01-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InternshipsApp', '0002_auto_20220125_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='department',
            field=models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics')], default=None, max_length=3),
            preserve_default=False,
        ),
    ]