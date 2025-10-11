from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books - requires can_view permission.
    Uses Django ORM to securely fetch data.
    """
    # Secure: Using Django ORM instead of raw SQL
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """
    View to create a book - requires can_create permission.
    Uses ExampleForm for secure input validation and CSRF protection.
    """
    if request.method == 'POST':
        # Secure: Using Django forms for validation and sanitization
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    View to edit a book - requires can_edit permission.
    Uses get_object_or_404 to prevent information disclosure.
    """
    # Secure: Using get_object_or_404 instead of raw queries
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # Secure: Using Django forms for validation
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm(instance=book)
    
    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    View to delete a book - requires can_delete permission.
    Requires POST request to prevent CSRF attacks.
    """
    # Secure: Using get_object_or_404
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'bookshelf/book_list.html', {'book': book})