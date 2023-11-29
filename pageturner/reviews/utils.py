from .models import Book, Author


def genre_selection(request):
    unique_genres = Book.objects.exclude(genres=None).values_list('genres', flat=True).distinct()

    # Remove None values and split tags into individual genres
    genres_list = [genre.strip() for genres in unique_genres if genres for genre in genres.split(',')]

    # Remove duplicates by converting the list to a set and then back to a list
    # unique_genres_list = list(set(genres_list))

    return genres_list


def genre_tuples(request):
    genres_list = genre_selection(request)
    genre_short_list = [genre.upper()[:4] for genre in genres_list]
    combined_list = list(zip(genre_short_list, genres_list))

    return combined_list


def author_tuples(request):
    authors_list = Author.objects.all().distinct()

    author_short_list = [author.upper()[:4] for author in authors_list]

    author_tuples_list = list(zip(author_short_list, authors_list))

    return author_tuples_list
