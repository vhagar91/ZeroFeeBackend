# Generated by Django 2.1.2 on 2018-11-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_price_breakfastfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', help_text='listing description', max_length=240),
        ),
    ]
