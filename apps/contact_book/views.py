from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Contact_book


def get_contact_book(request: HttpRequest) -> HttpResponse:
    # here we get all objects , this func could be set
    contact_book = Contact_book.objects.all()
    return render(
        request,
        "contact_book.html",
        {
            # contacts in general will be refering
            # to generator fuc , but here to contacts in this fun upper (with objects)
            "contact_book": contact_book,
            "title": "Contact_book",
        },
    )
