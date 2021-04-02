# 0x06. Basic authentication

## Resources:books:

Read or watch:

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

---

## Learning Objectives:bulb:

What you should learn from this project:

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

---

## Simple HTTP API for playing with `User` model.

### Setup

```
$ pip3 install -r requirements.txt
```

### Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

---

### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

---

### Files

#### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

#### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

---

### Tasks

### [0. Simple-basic-API](./api/v1/app.py)

- Download and start your project from this archive.zip

### [1. Error handler: Unauthorized](./api/v1/app.py)

- What the HTTP status code for a request unauthorized? 401 of course!

### [2. Error handler: Forbidden](./api/v1/auth)

- What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? 403 of course!

### [3. Auth class](./api/v1/auth/auth.py)

- Now you will create a class to manage the API authentication.

### [4. Define which routes don't need authentication](./api/v1/app.py)

- Update the method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: in Auth that returns True if the path is not in the list of strings excluded_paths:

### [5. Request validation!](./api/v1/app.py)

- Now you will validate all requests to secure the API:

### [6. Basic auth](./api/v1/auth/basic_auth.py)

- Create a class BasicAuth that inherits from Auth. For the moment this class will be empty.

### [7. Basic - Base64 part](./api/v1/auth/basic_auth.py)

- Add the method def extract_base64_authorization_header(self, authorization_header: str) -> str: in the class BasicAuth that returns the Base64 part of the Authorization header for a Basic Authentication:

### [8. Basic - Base64 decode](./api/v1/auth/basic_auth.py)

- Add the method def decode_base64_authorization_header(self, base64_authorization_header: str) -> str: in the class BasicAuth that returns the decoded value of a Base64 string base64_authorization_header:

### [9. Basic - User credentials](./api/v1/auth/basic_auth.py)

- Add the method def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str) in the class BasicAuth that returns the user email and password from the Base64 decoded value.

### [10. Basic - User object](./api/v1/auth/basic_auth.py)

- Add the method def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'): in the class BasicAuth that returns the User instance based on his email and password.

### [11. Basic - Overload current_user - and BOOM!](./api/v1/auth/basic_auth.py)

- Now, you have all pieces for having a complete Basic authentication.

### [12. Basic - Allow password with ":"](./api/v1/auth/basic_auth.py)

- Improve the method def extract_user_credentials(self, decoded_base64_authorization_header) to allow password with :.

### [13. Require auth with stars](./api/v1/auth/auth.py)

- Improve def require_auth(self, path, excluded_paths) by allowing \* at the end of excluded paths.

---

## Author

- **Michelle Domingo** - [michedomingo](https://github.com/michedomingo)
