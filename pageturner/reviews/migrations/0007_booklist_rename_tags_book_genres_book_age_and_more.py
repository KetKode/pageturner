# Generated by Django 4.2.5 on 2023-11-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_book_main_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Book List', max_length=50)),
                ('book_titles', models.CharField(help_text='Comma-separated list of book titles in the list', max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='tags',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='book',
            name='age',
            field=models.CharField(blank=True, help_text="Age of book's audience", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='best_books_of_2023',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='book',
            name='format_book',
            field=models.CharField(blank=True, help_text='Format of the book', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, help_text='ISBN', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn13',
            field=models.CharField(blank=True, help_text='ISBN13', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, help_text='Language of the book', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, help_text='Release year of the book', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='amazon_link',
            field=models.URLField(blank=True, help_text='Buy on Amazon', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='audible_link',
            field=models.URLField(blank=True, help_text='Buy on Audible', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, help_text='Number of pages in the book', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, default=0, help_text='The rating of the book', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.CharField(blank=True, help_text='Time to finish the book', max_length=30, null=True),
        ),
    ]
