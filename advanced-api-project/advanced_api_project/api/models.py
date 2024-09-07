from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    """
    Represents an author with a name.
    """

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    """
    Represents a book with a title, publication year, and author.
    """