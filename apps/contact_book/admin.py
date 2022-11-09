# modul to make staff (registrations with admin)
from django.contrib import admin

# we import our models)
from . import models

# here ready admin for contact_book
admin.site.register(models.Contact_book)
