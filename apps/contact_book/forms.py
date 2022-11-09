from django import forms
from django.forms import SelectDateWidget

from apps.contact_book.models import Contact_book


class ContactForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contact_book
        # to show all fields in the form
        # fields = "__all__"

        # to see one spesific field or couple for exmp
        fields = ("name", "phone", "birthday")
