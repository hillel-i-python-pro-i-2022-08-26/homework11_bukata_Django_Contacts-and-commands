from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import ContactForm
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


# after updating it will redirect to detail_View
def detail_view(request: HttpRequest, pk) -> HttpResponse:
    # dictionary for initial data with
    # field names as keys
    context = {"data": Contact_book.objects.get(pk=pk)}
    # add the dictionary during initialization
    return render(request, "update_view.html", context)


def edit_contact(request: HttpRequest, pk) -> HttpResponse:
    context = {}
    obj = get_object_or_404(Contact_book, pk=pk)
    form = ContactForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "edit.html", context)


def read_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contact_book.objects.get(pk=pk)
    form = ContactForm(instance=contact)
    return render(
        request,
        "read.html",
        {
            # contacts in general will be refering
            # to generator fuc , but here to forms in this fun upper (with objects)
            "form": form,
            "title": "Read_contact",
        },
    )


def delete_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contact_book.objects.get(pk=pk)
    contact.delete()
    return render(
        request,
        "delete.html",
        {
            # contacts in general will be refering
            # to generator fuc , but here to forms in this fun upper (with objects)
            "title": "Delete_contact",
        },
    )


def create_contact(request: HttpRequest) -> HttpResponse:
    context = {}
    # add the dictionary during initialization
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context["form"] = form
    return render(request, "create.html", context)
