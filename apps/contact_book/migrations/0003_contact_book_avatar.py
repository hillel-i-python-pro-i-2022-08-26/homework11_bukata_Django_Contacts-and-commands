# Generated by Django 4.1.3 on 2022-11-21 15:27

from django.db import migrations, models

import apps.contact_book.models


class Migration(migrations.Migration):

    dependencies = [
        ("contact_book", "0002_alter_contact_book_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact_book",
            name="avatar",
            field=models.ImageField(
                blank=True,
                max_length=265,
                null=True,
                upload_to=apps.contact_book.models.get_icon_path,
            ),
        ),
    ]
