**Creat a Book instance**
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.objects.create
book.save()

Expected output: Book instance created successfully

**Retrieve the book created**
from bookshelf.models import Book:

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected output: 1984 George Orwell 1949

**Update the title of the created book**
from bookshelf.models import Book:

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Expected output: Nineteen Eighty-Four

**Delete the book instance**
from bookshelf.models import Book 

book = Book.objects.get(title="Nineteen Eighty-Four") 
book.delete() 
print(Book.objects.all())

Expected output: []
