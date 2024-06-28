# Generated by Django 4.2.5 on 2023-11-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0005_delete_tagcolor"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="main_genre",
            field=models.CharField(
                blank=True, help_text="Main genre of the book", max_length=20, null=True
            ),
        ),
    ]
