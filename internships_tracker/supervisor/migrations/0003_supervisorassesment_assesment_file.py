# Generated by Django 3.2.9 on 2022-04-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0002_supervisorassesment_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisorassesment',
            name='assesment_file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
