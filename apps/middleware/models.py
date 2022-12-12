from django.conf import settings
from django.db import models


# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    session_key = models.CharField(max_length=300)
    # Slug is basically a short label for something, containing only letters, numbers, underscores or hyphens.
    # They’re generally used in URLs. For example, in a typical blog entry URL:
    path = models.SlugField(max_length=300)
    counter = models.IntegerField()
