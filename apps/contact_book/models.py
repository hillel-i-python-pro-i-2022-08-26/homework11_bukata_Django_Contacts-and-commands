from django.db import models

# we rely on the base class and describe the structure


class Contact_book(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone} - {self.birthday}"

    __repr__ = __str__
