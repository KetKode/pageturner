from enum import Enum

from api.serializers import BookSerializer, BookCollectionSerializer
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes


class SchemaTags(Enum):
    BOOK = "book"
    AUTHOR = "author"
    USER = "user"
    BOOK_COLLECTION = "book_collection"


BOOK_API_METADATA = {
    "BookList": {"tags": [SchemaTags.BOOK.value], "summary": "Get all books from DB"},
    "BookCreate": {
        "tags": [SchemaTags.BOOK.value],
        "summary": "Create a new book",
        "parameters": [BookSerializer],
    },
    "BookGet": {"tags": [SchemaTags.BOOK.value], "summary": "Get a book by ID"},
    "BookUpdate": {"tags": [SchemaTags.BOOK.value], "summary": "Update a book by ID"},
    "BookDelete": {"tags": [SchemaTags.BOOK.value], "summary": "Delete a book by ID"},
    "GeneralRecommendations": {
        "tags": [SchemaTags.BOOK.value],
        "summary": "Display recommendations for a not logged-in user",
    },
    "PersonalRecommendations": {
        "tags": [SchemaTags.BOOK.value],
        "summary": "Display recommendations for a logged-in user based on their likes",
    },
    "FriendsRecommendations": {
        "tags": [SchemaTags.BOOK.value],
        "summary": "Display recommendations based on user's friends' likes",
    },
    "LuckyBook": {"tags": [SchemaTags.BOOK.value], "summary": "Display a random book"},
    "BookmarkBook": {"tags": [SchemaTags.BOOK.value], "summary": "Bookmark a book"},
    "BookSearch": {"tags": [SchemaTags.BOOK.value], "summary": "Search a book"},
    "SearchBar": {
        "tags": [SchemaTags.BOOK.value],
        "summary": "Search bar: title, author, ISBN",
        "parameters": [
            OpenApiParameter(
                name="title",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Title of the book. Case-insensitive.",
            ),
            OpenApiParameter(
                name="author",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Author of the book. Case-insensitive.",
            ),
            OpenApiParameter(
                name="isbn",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description="ISBN of the book. Needs to be exact.",
            ),
        ],
    },
}

BOOK_COLLECTION_API_METADATA = {
    "BookCollectionList": {
        "tags": [SchemaTags.BOOK_COLLECTION.value],
        "summary": "Get all book collections from DB",
    },
    "BookCollectionCreate": {
        "tags": [SchemaTags.BOOK_COLLECTION.value],
        "summary": "Create a new book collection",
        "parameters": [BookCollectionSerializer],
    },
    "BookCollectionGet": {
        "tags": [SchemaTags.BOOK_COLLECTION.value],
        "summary": "Get a book collection by ID",
    },
    "BookCollectionUpdate": {
        "tags": [SchemaTags.BOOK_COLLECTION.value],
        "summary": "Update a book collection by ID",
    },
    "BookCollectionDelete": {
        "tags": [SchemaTags.BOOK_COLLECTION.value],
        "summary": "Delete a book collection by ID",
    },
}
