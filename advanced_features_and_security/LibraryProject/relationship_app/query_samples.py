from django.db.models import Q
from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = 'John Doe'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by John Doe:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = 'New York Public Library'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("\nBooks in New York Public Library:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name='New York Public Library')
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for New York Public Library:")
print(librarian.name)