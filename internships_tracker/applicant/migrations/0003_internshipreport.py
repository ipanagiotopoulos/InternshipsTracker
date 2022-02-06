# Generated by Django 3.2.9 on 2022-01-30 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0007_intershipreportperiod'),
        ('applicant', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_file', models.FileField(upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carrier.assignment')),
            ],
        ),
    ]