# Generated by Django 4.2.5 on 2023-10-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_bookimport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(default=None, help_text='The rating of the book', max_length=50),
        ),
    ]
