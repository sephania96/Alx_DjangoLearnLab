**Creat a Book instance**
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

Expected output: Book instance created successfully