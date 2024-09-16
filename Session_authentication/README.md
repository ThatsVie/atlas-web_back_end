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

5. **Test `GET /api/v1

/users/me` Endpoint with Basic Authorization:**
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
     `http://0.0.0.0:5000/api/v1/status`
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

2. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Open the following URL in the address bar:  
     `http://0.0.0.0:5000/api/v1/users`
   - **Expected Output:**  
   The browser will display a JSON response indicating `"error": "Unauthorized"`.

3. **Test `GET /api/v1/users/me` Endpoint with Basic Authorization:**
   - For this test, use a browser extension or tool that allows you to set custom headers (such as [ModHeader](https://modheader.com/)).
   - Set the `Authorization` header to:  
     `Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh`
   - Enter the following URL in the address bar:  
     `http://0.0.0.0:5000/api/v1/users/me`
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
     `http://0.0.0.0:5000/api/v1/status`
   - **Expected Output:**
   ```json
   {
     "status": "OK"
   }
   ```

2. **Test `GET /api/v1/users` Endpoint Without Authorization:**
   - Enter the following URL in the address bar:  
     `http://0.0.0.0:5000/api/v1/users`
   - **Expected Output:**  
   The browser will display a JSON response indicating `"error": "Unauthorized"`.

3. **Test `GET /api/v1/users` Endpoint with Incorrect Authorization:**
   - For this test, use a browser extension or tool that allows you to set custom headers (such as [ModHeader](https://modheader.com/)).
   - Set the `Authorization` header to:  
     `Test`
   - Enter the following URL in the address bar:  
     `http://0.0.0.0:5000/api/v1/users`
   - **Expected Output:**  
   The browser should display a JSON response indicating `"error": "Forbidden"`.

### Explanation of Changes

- **Creation of `SessionAuth` Class:**
  - A new class `SessionAuth` is created in `session_auth.py` inheriting from `Auth`. For now, this class is empty but sets up the structure for future development of session-based authentication.
  
- **Updating `api/v1/app.py` to Use `SessionAuth`:**
  - The `api/v1/app.py` file is updated to import and create an instance of `SessionAuth` when the `AUTH_TYPE` environment variable is set to `session_auth`. This change allows switching between different authentication mechanisms based on the environment variable.


</details>
