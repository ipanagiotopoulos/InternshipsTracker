# Generated by Django 3.2.9 on 2022-04-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0008_carrierassesement_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrierassesement',
            name='assesment_file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
