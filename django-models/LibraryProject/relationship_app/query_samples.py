from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# # Example usage:
# if __name__ == "__main__":
#     # Replace the strings with actual names in your database
#     author_name = "George Orwell"
#     library_name = "Central Library"

#     # Query 1: Get all books by a specific author
#     books_by_author = get_books_by_author(author_name)
#     print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

#     # Query 2: List all books in a specific library
#     books_in_library = get_books_in_library(library_name)
#     print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

#     # Query 3: Retrieve the librarian for a specific library
#     librarian = get_librarian_for_library(library_name)
#     if librarian:
#         print(f"Librarian of {library_name}: {librarian.name}")
#     else:
#         print(f"No librarian found for {library_name}")
