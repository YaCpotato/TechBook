from django import forms

from .models import Book,Review

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'link','image')

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content','star')
