from .models import Book, Author
from collections import OrderedDict


def genre_selection():
    # Use distinct to ensure unique values from the database
    unique_genres = Book.objects.exclude(genres=None).values_list('genres', flat=True).distinct()

    # Remove None values, split tags into individual genres, and convert to lowercase
    genres_list = [genre.strip() for genres in unique_genres if genres for genre in genres.split(',')]

    return genres_list


def genre_tuples():
    genres_list = Book.objects.exclude(genres=None).values_list('main_genre', flat=True).distinct()

    # Use an ordered set to maintain the order
    unique_genres = list(OrderedDict.fromkeys(genres_list))

    genre_short_list = [genre.upper()[:4] for genre in unique_genres]
    combined_list = list(zip(genre_short_list, unique_genres))

    return combined_list


def author_tuples():
    authors_list = Author.objects.values_list('name', flat=True).distinct()

    author_short_list = [author.upper()[:4] for author in authors_list]

    author_tuples_list = list(zip(author_short_list, authors_list))

    return author_tuples_list
