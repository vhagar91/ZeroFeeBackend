from django.contrib import admin
from .models import Listing, Terms, Price,Address,PictureListing
# Register your models here.
admin.site.register(Listing)
admin.site.register(Terms)
admin.site.register(Price)
admin.site.register(Address)
admin.site.register(PictureListing)