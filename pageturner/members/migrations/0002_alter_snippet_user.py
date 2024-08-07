# Generated by Django 4.2.5 on 2023-11-01 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snippet",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="snippets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
