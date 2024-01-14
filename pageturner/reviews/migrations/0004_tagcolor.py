# Generated by Django 4.2.5 on 2023-10-31 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.book')),
            ],
        ),
    ]
