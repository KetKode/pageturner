# Generated by Django 4.2.5 on 2023-10-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0029_rename_rating_small_book_rating_remove_book_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, help_text='Number of pages in the book.', null=True),
        ),
    ]
