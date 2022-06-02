# Generated by Django 3.2.9 on 2022-03-23 14:25

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('uni_department', models.CharField(max_length=200, verbose_name='uni_department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('city', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('street_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('street_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('postal_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('expiration', models.DateTimeField(verbose_name='expiration date')),
                ('externalMail', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('type', models.CharField(default='activation', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('department_1', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('department_2', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('department_3', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('department_4', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('full_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='UndergraduateStudent',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internships_app.user')),
                ('father_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('mother_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('birth_day', models.DateField()),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('register_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('department', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.address')),
            ],
            options={
                'verbose_name': 'Undergraduate Student',
                'verbose_name_plural': 'Undergraduate Students',
            },
            bases=('internships_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internships_app.user')),
                ('father_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('mother_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('birth_day', models.DateField()),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('register_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('department', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.address')),
            ],
            options={
                'verbose_name': 'Supervisor',
                'verbose_name_plural': 'Supervisors',
            },
            bases=('internships_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Secratarian',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internships_app.user')),
                ('father_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('mother_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('birth_day', models.DateField()),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('department', models.CharField(choices=[('IT', 'Informatics and Telematics'), ('G', 'Geogrpaphy'), ('ESD', 'Economics & Sustainable Development'), ('ND', 'Nutrition and  Dietetics'), ('ALL', 'Secreatary'), ('NON', 'Νone')], max_length=3)),
                ('alias_identifier', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.address')),
            ],
            options={
                'verbose_name': 'Secretarian',
                'verbose_name_plural': 'Secretarians',
            },
            bases=('internships_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CarrierNode',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='internships_app.user')),
                ('father_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('mother_name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')])),
                ('birth_day', models.DateField()),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('department', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships_app.address')),
                ('carrier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internships_app.carrier')),
            ],
            options={
                'verbose_name': 'Carrier Node',
                'verbose_name_plural': 'Carrier Nodes',
            },
            bases=('internships_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]