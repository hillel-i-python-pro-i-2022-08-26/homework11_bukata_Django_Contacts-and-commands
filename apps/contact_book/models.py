import uuid

from django.db import models


# from django.urls import reverse

# we rely on the base class and describe the structure

# function creation for download the files
# here we put our object and the name of the file ( which will be download) , and as response will be our path to the file
def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact_book(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(
        # here we can add name for admin with syntax of internationalisations: "Avatar" for ex
        # length of the path to file
        max_length=265,
        # default value empty like not all will have there avatar
        blank=True,
        null=True,
        # path where all should be downloaded via function( generated on id of syshnost)
        upload_to=get_icon_path,
    )
    #   def get_absolute_url(self):
    #      return reverse("contact_book:edit", kwargs={"pk": self.pk})
    def __str__(self) -> str:
        return f"{self.name} - {self.phone} - {self.birthday}"

    __repr__ = __str__
