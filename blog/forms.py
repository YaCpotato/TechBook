from django import forms

from .models import Book,Review

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author','title', 'link','image')

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('author','title', 'content','star')
