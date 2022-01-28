# Generated by Django 3.2.9 on 2022-01-28 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrier', '0001_initial'),
        ('internships_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrierconsent',
            name='carrier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internships_app.carrier'),
        ),
        migrations.AddField(
            model_name='carrierassignmentperiod',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.carrier'),
        ),
        migrations.AddField(
            model_name='carrierassesement',
            name='assignement_upon',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carrier.assignment'),
        ),
        migrations.AddField(
            model_name='assignmentperiod',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.carrier'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.assignmentperiod'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.supervisor'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='trainee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internships_app.undergraduatestudent'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='trainee_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrier.traineeposition'),
        ),
        migrations.AddField(
            model_name='applicationperiod',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.carrier'),
        ),
    ]
