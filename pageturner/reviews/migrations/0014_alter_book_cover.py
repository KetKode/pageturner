# Generated by Django 4.2.5 on 2023-10-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_book_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.URLField(blank=True, null=True),
        ),
    ]
