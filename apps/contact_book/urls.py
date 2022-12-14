from django.urls import path

from . import views

# app name will be use in _header
app_name = "contact_book"
# here we call function as an object, we give name for this path
# path for index view

# name= will be use in _header
urlpatterns = [
    # get_contacts : name of our view
    #    path("", views.get_contact_book, name="contact_book"),
    path("", views.ArticleListView.as_view(), name="contact_book"),
    path("", views.create_contact, name="create_contact"),
    path("<int:pk>/edit", views.edit_contact, name="edit_contact"),
    path("<int:pk>/delete", views.delete_contact, name="delete_contact"),
    path("<int:pk>/read", views.read_contact, name="read_contact"),
    path("create/", views.create_contact, name="create_contact"),
    #   path("<int:pk>", views.ContactUpdateView.as_view(), name="edit"),
]
