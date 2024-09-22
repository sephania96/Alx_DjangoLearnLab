#### User Authentication API
A simple user authentication API built using Django and Django REST Framework.

### Features
- User registration with username and password
- User login with username and password
- Token-based authentication for API requests

### Endpoints
## Register
- POST /register/
  - Request Body: username, password
  - Response: token ( authentication token)

## Login
- POST /login/
  - Request Body: username, password
  - Response: token (authentication token)

## Token
- GET /token/
  - Response: token (authentication token for the current user)

### Requirements
- Python 3.6+
- Django 3.2+
- Django REST Framework 3.12+

### Installation
- Clone the repository: git clone https://github.com/ your-username/your-repo-name.git
- Install dependencies: pip install -r requirements.txt
- Run migrations: python manage.py migrate
- Start the server: python manage.py runserver

### Usage
- Register a new user: curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "password": "password123"}' http://localhost:8000/register/
- Login with the new user: curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "password": "password123"}' http://localhost:8000/login/
- Get the authentication token: curl -X GET http://localhost:8000/token/

### License
This project is licensed under the MIT License. See LICENSE for details.