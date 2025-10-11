from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """View to list all books - requires can_view permission."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """View to create a book - requires can_create permission."""
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """View to edit a book - requires can_edit permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """View to delete a book - requires can_delete permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_list.html', {'book': book})