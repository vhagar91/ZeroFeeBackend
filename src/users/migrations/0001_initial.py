# Generated by Django 2.1.2 on 2018-11-05 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('U', 'unknown'), ('M', 'male'), ('F', 'female')], default='U', help_text='The gender of the user Female or Male.', max_length=1, null=True, verbose_name='gender')),
                ('address', models.CharField(default='', help_text='Users Current Address', max_length=50, null=True)),
                ('city', models.CharField(default='', help_text='Users Current City', max_length=20, null=True)),
                ('country', models.CharField(default='', help_text='Users Current Country', max_length=20, null=True)),
                ('about_me', models.CharField(default='', help_text='Users Extra Info', max_length=30, null=True)),
                ('phone', models.CharField(default='', help_text='Phone number', max_length=50, null=True)),
                ('picture', models.OneToOneField(help_text='User Avatar and Picture', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Picture')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
