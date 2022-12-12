from django.forms import SelectDateWidget

from apps.contact_book.models import Contact_book, CustomUser

# import preinstaled django form for user registration
from django.contrib.auth.forms import UserCreationForm
from django import forms

# import preinstaled django  model for user
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contact_book
        # to show all fields in the form
        # fields = "__all__"

        # to see one spesific field or couple for exmp

        fields = ("name", "phone", "birthday", "avatar")


# create a speasial customise user registration form
# which harited from preinstalled django form and model (upper imported)
class CreateUserForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "avatar")
        # to show all fields in the form

    # fields = "__all__"

    # to see one spesific field or couple for exmp
