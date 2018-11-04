# Generated by Django 2.1.2 on 2018-11-04 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accommodates', models.IntegerField(default=0, help_text='How many people cant host the listing')),
                ('bedrooms', models.IntegerField(default=0, help_text='How many rooms the listing have')),
                ('beds', models.IntegerField(default=0, help_text='How many Beds the listing have')),
                ('checkInTime', models.TimeField(help_text='Time for checkIn at the listing', null=True)),
                ('checkOutTime', models.TimeField(help_text='Time for chekOut at the listing', null=True)),
                ('propertyType', models.IntegerField(choices=[(0, 'unknown'), (1, 'Apartment'), (2, 'Home'), (3, 'Villa'), (4, 'Penthouse')], default=0, help_text='Property Type')),
                ('nickname', models.CharField(default='Nickname', help_text='Listing Nickname', max_length=200)),
                ('createAt', models.DateTimeField(auto_now=True, help_text='Date of creation')),
                ('isActive', models.BooleanField(default=False, help_text='Is the listing active or not')),
                ('address', models.OneToOneField(help_text='Listing Address', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
                ('owner', models.OneToOneField(help_text='Owner of the listing', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('picture', models.OneToOneField(help_text='Main listing Picture', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Picture')),
                ('pictures', models.ManyToManyField(help_text='Pictures Gallery', related_name='pictures', to='core.Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(help_text='Base currency', max_length=200)),
                ('basePrice', models.IntegerField(default=0, help_text='Base Price')),
                ('extraPersonFee', models.IntegerField(default=0, help_text='Extra person Fee')),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minNights', models.IntegerField(default=1, help_text='Min Nights Allow')),
                ('maxNights', models.IntegerField(default=45, help_text='Max Nights Allow')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.OneToOneField(help_text='listing prices', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Price'),
        ),
        migrations.AddField(
            model_name='listing',
            name='terms',
            field=models.OneToOneField(help_text='listing min and max stay allowed', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Terms'),
        ),
    ]
