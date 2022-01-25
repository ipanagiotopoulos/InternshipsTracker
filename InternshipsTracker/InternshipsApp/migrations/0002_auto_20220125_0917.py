# Generated by Django 3.2.9 on 2022-01-25 09:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('InternshipsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carriernode',
            name='msisdn',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='carriernode',
            name='tel_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='msisdn',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='tel_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='undergraduatestudent',
            name='msisdn',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='undergraduatestudent',
            name='tel_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
    ]