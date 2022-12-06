from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import ContactForm
from .models import Contact_book


class ArticleListView(ListView):
    model = Contact_book


def edit_contact(request: HttpRequest, pk) -> HttpResponse:
    obj = get_object_or_404(Contact_book, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
    form = ContactForm(instance=obj)
    context = {"form": form}
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
