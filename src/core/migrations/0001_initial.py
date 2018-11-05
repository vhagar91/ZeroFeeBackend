# Generated by Django 2.1.2 on 2018-11-05 18:00

from django.db import migrations, models
import src.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Currency Code exp EUR', max_length=5, null=True)),
                ('name', models.CharField(help_text='Currency Name', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=src.core.utils.asset_upload)),
                ('normal', models.ImageField(blank=True, null=True, upload_to=src.core.utils.asset_upload)),
            ],
        ),
    ]
