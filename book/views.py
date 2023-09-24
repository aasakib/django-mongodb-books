from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
    if request.method == 'POST':
        upload_form = BookCreate(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('index')
    else:
        upload_form = BookCreate()
    
    return render(request, 'book/upload_form.html', {'upload_form': upload_form})

def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book_form = BookCreate(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('index')
    else:
        book_form = BookCreate(instance=book)
    
    return render(request, 'book/upload_form.html', {'upload_form': book_form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    
    return render(request, 'book/delete_confirm.html', {'book': book})
