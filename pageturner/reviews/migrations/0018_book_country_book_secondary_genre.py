# Generated by Django 4.2.5 on 2024-01-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0017_remove_book_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Country associated with the book",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="secondary_genre",
            field=models.CharField(
                blank=True,
                help_text="Secondary genre of the book",
                max_length=50,
                null=True,
            ),
        ),
    ]
