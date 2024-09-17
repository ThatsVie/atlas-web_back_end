<div align="center">
  <img src="https://github.com/user-attachments/assets/0c54eefb-e8c4-4979-962b-2c140feac23f" alt="chubbyolderpuggy">
  <h1>Session Pugthentication</h1>
</div>

This project focuses on implementing a Session Authentication system in a Python web application using the Flask framework. You will create your own session authentication mechanism without relying on external modules, allowing you to understand each step of the process. Although it's common to use pre-built libraries for authentication in real-world applications, this project will enhance your understanding by building the mechanism from scratch.

## Background Context

In the industry, developing your own session authentication system is generally discouraged in favor of using established modules or frameworks, such as [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/). However, for learning purposes, this project will guide you through the core concepts and steps of creating a session authentication system to help deepen your understanding of the mechanism.

## Resources

- **[REST API Authentication Mechanisms - Session Auth](https://www.youtube.com/watch?v=501dpx2IjGY):** Focuses on session authentication methods in REST APIs, explaining how sessions are created, managed, and validated.
  
- **[HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie):** An overview of HTTP cookies, including their structure, usage, and how they are transmitted between clients and servers.
  
- **[Flask](https://palletsprojects.com/projects/flask/):** A lightweight WSGI web application framework in Python, providing tools for building web applications, including support for sessions and cookies.
  
- **[Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies):** Detailed documentation on managing cookies in Flask, including setting, retrieving, and deleting cookies.

## Learning Objectives


- **Explain what authentication means**: Understand the process of verifying the identity of a user or entity to control access to resources.
  
- **Describe session authentication**: Understand how session-based authentication works, including the creation, management, and validation of sessions.

- **Define cookies**: Learn what cookies are, their purpose, and how they are used in web development.

- **Send cookies correctly**: Understand how to transmit cookies between clients and servers.

- **Parse cookies**: Learn how to extract and interpret cookie data for authentication purposes.

## Requirements

- **Python Scripts:**
  - Must be compatible with Python 3.9 on Ubuntu 20.04 LTS.
  - All files should end with a new line and start with `#!/usr/bin/env python3`.
  - The project must include a README.md file at the root of the project folder.
  - Follow `pycodestyle` style guidelines (version 2.5).
  - All files must be executable.
  - Length of files will be tested using `wc`.
  - All modules, classes, and functions must have detailed documentation explaining their purpose and functionality.

## Tasks and Detailed Usage

**Note:**  
Throughout the following tasks, you will see references to `0.0.0.0` as the host address for the API server. However, I am using **VS Code** for development and testing, and I prefer to use `localhost` (`http://localhost:5000`) instead of `0.0.0.0`. Here's why:

- **`localhost`** refers specifically to the local machine and resolves to the IP address `127.0.0.1`, which is convenient for local testing in a browser.
- **`0.0.0.0`** is a special address that makes the server listen on all available network interfaces of the local machine. While this allows access from other devices on the same network, using `localhost` is functionally equivalent and more straightforward for local testing within VS Code.

For consistency and simplicity, I will use `http://localhost:5000` in place of `http://0.0.0.0:5000` when testing the API in the browser.

**Testing with Postman, curl commands, and a web browser:**  
To comprehensively test the API endpoints, we'll use multiple methods: **Postman** for a user-friendly interface, **curl commands** in the terminal for command-line proficiency, and direct testing in the **web browser** for quick checks. The following instructions will guide you on how to use these three methods to test each task effectively.


**Important:**  
Between tasks, make sure to terminate the running server before starting a new one to test the next task. If you don't terminate the server, the port (`5000`) will be busy, and the new instance of the server will not start correctly. To stop the server, use `CTRL+C` in the terminal where the server is running.

<details>
<summary><strong>Task 0: Et moi et moi et moi!</strong></summary>

In this task, we will extend the existing Basic Authentication system by adding a new endpoint, `GET /api/v1/users/me`, which retrieves the authenticated User object. We will modify the application to handle session authentication and ensure the new functionality is correctly implemented.

<details>
<summary>Instructions Provided in Curriculum</summary>
Copy all your work of the 0x06. Basic authentication project in this new folder.  
In this version, you implemented a Basic authentication for giving you access to all User endpoints:  
- `GET /api/v1/users`  
- `POST /api/v1/users`  
- `GET /api/v1/users/<user_id>`  
- `PUT /api/v1/users/<user_id>`  
- `DELETE /api/v1/users/<user_id>`  

Now, you will add a new endpoint: `GET /users/me` to retrieve the authenticated User object.

1. Copy folders `models` and `api` from the previous project **0x06. Basic authentication**.
2. Ensure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
3. Update `@app.before_request` in `api/v1/app.py`:
   - Assign the result of `auth.current_user(request)` to `request.current_user`.
4. Update the method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
   - If `<user_id>` is equal to `me` and `request.current_user` is `None`: abort(404)
   - If `<user_id>` is equal to `me` and `request.current_user` is not `None`: return the authenticated User in a JSON response (like a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid User ID).
   - Otherwise, keep the same behavior.
</details>

### Step-by-Step Instructions

1. **Copy Files from Previous Project:**
   - Copy all necessary files from the `0x06. Basic authentication` project to the `Session_authentication` directory, including:
     - `models/`
     - `api/`
     - `requirements.txt`

2. **Update `api/v1/app.py`:**
   - Modify the `@app.before_request` handler in `api/v1/app.py` to assign the result of `auth.current_user(request)` to `request.current_user`.
   ```python
   request.current_user = auth.current_user(request)
   ```

3. **Update `api/v1/views/users.py`:**
   - Add logic to handle the new `GET /api/v1/users/me` endpoint by modifying the `GET /api/v1/users/<user_id>` route in `users.py`:
   ```python
   if user_id == "me":
       if request.current_user is None:
           abort(404)
       else:
           return jsonify(request.current_user.to_json()), 200
   ```

4. **Make `main_0.py` Executable:**
   - Ensure that the `main_0.py` script is executable:
   ```bash
   chmod +x main_0.py
   ```

5. **Run the Test Script:**
   - Execute `main_0.py` to create a test user and generate Base64-encoded credentials:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py
   ```

6. **Start the API Server:**
   - Start the Flask API server in another terminal:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

### Explanation of Changes

- **Modification of `@app.before_request` in `api/v1/app.py`:**  
  The `before_request_handler` function is updated to assign the result of `auth.current_user(request)` to `request.current_user`. This assignment ensures that the currently authenticated user is accessible in every request that requires authentication. It allows you to easily retrieve the authenticated user's details and use them in route handlers, such as for the `GET /api/v1/users/me` endpoint.

- **New Logic in `GET /api/v1/users/<user_id>` Route in `api/v1/views/users.py`:**  
  The route is modified to handle requests where `<user_id>` is `"me"`. When the endpoint is hit with `"me"`, it checks if there is a currently authenticated user (`request.current_user`). If not, it returns a 404 error. If an authenticated user exists, it returns that user's information in JSON format. This makes it easy for users to retrieve their own profile information without needing to know their user ID.

### Testing with `curl`

To test the new endpoint and authentication functionality using `curl` commands:

1. **Check the API Status:**
   - Use `curl` to check if the API is running correctly:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   ```
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

2. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Use `curl` to test the endpoint without providing any credentials:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/users"
   ```
   - **Expected Output:**
   ```json
   {
     "error": "Unauthorized"
   }
   ```

3. **Test `GET /api/v1/users` Endpoint with Basic Authorization:**
   - Use `curl` with the `Authorization` header to provide Base64-encoded credentials:
   ```bash
   curl -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" "http://0.0.0.0:5000/api/v1/users"
   ```
   - **Expected Output:**
   ```json
   [
     {
       "created_at": "2024-09-16T20:07:58",
       "email": "bob@hbtn.io",
       "first_name": null,
       "id": "f03fce22-82d5-4ff4-9327-46e42244cc42",
       "last_name": null,
       "updated_at": "2024-09-16T20:07:58"
     }
   ]
   ```

4. **Test `GET /api/v1/users/me` Endpoint with Basic Authorization:**
   - Use `curl` to access the `/api/v1/users/me` endpoint with the same `Authorization` header:
   ```bash
   curl -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" "http://0.0.0.0:5000/api/v1/users/me"
   ```
   - **Expected Output:**
   ```json
   {
     "created_at": "2024-09-16T20:07:58",
     "email": "bob@hbtn.io",
     "first_name": null,
     "id": "f03fce22-82d5-4ff4-9327-46e42244cc42",
     "last_name": null,
     "updated_at": "2024-09-16T20:07:58"
   }
   ```

### Testing with Postman

To test the new endpoint and authentication functionality using Postman:

1. **Open Postman** and create a new request.
   
2. **Test API Status Endpoint:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/status`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

3. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/users`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "error": "Unauthorized"
   }
   ```

4. **Test `GET /api/v1/users` Endpoint with Basic Authorization:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/users`
   - Go to the "Authorization" tab.
   - Choose "Basic Auth" and enter the credentials:
     - **Username:** `bob@hbtn.io`
     - **Password:** `H0lbertonSchool98!`
   - Click "Send".
   - **Expected Output:**
   ```json
   [
     {
       "created_at": "2024-09-16T20:07:58",
       "email": "bob@hbtn.io",
       "first_name": null,
       "id": "f03fce22-82d5-4ff4-9327-46e42244cc42",
       "last_name": null,
       "updated_at": "2024-09-16T20:07:58"
     }
   ]
   ```

5. **Test `GET /api/v1/users/me` Endpoint with Basic Authorization:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/users/me`
   - Go to the "Authorization" tab.
   - Choose "Basic Auth" and enter the same credentials:
     - **Username:** `bob@hbtn.io`
     - **Password:** `H0lbertonSchool98!`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "created_at": "2024-09-16T20:07:58",
     "email": "bob@hbtn.io",
     "first_name": null,
     "id": "f03fce22-82d5-4ff4-9327-46e42244cc42",
     "last_name": null,
     "updated_at": "2024-09-16T20:07:58"
   }
   ```

### Testing with Web Browser

To test the endpoints using a web browser:

1. **Test API Status Endpoint:**
   - Open your web browser (e.g., Chrome, Firefox).
   - Enter the following URL in the address bar:
   ``` 
   http://localhost:5000/api/v1/status
   ```
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

2. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Open the following URL in the address bar:
   ```
   http://localhost:5000/api/v1/users
   ```
     
   - **Expected Output:**  
   The browser will display a JSON response indicating `"error": "Unauthorized"`.

3. **Test `GET /api/v1/users/me` Endpoint with Basic Authorization:**
   - For this test, use a browser extension or tool that allows you to set custom headers (such as [ModHeader](https://modheader.com/)).
   - Set the `Authorization` header to:  
     `Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh`
   - Enter the following URL in the address bar:
     ```
     http://localhost:5000/api/v1/users/me
     ```
   - **Expected Output:**  
   The browser should display the authenticated user's details in JSON format.

</details>

<details>
<summary><strong>Task 1: Empty session</strong></summary>

In this task, you will start creating a new session-based authentication mechanism by defining an empty class, SessionAuth, that inherits from Auth. You will update the application to use this new authentication class when the AUTH_TYPE environment variable is set to session_auth, ensuring that the application can switch between different authentication mechanisms using environment variables.

<details>
<summary>Instructions Provided in Curriculum</summary>
Create a class SessionAuth that inherits from Auth. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:
validate if everything inherits correctly without any overloading
validate the “switch” by using environment variables
Update api/v1/app.py for using SessionAuth instance for the variable auth depending of the value of the environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:
import SessionAuth from api.v1.auth.session_auth
create an instance of SessionAuth and assign it to the variable auth
Otherwise, keep the previous mechanism.
</details>

### Step-by-Step Instructions

1. **Create a New Class `SessionAuth`:**
   - Create a new file named `session_auth.py` in the `api/v1/auth` directory.
   - Inside `session_auth.py`, define a new class `SessionAuth` that inherits from `Auth`. This class will be empty for now.

   **File: `api/v1/auth/session_auth.py`**
   ```python
   #!/usr/bin/env python3
   """ SessionAuth module
   """
   from api.v1.auth.auth import Auth


   class SessionAuth(Auth):
       """ Empty class for Session Authentication """
       pass
   ```

2. **Update `api/v1/app.py` to Use `SessionAuth`:**
   - Modify the `api/v1/app.py` file to create an instance of `SessionAuth` if the `AUTH_TYPE` environment variable is set to `session_auth`.

   **File: `api/v1/app.py`**
   ```python
   #!/usr/bin/env python3
   """
   Route module for the API
   """
   from os import getenv
   from api.v1.views import app_views
   from flask import Flask, jsonify, abort, request
   from flask_cors import (CORS, cross_origin)
   import os

   app = Flask(__name__)
   app.register_blueprint(app_views)
   CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

   auth = None
   AUTH_TYPE = getenv("AUTH_TYPE")

   # Load the correct Auth class based on the environment variable
   if AUTH_TYPE == 'auth':
       from api.v1.auth.auth import Auth
       auth = Auth()
   elif AUTH_TYPE == 'basic_auth':
       from api.v1.auth.basic_auth import BasicAuth
       auth = BasicAuth()
   elif AUTH_TYPE == 'session_auth':
       from api.v1.auth.session_auth import SessionAuth
       auth = SessionAuth()  # Use SessionAuth if AUTH_TYPE is 'session_auth'

   @app.errorhandler(404)
   def not_found(error) -> str:
       """
       Not found handler
       """
       return jsonify({"error": "Not found"}), 404

   @app.errorhandler(401)
   def unauthorized(error) -> str:
       """
       Unauthorized handler
       """
       return jsonify({"error": "Unauthorized"}), 401

   @app.errorhandler(403)
   def forbidden(error) -> str:
       """
       Forbidden handler
       """
       return jsonify({"error": "Forbidden"}), 403

   @app.before_request
   def before_request_handler():
       """
       Before request handler to filter each request.
       """
       if auth is None:
           return
       excluded_paths = [
           '/api/v1/status/',
           '/api/v1/unauthorized/',
           '/api/v1/forbidden/'
       ]
       if not auth.require_auth(request.path, excluded_paths):
           return
       if auth.authorization_header(request) is None:
           abort(401)
       request.current_user = auth.current_user(request)  # Assign current user
       if request.current_user is None:
           abort(403)

   if __name__ == "__main__":
       host = getenv("API_HOST", "0.0.0.0")
       port = getenv("API_PORT", "5000")
       app.run(host=host, port=port)
   ```

3. **Test the Implementation:**

   - Open two terminals to test the new authentication mechanism.

   **First Terminal:**
   - Start the Flask API server with `AUTH_TYPE` set to `session_auth`:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
   ```

   **Second Terminal:**
   - Run the following `curl` commands to test the functionality:

   - **Check the API Status:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   ```
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

   - **Test with Slash at the End:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status/"
   ```
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

   - **Test `GET /api/v1/users` Without Authorization:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/users"
   ```
   - **Expected Output:**
   ```json
   {
     "error": "Unauthorized"
   }
   ```

   - **Test with Incorrect Authorization Header:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
   ```
   - **Expected Output:**
   ```json
   {
     "error": "Forbidden"
   }
   ```

### Testing with Postman

To test the new endpoint and authentication functionality using Postman:

1. **Open Postman** and create a new request.

2. **Test API Status Endpoint:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/status`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

3. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/users`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "error": "Unauthorized"
   }
   ```

4. **Test `GET /api/v1/users` Endpoint with Incorrect Authorization:**
   - Set the request type to `GET`.
   - Enter the URL: `http://0.0.0.0:5000/api/v1/users`
   - Go to the "Headers" tab.
   - Add a new header with:
     - **Key:** `Authorization`
     - **Value:** `Test`
   - Click "Send".
   - **Expected Output:**
   ```json
   {
     "error": "Forbidden"
   }
   ```

### Testing with Web Browser

To test the endpoints using a web browser:

1. **Test API Status Endpoint:**
   - Open your web browser (e.g., Chrome, Firefox).
   - Enter the following URL in the address bar:
     ```
     http://localhost:5000/api/v1/status
     ```
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

2. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Enter the following URL in the address bar:
     ```  
     http://localhost:5000//api/v1/users
     ```
   - **Expected Output:**  
   The browser will display a JSON response indicating `"error": "Unauthorized"`.

3. **Test `GET /api/v1/users` Endpoint with Incorrect Authorization:**
   - For this test, use a browser extension or tool that allows you to set custom headers (such as [ModHeader](https://modheader.com/)).
   - Set the `Authorization` header to:  
     `Test`
   - Enter the following URL in the address bar:
     ```
     http://localhost:5000/api/v1/users
     ```
   - **Expected Output:**  
   The browser should display a JSON response indicating `"error": "Forbidden"`.

### Explanation of Changes

- **Creation of `SessionAuth` Class:**
  - A new class `SessionAuth` is created in `session_auth.py` inheriting from `Auth`. For now, this class is empty but sets up the structure for future development of session-based authentication.
  
- **Updating `api/v1/app.py` to Use `SessionAuth`:**
  - The `api/v1/app.py` file is updated to import and create an instance of `SessionAuth` when the `AUTH_TYPE` environment variable is set to `session_auth`. This change allows switching between different authentication mechanisms based on the environment variable.

</details>

<details>
<summary><strong>Task 2: Create a session</strong></summary>

In this task, you will enhance the `SessionAuth` class by implementing a method to create and store session IDs associated with user IDs. This mechanism will allow multiple sessions per user and facilitate session-based authentication in future tasks.

<details>
<summary>Instructions Provided in Curriculum</summary>
Update the `SessionAuth` class:

1. Create a class attribute `user_id_by_session_id` initialized as an empty dictionary.
2. Create an instance method `create_session(self, user_id: str = None) -> str` that creates a Session ID for a `user_id`:
   - Return `None` if `user_id` is `None`.
   - Return `None` if `user_id` is not a string.
   - Otherwise:
     - Generate a Session ID using the `uuid` module and `uuid4()` like the ID in Base.
     - Use this Session ID as the key of the dictionary `user_id_by_session_id` — the value for this key must be `user_id`.
     - Return the Session ID.
3. The same `user_id` can have multiple Session IDs; indeed, the `user_id` is the value in the dictionary `user_id_by_session_id`.

Now you have an "in-memory" Session ID storing. You will be able to retrieve a User ID based on a Session ID.
</details>

### Step-by-Step Instructions

1. **Update the `SessionAuth` Class:**
   - Open the file `session_auth.py` located in `api/v1/auth/`.
   - Update the `SessionAuth` class to include a new class attribute and instance method as described below.

   **File: `api/v1/auth/session_auth.py`**
   ```python
   #!/usr/bin/env python3
   """ 
   This module contains the SessionAuth class for handling 
   session-based authentication in the API.
   """
   from api.v1.auth.auth import Auth
   import uuid


   class SessionAuth(Auth):
       """ SessionAuth class for handling session authentication """

       # Class attribute to store user IDs by session ID
       user_id_by_session_id = {}

       def create_session(self, user_id: str = None) -> str:
           """
           Creates a Session ID for a given user_id
           Args:
               user_id (str): The user ID to create a session for
           Returns:
               str: The generated Session ID or None if user_id is invalid
           """
           if user_id is None or not isinstance(user_id, str):
               return None

           # Generate a new Session ID using uuid4
           session_id = str(uuid.uuid4())

           # Store the user_id with the generated session_id
           self.user_id_by_session_id[session_id] = user_id

           return session_id
   ```

2. **Use `main_1.py` Script for Testing:**

   **File: `main_1.py`**
   ```python
   #!/usr/bin/env python3
   """ Main 1
   """
   from api.v1.auth.session_auth import SessionAuth

   sa = SessionAuth()

   print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

   user_id = None
   session = sa.create_session(user_id)
   print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

   user_id = 89
   session = sa.create_session(user_id)
   print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

   user_id = "abcde"
   session = sa.create_session(user_id)
   print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

   user_id = "fghij"
   session = sa.create_session(user_id)
   print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

   user_id = "abcde"
   session = sa.create_session(user_id)
   print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
   ```

3. **Make `main_1.py` Executable:**
   - Ensure `main_1.py` is executable:
   ```bash
   chmod +x main_1.py
   ```

4. **Run the Test Script:**
   - Execute `main_1.py` to test the creation of sessions:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py
   ```

   **Expected Output:**
   ```bash
   <class 'dict'>: {}
   None => None: {}
   89 => None: {}
   abcde => 00103b49-87fe-4e6b-9b5e-37bc6b76c5a5: {'00103b49-87fe-4e6b-9b5e-37bc6b76c5a5': 'abcde'}
   fghij => e8140bdc-c824-49ec-b666-7067fdae1d70: {'00103b49-87fe-4e6b-9b5e-37bc6b76c5a5': 'abcde', 'e8140bdc-c824-49ec-b666-7067fdae1d70': 'fghij'}
   abcde => 8d76f983-86ad-431a-92c8-d1b99049b73d: {'00103b49-87fe-4e6b-9b5e-37bc6b76c5a5': 'abcde', 'e8140bdc-c824-49ec-b666-7067fdae1d70': 'fghij', '8d76f983-86ad-431a-92c8-d1b99049b73d': 'abcde'}
   ```

### Explanation of Output

- **Empty Dictionary Initialization:**
   - `<class 'dict'>: {}` confirms that `user_id_by_session_id` is initialized as an empty dictionary.

- **Handling `None` and Non-String User ID:**
   - `None => None: {}` and `89 => None: {}` confirm that when `user_id` is `None` or not a string, the method returns `None` and the dictionary remains unchanged.

- **Generating Session IDs for Valid User IDs:**
   - Each call to `create_session` with a valid `user_id` (e.g., `"abcde"` and `"fghij"`) generates a unique Session ID and adds it to the dictionary, showing that the same `user_id` can have multiple session IDs.

### Testing with `curl`

This task does not involve direct testing with `curl` commands since it focuses on internal class behavior. 

### Testing with Postman

Similarly, this task does not involve direct testing with Postman. The functionality is internal to the `SessionAuth` class. Future tasks may use Postman for more comprehensive testing.

### Testing with Web Browser

There is no direct testing required using a web browser for this task. The browser will not display internal changes to the `SessionAuth` class.

</details>

<details>
<summary><strong>Task 3: User ID for Session ID</strong></summary>

In this task, you will enhance the `SessionAuth` class by implementing a method to retrieve a User ID based on a given Session ID. This method, together with the existing `create_session` method, will allow you to manage sessions and authenticate users based on session data.

<details>
<summary>Instructions Provided in Curriculum</summary>
Update the `SessionAuth` class:

1. Create an instance method `def user_id_for_session_id(self, session_id: str = None) -> str:` that returns a User ID based on a Session ID:
   - Return `None` if `session_id` is `None`.
   - Return `None` if `session_id` is not a string.
   - Otherwise, return the value (the User ID) for the key `session_id` in the dictionary `user_id_by_session_id`.
   - Use the `.get()` method to access the value based on the key in the dictionary.

Now you have two methods (`create_session` and `user_id_for_session_id`) for storing and retrieving a link between a User ID and a Session ID.
</details>

### Step-by-Step Instructions

1. **Update the `SessionAuth` Class:**
   - Open the file `session_auth.py` located in `api/v1/auth/`.
   - Update the `SessionAuth` class to include a new instance method `user_id_for_session_id` as described below.

   **File: `api/v1/auth/session_auth.py`**
   ```python
   #!/usr/bin/env python3
   """ 
   This module contains the SessionAuth class for handling 
   session-based authentication in the API.
   """
   from api.v1.auth.auth import Auth
   import uuid


   class SessionAuth(Auth):
       """ SessionAuth class for handling session authentication """

       # Class attribute to store user IDs by session ID
       user_id_by_session_id = {}

       def create_session(self, user_id: str = None) -> str:
           """
           Creates a Session ID for a given user_id
           Args:
               user_id (str): The user ID to create a session for
           Returns:
               str: The generated Session ID or None if user_id is invalid
           """
           if user_id is None or not isinstance(user_id, str):
               return None

           # Generate a new Session ID using uuid4
           session_id = str(uuid.uuid4())

           # Store the user_id with the generated session_id
           self.user_id_by_session_id[session_id] = user_id

           return session_id

       def user_id_for_session_id(self, session_id: str = None) -> str:
           """
           Retrieves the User ID associated with a given Session ID
           Args:
               session_id (str): The Session ID to retrieve the User ID for
           Returns:
               str: The User ID associated with the Session ID or None if not found
           """
           if session_id is None or not isinstance(session_id, str):
               return None

           # Retrieve the User ID using the session_id
           return self.user_id_by_session_id.get(session_id)
   ```

2. **Use `main_2.py` Script for Testing:**

   **File: `main_2.py`**
   ```python
   #!/usr/bin/env python3
   """ Main 2
   """
   from api.v1.auth.session_auth import SessionAuth

   sa = SessionAuth()

   user_id_1 = "abcde"
   session_1 = sa.create_session(user_id_1)
   print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

   user_id_2 = "fghij"
   session_2 = sa.create_session(user_id_2)
   print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

   print("---")

   tmp_session_id = None
   tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
   print("{} => {}".format(tmp_session_id, tmp_user_id))

   tmp_session_id = 89
   tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
   print("{} => {}".format(tmp_session_id, tmp_user_id))

   tmp_session_id = "doesntexist"
   tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
   print("{} => {}".format(tmp_session_id, tmp_user_id))

   print("---")

   tmp_session_id = session_1
   tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
   print("{} => {}".format(tmp_session_id, tmp_user_id))

   tmp_session_id = session_2
   tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
   print("{} => {}".format(tmp_session_id, tmp_user_id))

   print("---")

   session_1_bis = sa.create_session(user_id_1)
   print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

   tmp_user_id = sa.user_id_for_session_id(session_1_bis)
   print("{} => {}".format(session_1_bis, tmp_user_id))

   tmp_user_id = sa.user_id_for_session_id(session_1)
   print("{} => {}".format(session_1, tmp_user_id))
   ```

3. **Make `main_2.py` Executable:**
   - Ensure `main_2.py` is executable:
   ```bash
   chmod +x main_2.py
   ```

4. **Run the Test Script:**
   - Execute `main_2.py` to test the retrieval of User IDs based on Session IDs:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py
   ```

   **Expected Output:**
   ```bash
   abcde => 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
   fghij => a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
   ---
   None => None
   89 => None
   doesntexist => None
   ---
   8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
   a159ee3f-214e-4e91-9546-ca3ce873e975 => fghij
   ---
   abcde => 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
   5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee => abcde
   8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
   ```

### Explanation of Output

- **Empty Dictionary Initialization:**
   - The initial output confirms that `user_id_by_session_id` starts empty and then gets populated with session data after calling `create_session`.

- **Handling Invalid Session IDs:**
   - `None => None`, `89 => None`, and `doesntexist => None` confirm that if the session ID is `None`, not a string, or does not exist in the dictionary, the method returns `None`.

- **Retrieving Valid User IDs:**
   - The method correctly returns the associated user IDs for valid session IDs (`session_1` and `session_2`).

- **Multiple Sessions for Same User:**
   - The output shows that a user can have multiple sessions (`session_1` and `session_1_bis` for `user_id_1`), and each session ID can still correctly retrieve the user ID.

### Testing with `curl`

This task does not involve direct testing with `curl` commands since it focuses on internal class behavior. 
### Testing with Postman

Similarly, this task does not involve direct testing with Postman. The functionality is internal to the `SessionAuth` class. Future tasks may use Postman for more comprehensive testing.

### Testing with Web Browser

There is no direct testing required using a web browser for this task. The browser will not display internal changes to the `SessionAuth` class.


</details>



<details>
<summary><strong>Task 4: Session Cookie</strong></summary>

In this task, you will update the `Auth` class to implement a method that retrieves the session cookie value from an incoming HTTP request. This method will enable your application to extract session IDs from cookies, facilitating session management for authenticated users.

<details>
<summary>Instructions Provided in Curriculum</summary>
Update `api/v1/auth/auth.py` by adding the method `def session_cookie(self, request=None):` that returns a cookie value from a request:

1. Return `None` if `request` is `None`.
2. Return the value of the cookie named `_my_session_id` from the request:
   - The name of the cookie must be defined by the environment variable `SESSION_NAME`.
   - Use the `.get()` method to access the cookie in the request cookies dictionary.
   - Use the environment variable `SESSION_NAME` to define the name of the cookie used for the Session ID.
</details>

### Step-by-Step Instructions

1. **Update the `Auth` Class:**
   - Open the file `auth.py` located in `api/v1/auth/`.
   - Add the `session_cookie` method as described below.

   **File: `api/v1/auth/auth.py`**
   ```python
   #!/usr/bin/env python3
"""
This module contains the Auth class for managing API authentication.
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if a given path requires authentication."""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if normalized_path.startswith(excluded_path[:-1]):
                    return False
            elif normalized_path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from the request."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user."""
        return None

    def session_cookie(self, request=None):
        """
        Retrieves the value of the session cookie from a request.
        Args:
            request (flask.Request): The HTTP request object
        Returns:
            str: The value of the session cookie or None if not found
        """
        if request is None:
            return None

        cookie_name = getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(cookie_name)

   ```

2. **Use the `main_3.py` Script for Testing:**

   **File: `main_3.py`**
   ```python
   #!/usr/bin/env python3
   """ Cookie server
   """
   from flask import Flask, request
   from api.v1.auth.auth import Auth

   auth = Auth()

   app = Flask(__name__)

   @app.route('/', methods=['GET'], strict_slashes=False)
   def root_path():
       """ Root path
       """
       return "Cookie value: {}\n".format(auth.session_cookie(request))

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port="5000")
   ```

3. **Make `main_3.py` Executable:**
   - Ensure `main_3.py` is executable:
   ```bash
   chmod +x main_3.py
   ```

4. **Run the Test Script:**
   - Execute `main_3.py` to test retrieving session cookie values:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py
   ```

5. **Testing with `curl` Commands:**
   - Open another terminal and run the following `curl` commands to test the behavior:

   ```bash
   curl "http://0.0.0.0:5000"
   ```
   **Expected Output:**
   ```
   Cookie value: None
   ```

   ```bash
   curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
   ```
   **Expected Output:**
   ```
   Cookie value: Hello
   ```

   ```bash
   curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
   ```
   **Expected Output:**
   ```
   Cookie value: C is fun
   ```

   ```bash
   curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
   ```
   **Expected Output:**
   ```
   Cookie value: None
   ```

### Explanation of Output

1. **No Cookie Provided:**
   - The first `curl` command returns `Cookie value: None` because no cookie named `_my_session_id` was provided in the request.

2. **Cookie with Valid Value Provided:**
   - The second and third `curl` commands return the values `"Hello"` and `"C is fun"`, respectively, because cookies with these values are provided using the correct name (`_my_session_id`).

3. **Incorrect Cookie Name Provided:**
   - The fourth `curl` command returns `Cookie value: None` because the cookie provided does not match the name defined by the environment variable `SESSION_NAME`.

### Testing with Postman

To test the session cookie functionality with Postman:

1. **Open Postman** and create a new `GET` request to:
   ```
   http://localhost:5000/
   ```
2. **Add a Cookie:**
   - Click on the **Cookies** tab (located below the request URL).
   - Click on "Add Cookie" for the domain `localhost`.
   - Enter the following details:
     - **Name:** `_my_session_id`
     - **Value:** `Hello`
   - Click **Save**.
   
3. **Send the Request:**
   - Go back to the **Headers** tab.
   - Click **Send** to make the request.
   - **Expected Response:**
     ```
     Cookie value: Hello
     ```

4. **Change the Cookie Value:**
   - Go back to the **Cookies** tab.
   - Modify the cookie value from `Hello` to `C is fun`.
   - Click **Save**.

5. **Send the Request Again:**
   - Click **Send** once more.
   - **Expected Response:**
     ```
     Cookie value: C is fun
     ```

6. **Test with Incorrect or Missing Cookies:**
   - Delete the `_my_session_id` cookie or rename it to `_my_session_id_fake`.
   - Send the request again.
   - **Expected Response:**
     ```
     Cookie value: None
     ```

### Testing with Web Browser

1. **Open a Web Browser (e.g., Chrome, Firefox):**
   - Enter the following URL in the address bar: 
   ```
   http://localhost:5000/
   ```

2. **Open Developer Tools:**
   - Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac) to open Developer Tools.
   - Go to the **Application** tab (in Chrome) or **Storage** tab (in Firefox).
   - Select **Cookies** from the left sidebar, and then click on `http://localhost:5000`.

3. **Add a Cookie:**
   - Right-click in the empty space under the cookies table (or click on "Add" if available).
   - **Name:** Enter `_my_session_id`.
   - **Value:** Enter `Hello`.
   - **Domain:** Should automatically be set to `localhost`.

4. **Refresh the Page:**
   - Refresh the browser page (`http://localhost:5000/`).
   - **Expected Output:**
     ```
     Cookie value: Hello
     ```

5. **Modify the Cookie Value:**
   - Change the value of `_my_session_id` to `C is fun` in the same Cookies section.
   - Refresh the page.
   - **Expected Output:**
     ```
     Cookie value: C is fun
     ```

6. **Test with Incorrect or Missing Cookies:**
   - Delete the `_my_session_id` cookie or rename it to `_my_session_id_fake`.
   - Refresh the page.
   - **Expected Output:**
     ```
     Cookie value: None
     ```


</details>

<details>
<summary><strong>Task 5: Before request</strong></summary>


In this task, you will update the `@app.before_request` method in `api/v1/app.py` to handle session-based authentication. The new changes will allow for checking the presence of both an authorization header and a session cookie, ensuring proper access control to your API endpoints.

<details>
<summary>Instructions Provided in Curriculum</summary>

Update the `@app.before_request` method in `api/v1/app.py`:

1. Add the URL path `/api/v1/auth_session/login/` to the list of excluded paths in the method `require_auth`. This route doesn’t exist yet, but it should be accessible outside authentication.
2. If both `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`, abort with a `401 Unauthorized` error.

</details>

### Step-by-Step Instructions

1. **Update `app.py`:**
   - Open the file `app.py` located in `api/v1/`.
   - Make the following changes to handle session-based authentication properly.

   **Updated `app.py` Code:**
   ```python
   #!/usr/bin/env python3
   """
   Route module for the API
   """
   from os import getenv
   from api.v1.views import app_views
   from flask import Flask, jsonify, abort, request
   from flask_cors import (CORS, cross_origin)
   import os

   app = Flask(__name__)
   app.register_blueprint(app_views)
   CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

   auth = None
   AUTH_TYPE = getenv("AUTH_TYPE")

   # Load the correct Auth class based on the environment variable
   if AUTH_TYPE == 'auth':
       from api.v1.auth.auth import Auth
       auth = Auth()
   elif AUTH_TYPE == 'basic_auth':
       from api.v1.auth.basic_auth import BasicAuth
       auth = BasicAuth()
   elif AUTH_TYPE == 'session_auth':
       from api.v1.auth.session_auth import SessionAuth
       auth = SessionAuth()  # Use SessionAuth if AUTH_TYPE is 'session_auth'


   @app.errorhandler(404)
   def not_found(error) -> str:
       """
       Not found handler
       """
       return jsonify({"error": "Not found"}), 404


   @app.errorhandler(401)
   def unauthorized(error) -> str:
       """
       Unauthorized handler
       """
       return jsonify({"error": "Unauthorized"}), 401


   @app.errorhandler(403)
   def forbidden(error) -> str:
       """
       Forbidden handler
       """
       return jsonify({"error": "Forbidden"}), 403


   @app.before_request
   def before_request_handler():
       """
       Before request handler to filter each request.
       """
       if auth is None:
           return
       excluded_paths = [
           '/api/v1/status/',
           '/api/v1/unauthorized/',
           '/api/v1/forbidden/',
           '/api/v1/auth_session/login/'  # Add this route to excluded paths
       ]
       if not auth.require_auth(request.path, excluded_paths):
           return

       # Check for both authorization header and session cookie
       if (auth.authorization_header(request) is None and
               auth.session_cookie(request) is None):
           abort(401)

       request.current_user = auth.current_user(request)
       if request.current_user is None:
           abort(403)


   if __name__ == "__main__":
       host = getenv("API_HOST", "0.0.0.0")
       port = getenv("API_PORT", "5000")
       app.run(host=host, port=port)
   ```

2. **Explanation of the Code Changes:**

   - **Excluded Paths Update:**
     - The URL path `/api/v1/auth_session/login/` is added to the `excluded_paths` list, allowing it to be accessed without authentication.
   - **Combined Authentication Check:**
     - The check ensures that if both `auth.authorization_header(request)` and `auth.session_cookie(request)` are `None`, a `401 Unauthorized` response is returned, blocking unauthorized access.

### Testing with `curl`

1. **Start the Server:**
   - Run the server with the following command:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
   ```

2. **Test `curl` Commands:**

   - **Check API Status:**
     ```bash
     curl "http://0.0.0.0:5000/api/v1/status"
     ```
     **Expected Output:**
     ```json
     {
       "status": "OK"
     }
     ```

   - **Check the New Login Route:**
     ```bash
     curl "http://0.0.0.0:5000/api/v1/auth_session/login"
     ```
     **Expected Output:**
     ```json
     {
       "error": "Not found"
     }
     ```
     - The output should show "Not found" but should not be blocked by the authentication system.

   - **Check Unauthorized Access:**
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users/me"
     ```
     **Expected Output:**
     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **Check with Basic Auth (will fail because `AUTH_TYPE` is `session_auth`):**
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
     ```
     **Expected Output:**
     ```json
     {
       "error": "Forbidden"
     }
     ```

   - **Check with Invalid Session Cookie:**
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76"
     ```
     **Expected Output:**
     ```json
     {
       "error": "Forbidden"
     }
     ```

### Testing with Postman

To test the updated authentication mechanism with Postman:

1. **Open Postman** and create a new `GET` request to:
   ```
   http://localhost:5000/api/v1/users/me
   ```
2. **Test Unauthorized Access:**
   - Click **Send** without adding any authorization or cookies.
   - **Expected Response:**
   ```json
   {
     "error": "Unauthorized"
   }
   ```

3. **Test with Basic Auth:**
   - Go to the **Authorization** tab and select `Basic Auth`.
   - Enter the following credentials:
     - **Username:** `bob@hbtn.io`
     - **Password:** `H0lbertonSchool98!`
   - **Send the Request:**
   - **Expected Response:**
   ```json
   {
     "error": "Forbidden"
   }
   ```
   - This response confirms that Basic Authentication won't work when `AUTH_TYPE` is set to `session_auth`.

4. **Test with Session Cookie:**
   - Go to the **Cookies** tab.
   - Add a cookie named `_my_session_id` with a value like `5535d4d7-3d77-4d06-8281-495dc3acfe76`.
   - **Send the Request:**
   - **Expected Response:**
   ```json
   {
     "error": "Forbidden"
   }
   ```
   - This response confirms that a session cookie without an associated user will be rejected.

### Testing with Web Browser

1. **Open a Web Browser (e.g., Chrome, Firefox):**
   - Enter the URL in the address bar: 
   ```
   http://localhost:5000/api/v1/users/me
   ```

2. **Check Unauthorized Access:**
   - You should see:
   ```json
   {"error": "Unauthorized"}
   ```

3. **Add a Cookie for Session Auth:**
   - Open Developer Tools (`Ctrl+Shift+I` or `Cmd+Option+I`).
   - Go to the **Application** tab (in Chrome) or **Storage** tab (in Firefox).
   - Select **Cookies** > `http://localhost:5000`.
   - Add a cookie named `_my_session_id` with a value `5535d4d7-3d77-4d06-8281-495dc3acfe76`.
   - Refresh the page.
   - **Expected Output:**
   ```json
   {"error": "Forbidden"}
   ```
   - This indicates that the session cookie is not linked to a valid user.

</details>

<details>
<summary><strong>Task 6: Use Session ID for identifying a User</strong></summary>

In this task, you will enhance the `SessionAuth` class by implementing the `current_user` method to identify a user based on the session ID stored in a cookie. This method will allow the application to retrieve a `User` instance corresponding to a session ID.

<details>
<summary>Instructions Provided in Curriculum</summary>

Update `SessionAuth` class:

1. Create an instance method `def current_user(self, request=None):` (overload) that returns a `User` instance based on a cookie value:
   - You must use `self.session_cookie(...)` and `self.user_id_for_session_id(...)` to return the User ID based on the cookie `_my_session_id`.
   - By using this User ID, you will be able to retrieve a `User` instance from the database — you can use `User.get(...)` for retrieving a `User` from the database.
   
Now, you will be able to get a `User` based on their session ID.

</details>

### Step-by-Step Instructions

1. **Update the `SessionAuth` Class:**

Open the `session_auth.py` file located in `api/v1/auth/` and add the `current_user` method as shown below:

**File: `api/v1/auth/session_auth.py`**

```python
#!/usr/bin/env python3
"""
This module contains the SessionAuth class for handling
session-based authentication in the API.
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """SessionAuth class for handling session authentication"""

    # Class attribute to store user IDs by session ID
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a given user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new Session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the user_id with the generated session_id
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        if request is None:
            return None

        # Retrieve the session cookie value
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get the user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

```

2. **Use the `main_4.py` Script for Testing:**


**File: `main_4.py`**

```python
#!/usr/bin/env python3
""" Main 4
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

""" Create a Flask app """
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return "User found: {}\n".format(request_user.id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

3. **Make `main_4.py` Executable:**

```bash
chmod +x main_4.py
```

4. **Run the Server in the First Terminal:**

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
```

You should see output like:

```
User with ID: 7b249379-5973-4a59-a862-0378e419bc3a has a Session ID: 4a556716-27e7-4d15-9355-15377b527718
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

5. **Run the `curl` Commands in the Second Terminal:**

- **Without Cookie:**
   ```bash
   curl "http://0.0.0.0:5000/"
   ```
   **Expected Output:**
   ```
   No user found
   ```

- **With Incorrect Cookie:**
   ```bash
   curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
   ```
   **Expected Output:**
   ```
   No user found
   ```

- **With Correct Cookie:**
   ```bash
   curl "http://0.0.0.0:5000/" --cookie "_my_session_id=4a556716-27e7-4d15-9355-15377b527718"
   ```
   **Expected Output:**
   ```
   User found: 7b249379-5973-4a59-a862-0378e419bc3a
   ```

### Explanation of the Output

- **No User Found (No Cookie or Incorrect Cookie):**
   - If no session ID is provided or if an incorrect session ID is given, the server cannot find a matching user and correctly returns "No user found."
  
- **User Found (Correct Cookie):**
   - When the correct session ID is provided via the cookie `_my_session_id`, the server successfully retrieves the user and displays "User found: [User ID]."



### Testing with Postman

1. **Open Postman and Create a New `GET` Request:**
   - URL: 
   ```
   http://localhost:5000/
   ```

2. **Add a Cookie:**
   - Go to the **Cookies** tab.
   - Add a new cookie with the following details:
     - Key: `_my_session_id`
     - Value: `4a556716-27e7-4d15-9355-15377b527718`

3. **Send the Request:**
   - Click on **Send**.
   - The expected response should be:
     ```
     User found: 7b249379-5973-4a59-a862-0378e419bc3a
     ```

#### Testing with Web Browser

1. **Open a Web Browser:**
   - Enter the following URL in the address bar:
     ```
     http://localhost:5000/
     ```

2. **Add a Cookie:**
   - Open the developer tools (usually with `F12`).
   - Go to the **Application** tab (in Chrome) or **Storage** tab (in Firefox).
   - Under **Cookies**, select `http://localhost`.
   - Add a new cookie:
     - **Name**: `_my_session_id`
     - **Value**: `4a556716-27e7-4d15-9355-15377b527718`

3. **Refresh the Page:**
   - The page should display:
     ```
     User found: 7b249379-5973-4a59-a862-0378e419bc3a
     ```

</details>

<details>
<summary><strong>Task 7: New view for Session Authentication</strong></summary>

In this task, you will create a new Flask view to handle all routes related to Session Authentication. The main goal is to implement a route that will authenticate a user using email and password, create a session for the authenticated user, and store the session ID in a cookie.

<details>
<summary>Instructions Provided in Curriculum</summary>

1. Create a new Flask view in `api/v1/views/session_auth.py` with a route `POST /auth_session/login` (= `POST /api/v1/auth_session/login`):

   - Make it slash-tolerant (`/auth_session/login == /auth_session/login/`).
   - Use `request.form.get()` to retrieve `email` and `password` parameters.
   - Return a JSON error message and status code 400 if `email` is missing or empty.
   - Return a JSON error message and status code 400 if `password` is missing or empty.
   - Retrieve the `User` instance based on the `email`. Use the class method `search` of `User`.
   - Return a JSON error message and status code 404 if no user is found.
   - Return a JSON error message and status code 401 if the password is incorrect (use `is_valid_password` from the `User` instance).
   - Create a session ID for the user ID by using `auth.create_session(..)`.
   - Return the dictionary representation of the `User` using the `to_json()` method.
   - Set the cookie in the response using the value of the environment variable `SESSION_NAME` as the cookie name.

2. In `api/v1/views/__init__.py`, add this new view at the end of the file.

</details>

### Step-by-Step Instructions

1. **Create the `session_auth.py` File:**

   **File: `api/v1/views/session_auth.py`**
```python
  #!/usr/bin/env python3
"""
This module contains the view for handling Session Authentication
routes in the API. It provides a login route that creates and manages
session IDs for authenticated users.
"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """POST /api/v1/auth_session/login
    Creates a new session for a user
    """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    # Set the cookie in the response
    response = jsonify(user_json)
    cookie_name = getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)

    return response
   ```

2. **Update `__init__.py` to Include the New View:**

   **File: `api/v1/views/__init__.py`**
```python
  #!/usr/bin/env python3
"""Initialize views for the API
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import * #Added this 

User.load_from_file()

```

3. **Run the Flask Application:**

   In your terminal, run the Flask application with the following command:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
   ```

### Testing with `curl`

1. **Check for Missing Methods:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
   ```
   - **Expected Output:**
   ```html
   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
   <title>405 Method Not Allowed</title>
   <h1>Method Not Allowed</h1>
   <p>The method is not allowed for the requested URL.</p>
   ```

2. **Test with Missing Email:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
   ```
   - **Expected Output:**
   ```json
   {"error":"email missing"}
   ```

3. **Test with Missing Password:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io"
   ```
   - **Expected Output:**
   ```json
   {"error":"password missing"}
   ```

4. **Test with Non-Existent User:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io" -d "password=test"
   ```
   - **Expected Output:**
   ```json
   {"error":"no user found for this email"}
   ```

5. **Test with Wrong Password:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=test"
   ```
   - **Expected Output:**
   ```json
   {"error":"wrong password"}
   ```

6. **Test with Correct Email and Password:**
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd"
   ```
   - **Expected Output:**
   ```json
   {"created_at":"2024-09-17T19:52:13","email":"bobsession@hbtn.io","first_name":null,"id":"7b249379-5973-4a59-a862-0378e419bc3a","last_name":null,"updated_at":"2024-09-17T19:52:13"}
   ```

### Testing with Postman

1. **Open Postman** and create a new `POST` request to:
   ```
   http://localhost:5000/api/v1/auth_session/login
   ```

2. **Test with Missing Email:**
   - Click on "Send" without adding any parameters.
   - **Expected Response:**
   ```json
   {"error":"email missing"}
   ```

3. **Test with Missing Password:**
   - Add `email=guillaume@hbtn.io` as form-data.
   - Click "Send".
   - **Expected Response:**
   ```json
   {"error":"password missing"}
   ```

4. **Test with Non-Existent User:**
   - Add `email=guillaume@hbtn.io` and `password=test` as form-data.
   - Click "Send".
   - **Expected Response:**
   ```json
   {"error":"no user found for this email"}
   ```

5. **Test with Correct Email and Password:**
   - Add `email=bobsession@hbtn.io` and `password=fake pwd` as form-data.
   - Click "Send".
   - **Expected Response:**
   ```json
   {
     "created_at": "2024-09-17T19:52:13", 
     "email": "bobsession@hbtn.io", 
     "first_name": null, 
     "id": "7b249379-5973-4a59-a862-0378e419bc3a", 
     "last_name": null, 
     "updated_at": "2024-09-17T19:52:13"
   }
   ```

### Testing with Web Browser

To test the session authentication route using a web browser, follow these steps:

1. **Open Your Web Browser:**
   - Use a modern web browser like Chrome, Firefox, or Edge.

2. **Open Developer Tools:**
   - Press `F12` or right-click anywhere on the page and select "Inspect" or "Inspect Element" to open the developer tools.

3. **Go to the Network Tab:**
   - In the developer tools, click on the "Network" tab. This will allow you to see the network requests and responses made by the browser.

4. **Send a POST Request via Browser Console:**
   - Click on the "Console" tab in the developer tools.
   - To test the session login route, paste the following JavaScript code into the console and press `Enter`:
   ```javascript
   fetch("http://localhost:5000/api/v1/auth_session/login", {
       method: "POST",
       headers: {
           "Content-Type": "application/x-www-form-urlencoded"
       },
       body: new URLSearchParams({
           "email": "bobsession@hbtn.io", // Replace with the email to test
           "password": "fake pwd" // Replace with the correct or incorrect password to test various scenarios
       })
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
   ```
   - **Expected Output:**
     Depending on the email and password provided in the `body` of the request:
   - **Correct Credentials:**
     ```json
     {
       "created_at": "2024-09-17T19:52:13", 
       "email": "bobsession@hbtn.io", 
       "first_name": null, 
       "id": "7b249379-5973-4a59-a862-0378e419bc3a", 
       "last_name": null, 
       "updated_at": "2024-09-17T19:52:13"
     }
     ```
   - **Incorrect Credentials or Errors:**
     You will see the corresponding error message, such as:
     ```json
     {"error":"wrong password"}
     ```
     or
     ```json
     {"error":"no user found for this email"}
     ```

5. **Observe the Network Tab:**
   - While the console displays the output, the "Network" tab will show the request details (e.g., headers, method, and status code) and the response from the server.
   - This can help verify that the correct request was sent and received as expected.

6. **Inspect Cookies:**
   - After a successful login, check the "Application" or "Storage" tab in the developer tools.
   - Go to "Cookies" and select the domain `localhost`.
   - Verify that the cookie `_my_session_id` has been set with the correct session ID.

7. **Refresh the Page:**
   - To verify the session, you can manually refresh the page or make another request to `http://localhost:5000/api/v1/users/me` using the console:
   ```javascript
   fetch("http://localhost:5000/api/v1/users/me", {
       method: "GET",
       credentials: "include" // Include the session cookie in the request
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
   ```
   - **Expected Output:** If the session is valid, you should see the user's details.


</details>


<details>
<summary><strong>Task 8: Logout</strong></summary>

This task involves adding functionality to log out a user by deleting their session. We update the `SessionAuth` class and create a new route to handle session logout.

<details>
<summary>Instructions Provided in the Curriculum</summary>

1. **Update the `SessionAuth` Class:**
    - Create an instance method `destroy_session(self, request=None)` that deletes the user session/logout:
      - If `request` is `None`, return `False`.
      - If the request doesn’t contain the Session ID cookie, return `False` — you must use `self.session_cookie(request)`.
      - If the Session ID of the request is not linked to any User ID, return `False` — you must use `self.user_id_for_session_id(...)`.
      - Otherwise, delete the Session ID from `self.user_id_by_session_id` (as a key of this dictionary) and return `True`.

2. **Update the `session_auth.py` File:**
    - Add a new route `DELETE /api/v1/auth_session/logout`:
        - Slash tolerant.
        - Import `auth` only where needed (from `api.v1.app import auth`).
        - Use `auth.destroy_session(request)` to delete the Session ID contained in the request as a cookie:
            - If `destroy_session` returns `False`, abort with status code `404`.
            - Otherwise, return an empty JSON dictionary with the status code `200`.

</details>

---

### Step-by-Step Instructions

1. **Update the `SessionAuth` Class:**

   Update the `SessionAuth` class located in `api/v1/auth/session_auth.py` to include the `destroy_session` method.

   **Code:**
   ```python
   def destroy_session(self, request=None):
       """Deletes the user session (logs out the user)."""
       if request is None:
           return False

       # Retrieve session cookie value
       session_id = self.session_cookie(request)
       if session_id is None:
           return False

       # Check if session ID is linked to any user ID
       user_id = self.user_id_for_session_id(session_id)
       if user_id is None:
           return False

       # Delete the session ID from the dictionary
       del self.user_id_by_session_id[session_id]

       return True
   ```

2. **Update the `session_auth.py` View:**

   In `api/v1/views/session_auth.py`, add the following route to handle the logout request:

   **Code:**
   ```python
   @app_views.route(
           '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
   def session_auth_logout():
       """DELETE /api/v1/auth_session/logout
       Deletes the user session (logs out).
       """
       from api.v1.app import auth

       # Check if the session can be destroyed
       if not auth.destroy_session(request):
           abort(404)

       return jsonify({}), 200
   ```


### Testing with `curl`

1. **Login and Create a Session:**

   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
   ```
   Expected output:
   ```json
   {
     "created_at": "2024-09-17T19:52:13",
     "email": "bobsession@hbtn.io",
     "first_name": null,
     "id": "7b249379-5973-4a59-a862-0378e419bc3a",
     "last_name": null,
     "updated_at": "2024-09-17T19:52:13"
   }
   ```
   Check the `Set-Cookie` header to get the session ID (`_my_session_id`).

2. **Access User Info with Session ID:**

   ```bash
   curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=YOUR_SESSION_ID"
   ```
   Replace `YOUR_SESSION_ID` with the actual session ID obtained from the login response.

3. **Logout by Deleting the Session:**

   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=YOUR_SESSION_ID" -XDELETE
   ```
   Expected output:
   ```json
   {}
   ```

4. **Attempt to Access User Info After Logout:**

   ```bash
   curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=YOUR_SESSION_ID"
   ```
   Expected output:
   ```json
   {"error": "Forbidden"}
   ```

#### Testing with Postman

1. **Login to Create a Session:**
   - Send a `POST` request to `http://0.0.0.0:5000/api/v1/auth_session/login`.
   - Add form data:
     - `email`: `bobsession@hbtn.io`
     - `password`: `fake pwd`
   - Note the `Set-Cookie` header from the response.

2. **Access User Info:**
   - Send a `GET` request to `http://0.0.0.0:5000/api/v1/users/me`.
   - Add a cookie with key `_my_session_id` and the value of the session ID obtained in step 1.

3. **Logout:**
   - Send a `DELETE` request to `http://0.0.0.0:5000/api/v1/auth_session/logout`.
   - Include the same session ID cookie as in step 2.

4. **Check Access After Logout:**
   - Send a `GET` request again to `http://0.0.0.0:5000/api/v1/users/me` using the same cookie.
   - The response should show an error: `{"error": "Forbidden"}`.


### Troubleshooting Notes

- **Correct Session ID:** Always ensure that you are using the correct and active session ID in your requests. If you encounter a "Forbidden" error after logging out, make sure that you are using the session ID created during the login.
- **Use the Right Cookie:** Verify that the cookie name (`_my_session_id`) matches the environment variable `SESSION_NAME`.
- **Check the Terminal Outputs:** Review the output in both terminals to confirm that the session creation and deletion processes are handled as expected.

</details>