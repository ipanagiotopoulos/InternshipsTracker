# Generated by Django 3.2.9 on 2022-04-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisorassesment',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
    ]
