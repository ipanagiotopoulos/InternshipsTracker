# Generated by Django 3.2.9 on 2022-03-29 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_auto_20220328_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]