# Generated by Django 3.2.9 on 2022-04-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0007_alter_assignment_trainee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrierassesement',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
    ]
