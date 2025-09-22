import django
import os

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author():
    """Query all books by a specific author."""
    try:
        # Get a specific author (assuming author exists)
        author_name = "George Orwell"  # Example author name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using ForeignKey relationship
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
            
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")

def list_books_in_library():
    """List all books in a library."""
    try:
        # Get a specific library (assuming library exists)
        library_name = "Central Library"  # Example library name
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using ManyToMany relationship
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")

def retrieve_librarian_for_library():
    """Retrieve the librarian for a library."""
    try:
        # Get a specific library (assuming library exists)
        library_name = "Central Library"  # Example library name
        library = Library.objects.get(name=library_name)
        
        # Query librarian using OneToOne relationship
        librarian = Librarian.objects.get(library=library)
        
        print(f"Librarian for {library_name}: {librarian.name}")
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

if __name__ == "__main__":
    print("=== Django Relationship Queries ===")
    print()
    
    # Sample queries demonstrating different relationships
    query_books_by_author()
    print()
    list_books_in_library()
    print()
    retrieve_librarian_for_library()
