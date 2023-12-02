from django import forms
from .models import Publisher, Review, Book, BookImport, ReviewComment
from .utils import genre_tuples


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


class BookRecommendationForm1(forms.ModelForm):
    cover_choices = [(book.id, book.cover_url) for book in Book.objects.all()[22:28]]
    cover_field = forms.ChoiceField(choices=cover_choices)

    class Meta:
        model = Book
        fields = ["cover_field"]


class BookRecommendationForm2(forms.ModelForm):
    genre_choices = genre_tuples()
    genre_choice_field = forms.MultipleChoiceField(choices=genre_choices)

    class Meta:
        model = Book
        fields = ["genre_choice_field"]


class BookRecommendationForm3(forms.Form):
    series_choices = [
        ("FRI", "Friends"),
        ("GOT", "Game of Thrones"),
        ("YSH", "Young Sheldon"),
        ("BRB", "Breaking Bad"),
        ("DES", "Desperate Housewives"),
        ("SAC", "Sex and the City"),
        ("CRO", "The Crown"),
        ("OFF", "The Office"),
        ("BLA", "Black Mirror"),
        ("EMI", "Emily in Paris"),
        ("GIL", "Gilmore Girls"),
        ("HOU", "House MD")
        ]

    series_choice_field = forms.MultipleChoiceField(choices=series_choices)


class BookRecommendationForm4(forms.Form):
    description_choices = [
        ("ADV", "Adventurous"),
        ("FUN", "Fun"),
        ("GEN", "Gentle"),
        ("ROM", "Romantic"),
        ("ENT", "Enthusiastic"),
        ("CUR", "Curious"),
        ("CON", "Constant"),
        ("DEC", "Decisive"),
        ("CAS", "Casual"),
        ("CHI", "Chill"),
        ("DED", "Dedicated"),
        ("AVI", "Avid")
        ]

    description_choice_field = forms.MultipleChoiceField(choices=description_choices)


class BookRecommendationForm5(forms.ModelForm):
    pass