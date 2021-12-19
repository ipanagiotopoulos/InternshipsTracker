# Generated by Django 3.2.9 on 2021-12-18 23:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=40)),
                ('street_name', models.CharField(max_length=100)),
                ('street_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('postal_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1000)),
                ('full_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThesisApp.address')),
            ],
        ),
        migrations.CreateModel(
            name='UndergraduateStudent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('title', models.CharField(max_length=120)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('birth_day', models.DateField()),
                ('msisdn', models.IntegerField()),
                ('tel_no2', models.IntegerField()),
                ('register_number', models.CharField(max_length=10)),
                ('register_date', models.DateField()),
                ('department', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics')], max_length=3)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThesisApp.address')),
            ],
            options={
                'verbose_name': 'Undergraduate Student',
                'verbose_name_plural': 'Undergraduate Students',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('title', models.CharField(max_length=120)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('birth_day', models.DateField()),
                ('msisdn', models.IntegerField()),
                ('tel_no2', models.IntegerField()),
                ('register_number', models.CharField(max_length=10)),
                ('register_date', models.DateField()),
                ('department', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics')], max_length=3)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThesisApp.address')),
            ],
            options={
                'verbose_name': 'Supervisor',
                'verbose_name_plural': 'Supervisors',
            },
        ),
        migrations.CreateModel(
            name='CarrierNode',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('title', models.CharField(max_length=120)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('birth_day', models.DateField()),
                ('msisdn', models.IntegerField()),
                ('tel_no2', models.IntegerField()),
                ('department', models.CharField(max_length=150)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThesisApp.address')),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThesisApp.carrier')),
            ],
            options={
                'verbose_name': 'Carrier Node',
                'verbose_name_plural': 'Carrier Nodes',
            },
        ),
    ]
