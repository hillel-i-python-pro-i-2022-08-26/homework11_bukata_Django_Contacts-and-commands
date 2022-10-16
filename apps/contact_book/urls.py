from django.urls import path

from . import views

# app name will be use in _header
app_name = "contact_book"
# here we call function as an object, we give name for this path
# path for index view

# name= will be use in _header
urlpatterns = [
    # get_contacts : name of our view
    path("", views.get_contact_book, name="contact_book"),
]
