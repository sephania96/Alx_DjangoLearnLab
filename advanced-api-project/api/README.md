# Advanced API Project

This project provides a RESTful API for managing books using Django REST Framework. The API supports CRUD (Create, Read, Update, Delete) operations for books.

## API Endpoints

The following API endpoints are available:

* **GET /books/**: Retrieves a list of all books.
* **GET /books/<int:pk>/**: Retrieves a single book by ID.
* **POST /books/create/**: Creates a new book.
* **PUT /books/<int:pk>/update/**: Updates an existing book.
* **DELETE /books/<int:pk>/delete/**: Deletes a book.

## Permissions

The API uses Django REST Framework's built-in permission classes to control access to the API endpoints. The following permissions are enforced:

* **IsAuthenticatedOrReadOnly**: Allows read-only access to unauthenticated users, while requiring authentication for write operations (create, update, delete).
* **IsAuthenticated**: Requires authentication for all operations.

## API Views

The API views are implemented using Django REST Framework's generic views. The following views are available:

* **BookListView**: Retrieves a list of all books.
* **BookDetailView**: Retrieves a single book by ID.
* **BookCreateView**: Creates a new book.
* **BookUpdateView**: Updates an existing book.
* **BookDeleteView**: Deletes a book.

## Serializers

The API uses Django REST Framework's serializers to convert data between the API and the database. The following serializer is available:

* **BookSerializer**: Serializes and deserializes book data.

## Models

The API uses Django's models to interact with the database. The following model is available:

* **Book**: Represents a book with attributes such as title, author, and publication date.

## Installation

To install the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/advanced-api-project.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

## Testing

To test the API, use a tool such as Postman or curl to send requests to the API endpoints. You can also use Django's built-in testing framework to write unit tests for the API views.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes.