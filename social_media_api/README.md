# Follow Endpoints

## Follow a User

* **URL:** `/accounts/follow/<int:user_id>/`
* **Method:** `POST`
* **Description:** Follow a user.
* **Request Body:** None
* **Response:** `200 OK` if successful, `404 Not Found` if the user does not exist.

## Unfollow a User

* **URL:** `/accounts/unfollow/<int:user_id>/`
* **Method:** `POST`
* **Description:** Unfollow a user.
* **Request Body:** None
* **Response:** `200 OK` if successful, `404 Not Found` if the user does not exist.

# Feed Endpoint

## Get Feed

* **URL:** `/posts/feed/`
* **Method:** `GET`
* **Description:** Get the feed of posts from followed users.
* **Request Body:** None
* **Response:** A list of posts in JSON format, ordered by creation date.

**Likes Endpoints**

### Like a Post

* **POST** `/posts/<int:pk>/like/`
* Request Body: None
* Response: `Like` object with `id`, `post`, `user`, and `created_at` fields

### Unlike a Post

* **POST** `/posts/<int:pk>/unlike/`
* Request Body: None
* Response: `message` field with "Post unliked" or "You did not like this post"

**Notifications Endpoints**

### Get Notifications

* **GET** `/notifications/`
* Request Body: None
* Response: List of `Notification` objects with `id`, `recipient`, `actor`, `verb`, `target`, and `timestamp` fields

### Create Notification

* **POST** `/notifications/`
* Request Body: `verb`, `target_id`, and `target_model` fields
* Response: `Notification` object with `id`, `recipient`, `actor`, `verb`, `target`, and `timestamp` fields