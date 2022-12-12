from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

# imported customised for for user registration CreateUserForm
from .forms import ContactForm, CreateUserForm
from .models import Contact_book, CustomUser

# imported preintalled django form for user registration
from django.contrib.auth.forms import UserCreationForm

# import preinstalled flash messages ( like errors or sucsess log in which we use in home.html
from django.contrib import messages


def get_contact_book(request: HttpRequest) -> HttpResponse:
    # here we get all objects , this func could be set
    contact_book = Contact_book.objects.all()
    return render(
        request,
        "contact_book/contact_book_list.html",
        {
            # contacts in general will be refering
            # to generator fuc , but here to contacts in this fun upper (with objects)
            "contact_book": contact_book,
            "title": "Contact_book",
        },
    )


def registrationPage(request: HttpRequest, pk) -> HttpResponse:
    obj = get_object_or_404(CustomUser, pk=pk)
    # imported preinstaled django form
    #    form = CreateUserForm()

    # this block to save created user
    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES, instance=obj)
        #     form = CreateUserForm(request.POST)
        # here we validate the form
        if form.is_valid():
            form.save()
            # add user cleaned data for flash message
            user = form.cleaned_data("username")
            # add flash message for user with our message
            messages.success((request, "Account was created for " + user))
            return redirect("contact_book")
    form = CreateUserForm(instance=obj)
    context = {"form": form}
    return render(request, "home.html", context)


# here we pass our template
# context = {'form':form}
# return render(request, "home.html", context)

#  if request.method == "POST":
#     form = CustomUserForm(request.POST, request.FILES, instance=obj)
#    if form.is_valid():
#       form.save()
# form = CustomUserForm(instance=obj)
#  context = {"form": form}


# after updating it will redirect to detail_View
def detail_view(request: HttpRequest, pk) -> HttpResponse:
    # dictionary for initial data with
    # field names as keys
    context = {"data": Contact_book.objects.get(pk=pk)}
    # add the dictionary during initialization
    return render(request, "update_view.html", context)


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
