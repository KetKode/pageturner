# Generated by Django 4.2.5 on 2023-11-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0011_rename_bookslist_bookcollection"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="main_age",
            field=models.CharField(
                blank=True, help_text="Main age of the book", max_length=20, null=True
            ),
        ),
    ]
