from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm,ReviewForm
from .models import Book


def home(request):
    return render(request, 'blog/home.html')

def book_list(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/book_list.html', {'books': books})


def newBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book()
            print(request)
            book.title = request.POST['title']
            book.link = request.POST['link']
            book.image = request.FILES['image']
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'blog/new.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'blog/book_detail.html', {'book': book})

def add_review_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/add_review_to_book.html', {'form': form})
