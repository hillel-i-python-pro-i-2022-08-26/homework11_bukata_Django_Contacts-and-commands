# Generated by Django 4.1.3 on 2022-12-02 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0002_rename_user_customuser"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CustomUser",
            new_name="User",
        ),
    ]
