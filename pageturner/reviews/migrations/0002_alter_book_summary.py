# Generated by Django 4.2.5 on 2023-10-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, help_text='Summary of the book', max_length=5000, null=True),
        ),
    ]
