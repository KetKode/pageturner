# Generated by Django 4.2.5 on 2023-11-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0009_booklist_list_cover"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BookList",
            new_name="BooksList",
        ),
    ]
