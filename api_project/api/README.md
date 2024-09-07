# Authentication and Permission Setup

## Token Authentication

To obtain a token, send a POST request to the `/api-token-auth/` endpoint with your username and password.

### Example Request
```bash
curl -X POST \
  http://localhost:8000/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d '{"username": "your_username", "password": "your_password"}'