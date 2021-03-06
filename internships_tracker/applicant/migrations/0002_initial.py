# Generated by Django 3.2.9 on 2022-03-23 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrier', '0001_initial'),
        ('internships_app', '0001_initial'),
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='applicant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internships_app.undergraduatestudent'),
        ),
        migrations.AddField(
            model_name='preference',
            name='trainee_position_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_choice', to='carrier.traineeposition', verbose_name='First Choice'),
        ),
        migrations.AddField(
            model_name='preference',
            name='trainee_position_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_choice', to='carrier.traineeposition', verbose_name='Second Choice'),
        ),
        migrations.AddField(
            model_name='preference',
            name='trainee_position_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_choice', to='carrier.traineeposition', verbose_name='Third Choice'),
        ),
        migrations.AddField(
            model_name='preference',
            name='trainee_position_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_choice', to='carrier.traineeposition', verbose_name='Fourth Choice'),
        ),
        migrations.AddField(
            model_name='preference',
            name='trainee_position_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_choice', to='carrier.traineeposition', verbose_name='Fifth Choice'),
        ),
        migrations.AddField(
            model_name='internshipreport',
            name='assignment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carrier.assignment'),
        ),
    ]
