# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Verify deletion
all_books = Book.objects.all()
print(f"Total books remaining: {all_books.count()}")
```

## Output
```
Book deleted successfully
Total books remaining: 0
```
