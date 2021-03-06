# Generated by Django 2.1.2 on 2018-11-05 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(help_text='Full address', max_length=250, null=True)),
                ('lng', models.FloatField(help_text='Geo Longitude', null=True)),
                ('lat', models.FloatField(help_text='Geo Latitude', null=True)),
                ('street', models.CharField(help_text='Street', max_length=200, null=True)),
                ('city', models.CharField(help_text='City', max_length=200, null=True)),
                ('country', models.CharField(help_text='Country', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accommodates', models.IntegerField(default=0, help_text='How many people cant host the listing')),
                ('bedrooms', models.IntegerField(default=0, help_text='How many rooms the listing have')),
                ('beds', models.IntegerField(default=0, help_text='How many Beds the listing have')),
                ('checkInTime', models.TimeField(help_text='Time for checkIn at the listing', null=True)),
                ('checkOutTime', models.TimeField(help_text='Time for chekOut at the listing', null=True)),
                ('propertyType', models.IntegerField(choices=[(0, 'unknown'), (1, 'Apartment'), (2, 'Home'), (3, 'Villa'), (4, 'Penthouse')], default=0, help_text='Property Type', null=True)),
                ('roomType', models.IntegerField(choices=[(0, 'unknown'), (1, 'Full Property'), (2, 'Room')], default=0, help_text='Room Type Full Property/Room', null=True)),
                ('nickname', models.CharField(default='Nickname', help_text='Listing Nickname', max_length=200)),
                ('createAt', models.DateTimeField(auto_now=True, help_text='Date of creation')),
                ('isActive', models.BooleanField(default=False, help_text='Is the listing active or not')),
                ('address', models.OneToOneField(help_text='Listing Address', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PictureListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=src.core.utils.asset_upload_property)),
                ('normal', models.ImageField(blank=True, null=True, upload_to=src.core.utils.asset_upload_property)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basePrice', models.IntegerField(default=0, help_text='Base Price')),
                ('extraPersonFee', models.IntegerField(default=0, help_text='Extra person Fee')),
                ('currency', models.OneToOneField(help_text='Base currency', on_delete=django.db.models.deletion.CASCADE, to='core.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now=True, help_text='Day of creations', null=True)),
                ('lastUpdatedAt', models.DateField(auto_now=True, help_text='Last updated Day', null=True)),
                ('confirmationCode', models.CharField(help_text='Confirmation Code exp C001', max_length=50, null=True)),
                ('checkIn', models.DateField(help_text='Day of entrance', null=True)),
                ('checkOut', models.DateField(help_text='Day leaving the listing', null=True)),
                ('nightsCount', models.IntegerField(help_text='Amount of nights', null=True)),
                ('daysInAdvance', models.IntegerField(help_text='Days in Advance of the booking', null=True)),
                ('guestsCount', models.IntegerField(help_text='Amount of guest to recieve', null=True)),
                ('status', models.IntegerField(choices=[(0, 'inquiry'), (1, 'declined'), (2, 'expired'), (3, 'canceled'), (4, 'reserved'), (5, 'confirmed'), (6, 'Awaiting for Payment')], default=0, help_text='Status')),
                ('guest', models.OneToOneField(help_text='reference to de client', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.OneToOneField(help_text='listing booked', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
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
            name='picture',
            field=models.OneToOneField(help_text='Main listing Picture', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.PictureListing'),
        ),
        migrations.AddField(
            model_name='listing',
            name='pictures',
            field=models.ManyToManyField(help_text='Pictures Gallery', related_name='pictures', to='listings.PictureListing'),
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
