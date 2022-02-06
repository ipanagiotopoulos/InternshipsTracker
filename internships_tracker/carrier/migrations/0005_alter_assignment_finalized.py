# Generated by Django 3.2.9 on 2022-01-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0004_alter_assignment_finalized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='finalized',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]