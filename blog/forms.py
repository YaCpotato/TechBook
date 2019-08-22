from django import forms

from .models import Book,Review

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('Title', 'Link',)

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('Title', 'Content','Star')
