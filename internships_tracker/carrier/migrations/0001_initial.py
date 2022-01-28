# Generated by Django 3.2.9 on 2022-01-28 03:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('finalized', models.CharField(choices=[('A', 'Accepted'), ('D', 'Deleted'), ('FD', 'Finalized and Declined')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('complementary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CarrierAssesement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comments', models.TextField(max_length=1000)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='CarrierAssignmentPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TraineePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1500)),
                ('application_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.applicationperiod')),
                ('carrier_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.carrierassignmentperiod')),
            ],
        ),
        migrations.CreateModel(
            name='CarrierConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('consent', models.BooleanField()),
                ('assignement_upon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carrier.assignment')),
            ],
        ),
    ]