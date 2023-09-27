# Generated by Django 4.2.5 on 2023-09-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_contributor_author_remove_book_contributors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_names',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='last_names',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(default=None),
        ),
    ]
