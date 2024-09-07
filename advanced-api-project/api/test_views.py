import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book
from .seriealizers import BookSerializer
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('testuser', 'testuser@gmail.com', 'password')
        self.client.login(username='testuser', password='password')
        self.book1 = Book.objects.create(title='Book1', author='Author1', publication_year=2020)
        self.book2 = Book.objects.create(title='Book2', author='Author2', publication_year=2021)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        book = Book.objects.get(pk=self.book1.pk)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_invalid_book(self):
        data = {'title': '', 'author': '', 'publication_year': ''}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_book(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2023}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'Updated Book')

    def test_update_invalid_book(self):
        data = {'title': '', 'author': '', 'publication_year': ''}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_invalid_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'title': 'Book1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(reverse('book-list'), {'author': 'Author1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(reverse('book-list'), {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'search': 'Book1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        response = self.client.get(reverse('book-list'), {'search': 'Author1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_required(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_success(self):
        self.client.force_authenticate(user=None)
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post(reverse('rest_framework:login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_failure(self):
        self.client.force_authenticate(user=None)
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('rest_framework:login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    