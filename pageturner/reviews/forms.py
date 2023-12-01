from django import forms
from .models import Publisher, Review, Book, BookImport, ReviewComment
from .utils import genre_tuples, author_tuples


class BookSearchForm(forms.Form):
    search = forms.CharField(min_length=3, max_length=50, required=False, label="Search")


class BookImportForm(forms.ModelForm):
    class Meta:
        model = BookImport
        fields = ('csv_file',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(required=True,
                               widget=forms.widgets.Textarea(attrs={"placeholder": "Type your review here.",
                                                                     "class": "form-control center-content", }
                                                              ), label="", )
    rating = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Review
        exclude = ("date_created", "date_edited", "book", "written_by")


class ReviewCommentForm(forms.ModelForm):
    body = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(attrs={"placeholder": "Type your comment here.",
                                                                  "class": "form-control", }
                                                           ), label="", )

    class Meta:
        model = ReviewComment
        fields = ["body"]


class BookRecommendationsForm1(forms.ModelForm):
    genre_choices = genre_tuples()
    genre_choice_field = forms.MultipleChoiceField(choices=genre_choices)

    class Meta:
        model = Book
        fields = ['genre_choice_field']


class BookRecommendationsForm2(forms.ModelForm):

    authors_choices = author_tuples()
    author_choice_field = forms.MultipleChoiceField(choices=authors_choices)

    class Meta:
        model = Book
        fields = ['author_choice_field']


class BookRecommendationsForm3(forms.ModelForm):

    genre_choices = genre_tuples()
    no_genre_choice_field = forms.MultipleChoiceField(choices=genre_choices)

    class Meta:
        model = Book
        fields = ['no_genre_choice_field']


class BookRecommendationsForm4(forms.ModelForm):

    authors_choices = author_tuples()
    no_author_choice_field = forms.MultipleChoiceField(choices=authors_choices)

    class Meta:
        model = Book
        fields = ['no_author_choice_field']


class BookRecommendationsForm5(forms.ModelForm):
    rating_choices = [("5", "5"),
                      ("4", "4"),
                      ("3", "3"),
                      ("2", "2"),
                      ("1", "1")
                      ]
    rating_field = forms.ChoiceField(choices=rating_choices)

    class Meta:
        model = Book
        fields = ['rating_field']
