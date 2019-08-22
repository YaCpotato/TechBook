from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm,ReviewForm
from .models import Book


def home(request):
    return render(request, 'blog/home.html')

def newBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # book.Title = request.Title
            # book.Tink = request.Link
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'blog/new.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'blog/book_detail.html', {'book': book})
