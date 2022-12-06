from django import forms
from django.forms import SelectDateWidget

from apps.contact_book.models import Contact_book, CustomUser


class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contact_book
        # to show all fields in the form
        # fields = "__all__"

        # to see one spesific field or couple for exmp

        fields = ("name", "phone", "birthday", "avatar")


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # to show all fields in the form
        fields = "__all__"

        # to see one spesific field or couple for exmp

    #    fields = ("name", "email", "password", "avatar")
