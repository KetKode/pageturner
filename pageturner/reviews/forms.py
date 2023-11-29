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
    type_choices = [
        ("CLAS", "Classics"),
        ("CONT", "Contemporary")
        ]
    choice_type = forms.ChoiceField(choices=type_choices)


class BookRecommendationsForm2(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        genre_choices = genre_tuples(request)

        self.fields['genre_choice'] = forms.MultipleChoiceField(choices=genre_choices)


class BookRecommendationsForm3(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        authors_choices = author_tuples(request)

        self.fields['author_choice'] = forms.MultipleChoiceField(choices=authors_choices)


class BookRecommendationsForm4(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        genre_choices = genre_tuples(request)

        self.fields['no_genre_choice'] = forms.MultipleChoiceField(choices=genre_choices)


class BookRecommendationsForm5(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        authors_choices = author_tuples(request)

        self.fields['no_author_choice'] = forms.MultipleChoiceField(choices=authors_choices)


class BookRecommendationsForm6(forms.ModelForm):
    rating = forms.CharField(widget=forms.HiddenInput())