# Generated by Django 3.2.9 on 2022-04-23 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0006_auto_20220419_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='trainee_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.traineeposition', unique=True),
        ),
    ]
