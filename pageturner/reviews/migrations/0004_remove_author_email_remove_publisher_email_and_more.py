# Generated by Django 4.2.5 on 2023-09-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_first_names_author_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(help_text="The author's first name or names.", max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(help_text="The author's last name or names.", max_length=50),
        ),
    ]
