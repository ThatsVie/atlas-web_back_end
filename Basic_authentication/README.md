
<div align="center">
  <img src="https://github.com/user-attachments/assets/68a4c398-6158-43b2-a6f2-ec1a357f5390" alt="basic pawthentication">
</div>


<div align="center">
  <h1>Basic Pawthentication</h1>
</div>

## Background Context

In this project, you'll learn about the authentication process and implement Basic Authentication on a simple API. Although, in the industry, it's common to use a module or framework like [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/) for this purpose, this project focuses on building your own Basic Authentication mechanism to understand how it works.

## Resources and Brief Summaries

- **[REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY):** This video explains various ways to authenticate a user when accessing a REST API, covering Basic, Digest, Token-based, and OAuth authentication methods.
  
- **[Base64 in Python](https://docs.python.org/3.9/library/base64.html):** This Python documentation provides details about the `base64` module, which allows encoding and decoding data using Base64—a binary-to-text encoding scheme that represents binary data in an ASCII string format.
  
- **[HTTP Header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization):** This page from MDN Web Docs explains the `Authorization` HTTP header, which is used to send credentials for authenticating a user or accessing a resource.
  
- **[Flask](https://palletsprojects.com/projects/flask/):** Flask is a lightweight WSGI web application framework in Python. It's designed with simplicity in mind and provides the tools needed to build a web application, including support for handling requests and responses.
  
- **[Base64 - Concept](https://en.wikipedia.org/wiki/Base64):** This Wikipedia page provides an overview of the Base64 encoding scheme, its history, usage, and implementation details, such as the mapping of binary data to a set of 64 different ASCII characters.

## Learning Objectives
- Understand what authentication is.
- Explain what Base64 encoding is and how to encode a string in Base64.
- Describe what Basic Authentication is and how it works.
- Send the `Authorization` header correctly in HTTP requests.

## Requirements

- **Python Scripts:**
  - Must be compatible with Python 3.9 on Ubuntu 20.04 LTS.
  - All files should end with a new line and start with `#!/usr/bin/env python3`.
  - Follow `pycodestyle` style guidelines (version 2.5).
  - Ensure all files are executable.
  - Documentation is mandatory for modules, classes, and functions.
  - Length of files will be checked using `wc`.

## Project Structure

- **`models/`**
  - `base.py`: Base of all models of the API - handles serialization to a file.
  - `user.py`: User model.

- **`api/v1`**
  - `app.py`: Entry point of the API.
  - `views/index.py`: Basic endpoints of the API: `/status` and `/stats`.
  - `views/users.py`: All user endpoints.

## Setup and Installation

1. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Start the API server:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

   You should see output similar to:
   ```
   * Serving Flask app "app" (lazy loading)
   ...
   ```

## Routes

- **`GET /api/v1/status`**: Returns the status of the API.
- **`GET /api/v1/stats`**: Returns some stats of the API.
- **`GET /api/v1/users`**: Returns the list of users.
- **`GET /api/v1/users/:id`**: Returns a user based on the ID.
- **`DELETE /api/v1/users/:id`**: Deletes a user based on the ID.
- **`POST /api/v1/users`**: Creates a new user (JSON parameters: `email`, `password`, `last_name` (optional), and `first_name` (optional)).
- **`PUT /api/v1/users/:id`**: Updates a user based on the ID (JSON parameters: `last_name` and `first_name`).

## Troubleshooting
<details> <summary>
During the setup of the Basic Authentication API, several dependency conflicts were encountered due to incompatible package versions. Below is a summary of the steps taken to resolve these issues:</summary>

1. **Identified Dependency Conflicts:**
   - The initial error was due to an incompatibility between `Jinja2==2.11.2` and `MarkupSafe` versions. `Jinja2` required an older version of `MarkupSafe` that included the `soft_unicode` function, which was removed in newer versions.

2. **Downgraded `MarkupSafe` to a Compatible Version:**
   - Downgraded `MarkupSafe` to version `1.1.1` using:
     ```bash
     pip3 install markupsafe==1.1.1
     ```
   - This resolved the `soft_unicode` issue but led to another conflict with `Werkzeug`, which required a newer version of `MarkupSafe`.

3. **Aligned All Package Versions:**
   - To ensure compatibility across all dependencies, the following versions were installed:
     ```bash
     pip3 install Flask==1.1.2 Flask-Cors==3.0.8 Jinja2==2.11.2 requests==2.18.4 pycodestyle==2.6.0 MarkupSafe==1.1.1 Werkzeug==1.0.1
     ```
   - This included downgrading `Werkzeug` to version `1.0.1` to be compatible with the older `MarkupSafe`.

4. **Addressed `itsdangerous` Import Error:**
   - An import error occurred due to the installed version of `itsdangerous` (`2.1.2`) being incompatible with `Flask==1.1.2`.
   - Downgraded `itsdangerous` to version `1.1.0` to match the requirements of `Flask`:
     ```bash
     pip3 install itsdangerous==1.1.0
     ```

5. **Verified All Versions:**
   - Used the following command to verify the correct versions of all dependencies:
     ```bash
     pip3 list | grep -E 'Flask|Flask-Cors|Jinja2|requests|pycodestyle|MarkupSafe|Werkzeug|itsdangerous'
     ```

6. **Successfully Started the API Server:**
   - After aligning all package versions correctly, the API server started without errors using:
     ```bash
     API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
     ```


By carefully downgrading or upgrading packages to their compatible versions, the dependency conflicts were resolved, and the API was successfully launched.


</details>

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
<summary><strong>Task 0: Simple-basic-API</strong></summary>

This task involves setting up and running a simple API that contains a single model, `User`. The users are stored using a serialization/deserialization mechanism in files. The goal is to start the API server and confirm its functionality by making a request to a specific endpoint.

### Step-by-Step Instructions

1. **Download the Project Files:**
   - I downloaded the provided `archive.zip` containing the necessary files for the project.
   - I then extracted the contents of `archive.zip`. There was a folder named `SimpleAPI` with the following files:
     - `requirements.txt`: Lists all dependencies needed to run the API.
     - `models/`: Contains the user model and base model for handling serialization.
     - `api/v1/`: Contains the API application and endpoint views.
     - `README.md`: I incorporated relevant pieces into this README.md.

2. **Move the Files to Your Repository:**
   - I moved the contents of the `SimpleAPI` folder (`models`, `api`, `requirements.txt`, and `README.md`) to the root of your repository directory (`atlas-web_back_end/Basic_authentication`).

3. **Install the Required Dependencies:**
   - Open a terminal and navigate to the root of your repository:
     ```bash
     cd path/to/atlas-web_back_end/Basic_authentication
     ```
   - Install the required dependencies specified in `requirements.txt`:
     ```bash
     pip3 install -r requirements.txt
     ```
   - If you encounter any dependency issues, refer to the [Troubleshooting](#troubleshooting) section for steps to resolve them.

4. **Start the API Server:**
   - Once all dependencies are installed, start the API server using the following command:
     ```bash
     API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
     ```
   - You should see output indicating the Flask app is being served:
     ```
     * Serving Flask app "app" (lazy loading)
     ...
     ```

5. **Test the API Using `curl`:**
   - In another terminal tab, make a GET request to the `/status` endpoint to confirm the API is running correctly:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/status" -vvv
     ```
   - The expected output should be similar to:
     ```
     *   Trying 0.0.0.0:5000...
     * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
     > GET /api/v1/status HTTP/1.1
     > Host: 0.0.0.0:5000
     > User-Agent: curl/7.81.0
     > Accept: */*
     > 
     * Mark bundle as not supporting multiuse
     * HTTP/1.0, assume close after body
     < HTTP/1.0 200 OK
     < Content-Type: application/json
     < Content-Length: 16
     < Access-Control-Allow-Origin: *
     < Server: Werkzeug/1.0.1 Python/3.10.12
     < Date: Tue, 10 Sep 2024 19:33:19 GMT
     < 
     {"status":"OK"}
     * Closing connection 0
     ```
   - This confirms that the API server is running and responding correctly.

6. **Test the API Using Postman:**
   - **Open Postman** and create a new request:
     - Set the request type to `GET`.
     - Enter the URL:
       ```
       http://localhost:5000/api/v1/status
       ```
     - Click on "Send" to make the request.
     - You should see a JSON response similar to:
       ```json
       {"status":"OK"}
       ```

7. **Test Using a Web Browser:**
   - Open your web browser (e.g., Chrome, Firefox, Safari).
   - In the address bar, type the following URL and press Enter:
     ```
     http://localhost:5000/api/v1/status
     ```
   - The browser should display the following JSON response:
     ```json
     {"status":"OK"}
     ```
   - This confirms that the API server is running correctly and responding to HTTP GET requests.

</details>


<details>
<summary><strong>Task 1: Error handler: Unauthorized</strong></summary>

This task involves adding a new error handler for unauthorized access (HTTP status code 401) in `api/v1/app.py` and creating an endpoint that triggers this error in `api/v1/views/index.py`.

### Step-by-Step Instructions

1. **Edit `api/v1/app.py`:**
   - Add a new error handler for the 401 status code. The response should be a JSON object `{"error": "Unauthorized"}` with a status code of `401`. Use `jsonify` from Flask to format the response.
   - The updated `app.py` should look like this:

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

   @app.errorhandler(404)
   def not_found(error) -> str:
       """ Not found handler """
       return jsonify({"error": "Not found"}), 404

   @app.errorhandler(401)
   def unauthorized(error) -> str:
       """ Unauthorized handler """
       return jsonify({"error": "Unauthorized"}), 401

   if __name__ == "__main__":
       host = getenv("API_HOST", "0.0.0.0")
       port = getenv("API_PORT", "5000")
       app.run(host=host, port=port)
   ```

2. **Edit `api/v1/views/index.py`:**
   - Add a new endpoint `/api/v1/unauthorized` that raises a 401 error using `abort(401)`.
   - The updated `index.py` should look like this:

   ```python
   #!/usr/bin/env python3
   """ Module of Index views """
   from flask import jsonify, abort
   from api.v1.views import app_views

   @app_views.route('/status', methods=['GET'], strict_slashes=False)
   def status() -> str:
       """ GET /api/v1/status
       Return:
         - the status of the API
       """
       return jsonify({"status": "OK"})

   @app_views.route('/stats/', strict_slashes=False)
   def stats() -> str:
       """ GET /api/v1/stats
       Return:
         - the number of each objects
       """
       from models.user import User
       stats = {}
       stats['users'] = User.count()
       return jsonify(stats)

   @app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
   def unauthorized_endpoint():
       """ GET /api/v1/unauthorized
       Raise:
         - a 401 error
       """
       abort(401)
   ```

3. **Start the API Server:**
   - Run the following command to start the API server:
     ```bash
     API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
     ```
   - You should see output indicating the Flask app is running:
     ```
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     ```

4. **Test the Unauthorized Endpoint:**

   **Using `curl` in the Terminal:**
   - In a new terminal tab, use `curl` to test the new endpoint:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/unauthorized"
     ```
   - The expected output should be:
     ```json
     {"error":"Unauthorized"}
     ```
   - You can also use the `-vvv` flag for a verbose output:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
     ```
   - The verbose output should show:
     ```
     *   Trying 0.0.0.0:5000...
     * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
     > GET /api/v1/unauthorized HTTP/1.1
     > Host: 0.0.0.0:5000
     > User-Agent: curl/7.81.0
     > Accept: */*
     > 
     * Mark bundle as not supporting multiuse
     * HTTP/1.0 401 UNAUTHORIZED
     < Content-Type: application/json
     < Content-Length: 25
     < Access-Control-Allow-Origin: *
     < Server: Werkzeug/1.0.1 Python/3.10.12
     < Date: Tue, 10 Sep 2024 20:59:56 GMT
     < 
     {"error":"Unauthorized"}
     * Closing connection 0
     ```

   **Using a Web Browser:**
   - Open your web browser (e.g., Chrome, Firefox, Safari).
   - In the address bar, type the following URL and press Enter:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
   - The browser should display the following JSON response:
     ```json
     {"error":"Unauthorized"}
     ```
   - This confirms that the API server is running correctly and handling unauthorized access as expected.

   **Using Postman:**
   - Open **Postman** and create a new request.
   - Set the request type to **GET**.
   - Enter the following URL:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
   - Click **Send**.
   - You should see a response with status code **401** and the JSON body:
     ```json
     {"error":"Unauthorized"}
     ```
   - This confirms that the error handler for unauthorized access is working correctly in Postman.

### Note
**Make sure to terminate the server (using `CTRL+C` in the terminal) between tasks.** This prevents the port (`5000`) from being busy and ensures the new instance of the server starts correctly.

</details>


<details>
<summary><strong>Task 2: Error handler: Forbidden</strong></summary>

This task involves adding a new error handler for the 403 Forbidden status code in `api/v1/app.py` and creating an endpoint `/api/v1/forbidden` in `api/v1/views/index.py` that triggers this error using `abort(403)`.

### Step-by-Step Instructions

1. **Edit `api/v1/app.py`:**
   - Add a new error handler for the 403 status code. The response should be a JSON object `{"error": "Forbidden"}` with a status code of `403`. Use `jsonify` from Flask to format the response.

   **Updated `api/v1/app.py`:**

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

   @app.errorhandler(404)
   def not_found(error) -> str:
       """ Not found handler """
       return jsonify({"error": "Not found"}), 404

   @app.errorhandler(401)
   def unauthorized(error) -> str:
       """ Unauthorized handler """
       return jsonify({"error": "Unauthorized"}), 401

   @app.errorhandler(403)
   def forbidden(error) -> str:
       """ Forbidden handler """
       return jsonify({"error": "Forbidden"}), 403

   if __name__ == "__main__":
       host = getenv("API_HOST", "0.0.0.0")
       port = getenv("API_PORT", "5000")
       app.run(host=host, port=port)
   ```

2. **Edit `api/v1/views/index.py`:**
   - Add a new endpoint `/api/v1/forbidden` that raises a 403 error using `abort(403)`.

   **Updated `api/v1/views/index.py`:**

   ```python
   #!/usr/bin/env python3
   """ Module of Index views """
   from flask import jsonify, abort
   from api.v1.views import app_views

   @app_views.route('/status', methods=['GET'], strict_slashes=False)
   def status() -> str:
       """ GET /api/v1/status
       Return:
         - the status of the API
       """
       return jsonify({"status": "OK"})

   @app_views.route('/stats/', strict_slashes=False)
   def stats() -> str:
       """ GET /api/v1/stats
       Return:
         - the number of each objects
       """
       from models.user import User
       stats = {}
       stats['users'] = User.count()
       return jsonify(stats)

   @app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
   def unauthorized_endpoint():
       """ GET /api/v1/unauthorized
       Raise:
         - a 401 error
       """
       abort(401)

   @app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
   def forbidden_endpoint():
       """ GET /api/v1/forbidden
       Raise:
         - a 403 error
       """
       abort(403)
   ```

3. **Start the API Server:**
   - Run the following command to start the API server:
     ```bash
     API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
     ```
   - You should see output indicating the Flask app is running:
     ```
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     ```

4. **Test the Forbidden Endpoint:**

   - **Using `curl` in the Terminal:**
     - In a new terminal tab, use `curl` to test the new endpoint:
       ```bash
       curl "http://localhost:5000/api/v1/forbidden"
       ```
     - The expected output should be:
       ```json
       {"error":"Forbidden"}
       ```
     - You can also use the `-vvv` flag for a verbose output:
       ```bash
       curl "http://localhost:5000/api/v1/forbidden" -vvv
       ```
     - The verbose output should show:
       ```
       *   Trying 0.0.0.0:5000...
       * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
       > GET /api/v1/forbidden HTTP/1.1
       > Host: 0.0.0.0:5000
       > User-Agent: curl/7.81.0
       > Accept: */*
       > 
       * Mark bundle as not supporting multiuse
       * HTTP 1.0 403 FORBIDDEN
       < Content-Type: application/json
       < Content-Length: 27
       < Access-Control-Allow-Origin: *
       < Server: Werkzeug/1.0.1 Python/3.10.12
       < Date: Tue, 10 Sep 2024 22:00:56 GMT
       < 
       {"error":"Forbidden"}
       * Closing connection 0
       ```

     - This confirms that the API server is running and the 403 error handler is working correctly.

   - **Using a Web Browser:**
     - Open your web browser (e.g., Chrome, Firefox, Safari).
     - In the address bar, type the following URL and press Enter:
       ```
       http://localhost:5000/api/v1/forbidden
       ```
     - The browser should display the following JSON response:
       ```json
       {"error":"Forbidden"}
       ```
     - This confirms that the API server is running correctly and handling forbidden access as expected.

   - **Using Postman:**
     - Open **Postman** and create a new request.
     - Set the request type to **GET**.
     - Enter the following URL:
       ```
       http://localhost:5000/api/v1/forbidden
       ```
     - Click **Send**.
     - You should see a response with status code **403** and the JSON body:
       ```json
       {"error":"Forbidden"}
       ```
     - This confirms that the error handler for forbidden access is working correctly in Postman.

### Note
**Make sure to terminate the server (using `CTRL+C` in the terminal) between tasks.** This prevents the port (`5000`) from being busy and ensures the new instance of the server starts correctly.

</details>


<details>
<summary><strong>Task 3: Auth Class</strong></summary>

This task involves creating a new `Auth` class in `api/v1/auth/auth.py` to manage the API's authentication system. The class serves as a template for all future authentication systems.

### Step-by-Step Instructions

1. **Create the Required Folder and Files:**
   - Create the `auth` folder inside `api/v1`:
     ```bash
     mkdir -p api/v1/auth
     ```
   - Create an empty `__init__.py` file inside `api/v1/auth`:
     ```bash
     touch api/v1/auth/__init__.py
     ```
   - Create the `auth.py` file inside `api/v1/auth`:
     ```bash
     touch api/v1/auth/auth.py
     ```

2. **Implement the `Auth` Class:**
   - File `api/v1/auth/auth.py:

   ```python
   #!/usr/bin/env python3
   """
   This module contains the Auth class for managing API authentication.
   """
   from flask import request
   from typing import List, TypeVar

   class Auth:
       """Auth class to manage the API authentication."""

       def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
           """This determines if a given path requires authentication."""
           return False

       def authorization_header(self, request=None) -> str:
           """Returns the authorization header from the request."""
           return None

       def current_user(self, request=None) -> TypeVar('User'):
           """Returns the current user."""
           return None
   ```

3. **Test the `Auth` Class:**

   - Use `main_0.py`:

   ```python
   #!/usr/bin/env python3
   """ Main 0
   """
   from api.v1.auth.auth import Auth

   a = Auth()

   print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
   print(a.authorization_header())
   print(a.current_user())
   ```

4. **Ensure `main_0.py` is Executable:**

   - To ensure that you can run the script from the command line, you need to make it executable:
     ```bash
     chmod +x main_0.py
     ```

5. **Run the Script to Test the `Auth` Class:**

   - Execute the script to test the `Auth` class:
     ```bash
     ./main_0.py
     ```

   - The expected output should be:
     ```
     False
     None
     None
     ```

### Testing

- **Using `curl` in the Terminal:**
  - Open a new terminal and use the following `curl` commands to test the endpoints:

   ```bash
   curl "http://localhost:5000/api/v1/status"
   ```
   - Expected output:
   ```json
   {"status":"OK"}
   ```

   - To test the unauthorized endpoint:
   ```bash
   curl "http://localhost:5000/api/v1/unauthorized"
   ```
   - Expected output:
   ```json
   {"error":"Unauthorized"}
   ```

- **Using a Web Browser:**
   - Open your web browser (e.g., Chrome, Firefox, Safari).
   - In the address bar, type the following URL and press Enter:
     ```
     http://localhost:5000/api/v1/status
     ```
   - The browser should display the following JSON response:
     ```json
     {"status":"OK"}
     ```
   - To test the unauthorized endpoint, type:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
   - The browser should display:
     ```json
     {"error":"Unauthorized"}
     ```

- **Using Postman:**
  1. Open Postman and create a new request.
  2. Set the request method to `GET`.
  3. Enter the URL for the status endpoint:
     ```
     http://localhost:5000/api/v1/status
     ```
  4. Click **Send**. You should see a response similar to:
     ```json
     {"status":"OK"}
     ```
  5. To test the unauthorized endpoint, change the URL to:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
  6. Click **Send** again. The expected response should be:
     ```json
     {"error":"Unauthorized"}
     ```

### Explanation

- The `Auth` class contains three public methods that will form the basis for future authentication tasks:
  - **`require_auth`**: Checks if a given path requires authentication (currently always returns `False`).
  - **`authorization_header`**: Retrieves the `Authorization` header from the Flask request object (currently returns `None`).
  - **`current_user`**: Retrieves the current user (currently returns `None`).

### Note

Make sure to terminate the server between tasks to avoid any issues with the port being busy or the old configuration being used. To stop the server, use `CTRL+C` in the terminal where the server is running.

</details>


<details>
<summary><strong>Task 4: Define which routes don't need authentication</strong></summary>

This task involves updating the `require_auth` method in the `Auth` class to determine if a given path requires authentication by comparing it against a list of excluded paths.

### Step-by-Step Instructions

1. **Update the `require_auth` Method:**
   - File `api/v1/auth/auth.py`:

   ```python
   def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
       """This determines if a given path requires authentication."""
       if path is None or excluded_paths is None or not excluded_paths:
           return True

       # Normalize path to ensure it ends with a '/'
       if not path.endswith('/'):
           path += '/'

       # Check if the path is in excluded_paths
       if path in excluded_paths:
           return False

       return True
   ```

2. **Test the `require_auth` Method:**

   - Use `main_1.py`:

   ```python
   #!/usr/bin/env python3
   """ Main 1
   """
   from api.v1.auth.auth import Auth

   a = Auth()

   print(a.require_auth(None, None))
   print(a.require_auth(None, []))
   print(a.require_auth("/api/v1/status/", []))
   print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
   print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
   print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
   print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
   ```

3. **Ensure `main_1.py` is Executable:**

   - To ensure that you can run the script from the command line, make it executable:
     ```bash
     chmod +x main_1.py
     ```

4. **Run the Script to Test the Updated Method:**

   - Execute the script to test the updated `require_auth` method:
     ```bash
     ./main_1.py
     ```

   - The expected output should be:
     ```
     True
     True
     True
     False
     False
     True
     True
     ```

### Testing

- **Using `curl` in the Terminal:**
  - Open a new terminal and use the following `curl` commands to test the endpoints:

   ```bash
   curl "http://localhost:5000/api/v1/status"
   ```
   - Expected output:
   ```json
   {"status":"OK"}
   ```

   - To test the unauthorized endpoint:
   ```bash
   curl "http://localhost:5000/api/v1/unauthorized"
   ```
   - Expected output:
   ```json
   {"error":"Unauthorized"}
   ```

- **Using a Web Browser:**
   - Open your web browser (e.g., Chrome, Firefox, Safari).
   - In the address bar, type the following URL and press Enter:
     ```
     http://localhost:5000/api/v1/status
     ```
   - The browser should display the following JSON response:
     ```json
     {"status":"OK"}
     ```
   - To test the unauthorized endpoint, type:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
   - The browser should display:
     ```json
     {"error":"Unauthorized"}
     ```

- **Using Postman:**
  1. Open Postman and create a new request.
  2. Set the request method to `GET`.
  3. Enter the URL for the status endpoint:
     ```
     http://localhost:5000/api/v1/status
     ```
  4. Click **Send**. You should see a response similar to:
     ```json
     {"status":"OK"}
     ```
  5. To test the unauthorized endpoint, change the URL to:
     ```
     http://localhost:5000/api/v1/unauthorized
     ```
  6. Click **Send** again. The expected response should be:
     ```json
     {"error":"Unauthorized"}
     ```

### Explanation

- The updated `require_auth` method checks if:
  - `path` is `None` or `excluded_paths` is `None` or empty, and returns `True` (authentication required).
  - Normalizes `path` to ensure it ends with a `/`.
  - If the normalized `path` is in `excluded_paths`, it returns `False` (no authentication required).
  - If none of these conditions are met, it returns `True` (authentication required).

### Note

Make sure to terminate the server between tasks to avoid any issues with the port being busy or the old configuration being used. To stop the server, use `CTRL+C` in the terminal where the server is running.

</details>


<details>
<summary><strong>Task 5: Request Validation</strong></summary>

This task secures the API by validating all incoming requests, ensuring that only authorized requests can access specific resources. The authentication logic is dynamically set up based on the `AUTH_TYPE` environment variable.

### Step-by-Step Instructions

1. **Update the `authorization_header` Method in `Auth` Class:**

   ```python
   def authorization_header(self, request=None) -> str:
       """Returns the authorization header from the request."""
       if request is None or 'Authorization' not in request.headers:
           return None
       return request.headers['Authorization']
   ```

2. **Update `api/v1/app.py` to Validate Requests:**

   - Open `api/v1/app.py` and make the following changes:
     - Define a variable `auth` initialized to `None`.
     - Use the `AUTH_TYPE` environment variable to determine the type of authentication to use.
     - Implement the `before_request` method to filter each request.

   **Updated `app.py` code:**
   ```python
   auth = None
   AUTH_TYPE = getenv("AUTH_TYPE")

   if AUTH_TYPE == 'auth':
       from api.v1.auth.auth import Auth
       auth = Auth()

   @app.before_request
   def before_request_handler():
       """Before request handler to filter each request."""
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
       if auth.current_user(request) is None:
           abort(403)
   ```

3. **Run the Server with the Correct Environment Variable:**

   - Open a terminal and run the server with the `AUTH_TYPE` environment variable set:
     ```bash
     API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
     ```

4. **Test the Request Validation Using `curl`:**

   - In another terminal, use `curl` to test the various endpoints:

   ```bash
   curl "http://localhost:5000/api/v1/status"
   # Expected output: {"status": "OK"}

   curl "http://localhost:5000/api/v1/status/"
   # Expected output: {"status": "OK"}

   curl "http://localhost:5000/api/v1/users"
   # Expected output: {"error": "Unauthorized"}

   curl "http://localhost:5000/api/v1/users" -H "Authorization: Test"
   # Expected output: {"error": "Forbidden"}
   ```

5. **Test the Request Validation Using Postman:**

   - Open Postman and create a new **GET** request:
     - **URL**: `http://localhost:5000/api/v1/status`
   - Click **Send**.
   - You should see a JSON response:
     ```json
     {
       "status": "OK"
     }
     ```

   - Test the endpoint that requires authentication:
     - **URL**: `http://localhost:5000/api/v1/users`
     - Click **Send** without any headers.
   - You should see a JSON response:
     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **To Test the `Forbidden` Response:**
     1. In Postman, add a new header:
        - **Key**: `Authorization`
        - **Value**: `Test`
     2. Click **Send**.
     3. You should see the following JSON response:
     ```json
     {
       "error": "Forbidden"
     }
     ```

6. **Test the Request Validation in the Browser:**

   - Open your web browser and navigate to the following URL:
     ```
     http://localhost:5000/api/v1/status/
     ```
   - You should see a JSON response similar to:
     ```json
     {
       "status": "OK"
     }
     ```

   - Next, test an endpoint that requires authentication by navigating to:
     ```
     http://localhost:5000/api/v1/users
     ```
   - You should see a JSON response similar to:
     ```json
     {
       "error": "Unauthorized"
     }
     ```

   - **To Test the `Forbidden` Response in the Browser:**
     1. Install a browser extension like **ModHeader** (available for Chrome and Firefox) or any other HTTP header modification tool.
     2. Open the extension (e.g., **ModHeader**).
     3. Add a new header:
        - **Name**: `Authorization`
        - **Value**: `Test`
     4. Navigate to:
        ```
        http://localhost:5000/api/v1/users
        ```
     5. You should see the following JSON response:
     ```json
     {
       "error": "Forbidden"
     }
     ```

### Explanation

- **Request Validation Logic:**
  - **Check for `auth`:** If `auth` is `None`, do nothing.
  - **Check Path:** If the request path does not require authentication, do nothing.
  - **Check Authorization Header:** If the `Authorization` header is missing, return a 401 error.
  - **Check Current User:** If the user is not authenticated, return a 403 error.

### Note

Make sure to terminate the server between tasks to avoid any issues with the port being busy or the old configuration being used.

</details>



<details>
<summary><strong>Task 6: Basic Authentication</strong></summary>

This task involves creating a new authentication class, `BasicAuth`, which inherits from `Auth`. The class will be used to manage basic authentication for the API.

### Step-by-Step Instructions

1. **Create the `BasicAuth` Class:**
   - File `api/v1/auth/basic_auth.py`.
   - Inside `basic_auth.py`, a new class `BasicAuth` is defined that inherits from `Auth`:

   ```python
   #!/usr/bin/env python3
   """Basic authentication module for the API."""

   from api.v1.auth.auth import Auth

   class BasicAuth(Auth):
       """BasicAuth class that inherits from Auth."""
       pass
   ```

2. **Update `api/v1/app.py` to Use `BasicAuth`:**
  
   ```python
   auth = None
   AUTH_TYPE = getenv("AUTH_TYPE")

   if AUTH_TYPE == 'auth':
       from api.v1.auth.auth import Auth
       auth = Auth()
   elif AUTH_TYPE == 'basic_auth':
       from api.v1.auth.basic_auth import BasicAuth
       auth = BasicAuth()
   ```

3. **Run the Server with the Correct Environment Variable:**
   - Run the server with `AUTH_TYPE` set to `basic_auth`:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

4. **Test the Basic Authentication Using `curl`:**
   - Use `curl` commands to test the different endpoints:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   # Expected output: {"status": "OK"}

   curl "http://0.0.0.0:5000/api/v1/status/"
   # Expected output: {"status": "OK"}

   curl "http://0.0.0.0:5000/api/v1/users"
   # Expected output: {"error": "Unauthorized"}

   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
   # Expected output: {"error": "Forbidden"}
   ```

5. **Test Basic Authentication in the Browser:**

   - Follow the steps mentioned in previous tasks to use the **ModHeader** extension to add the `Authorization` header:
     - **Name:** `Authorization`
     - **Value:** `Test`
   - Navigate to:
     ```
     http://localhost:5000/api/v1/users
     ```
   - You should see the following JSON response:
     ```json
     {
       "error": "Forbidden"
     }
     ```

6. **Test Basic Authentication Using Postman:**

   - **Open Postman:**
     - Launch the Postman application on your computer.
   - **Create a New Request:**
     - Click on the "New" button or select "Request" to create a new HTTP request.
   - **Set the Request Method and URL:**
     - Set the request method to **GET**.
     - Enter the URL:
       ```
       http://localhost:5000/api/v1/users
       ```
   - **Add the Authorization Header:**
     - Go to the **Headers** tab in Postman.
     - Add a new header with:
       - **Key:** `Authorization`
       - **Value:** `Test`
   - **Send the Request:**
     - Click the "Send" button to send the request to the server.
   - **Check the Response:**
     - You should see a JSON response indicating a "Forbidden" error:
     ```json
     {
       "error": "Forbidden"
     }
     ```

### Explanation

- **Dynamic Authentication Setup:** Depending on the value of the `AUTH_TYPE` environment variable, the server uses either `Auth` or `BasicAuth` for request validation.

- **Request Handling Logic:**
  - **`auth` Variable:** Initialized to `None` and dynamically assigned based on the environment variable `AUTH_TYPE`.
  - **`BasicAuth` Class:** Inherits from `Auth` and will later be expanded to handle basic authentication mechanisms.

### Note

- **Remember to Terminate the Server Between Tasks:**  
  To avoid any issues with the port being busy or the old configuration being used, make sure to terminate the server before starting the next task.

</details>



<details>
<summary><strong>Task 7: Basic - Base64 part</strong></summary>

This task involves adding the method `extract_base64_authorization_header` in the `BasicAuth` class to extract the Base64 part of the Authorization header for Basic Authentication.

### Step-by-Step Instructions

1. **Implement the `extract_base64_authorization_header` Method:**


   ```python
   #!/usr/bin/env python3
   """This module contains Basic authentication for the API."""

   from api.v1.auth.auth import Auth


   class BasicAuth(Auth):
       """BasicAuth class that inherits from Auth."""

       def extract_base64_authorization_header(
           self, authorization_header: str
       ) -> str:
           """
           Extracts the Base64 part of the Authorization header for Basic Auth.
           """
           if authorization_header is None or not isinstance(
               authorization_header, str
           ):
               return None
           if not authorization_header.startswith("Basic "):
               return None
           return authorization_header[len("Basic "):]
   ```

2. **Test the `extract_base64_authorization_header` Method:**

   - Use `main_2.py`:

   ```python
   #!/usr/bin/env python3
   """ Main 2
   """
   from api.v1.auth.basic_auth import BasicAuth

   a = BasicAuth()

   print(a.extract_base64_authorization_header(None))
   print(a.extract_base64_authorization_header(89))
   print(a.extract_base64_authorization_header("Holberton School"))
   print(a.extract_base64_authorization_header("Basic Holberton"))
   print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
   print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
   print(a.extract_base64_authorization_header("Basic1234"))
   ```

3. **Ensure  `main_2.py` is Executable:**

   - Make the script executable to run it from the command line:
     ```bash
     chmod +x main_2.py
     ```

4. **Run the Script to Test the `BasicAuth` Class:**

   - Execute the script to test the `extract_base64_authorization_header` method:
     ```bash
     ./main_2.py
     ```

   - The expected output should be:
     ```
     None
     None
     None
     Holberton
     SG9sYmVydG9u
     SG9sYmVydG9uIFNjaG9vbA==
     None
     ```

### Testing with Postman, `curl`, and Web Browser

#### **Testing with `curl` Commands:**

   - To test the method in the context of an API, use the following `curl` commands:

   ```bash
   curl -H "Authorization: Basic SG9sYmVydG9u" "http://0.0.0.0:5000/api/v1/users"
   # Expected output: {"error": "Unauthorized"}

   curl -H "Authorization: Basic SG9sYmVydG9uIFNjaG9vbA==" "http://0.0.0.0:5000/api/v1/users"
   # Expected output: {"error": "Forbidden"}
   ```

#### **Testing with a Web Browser:**

   - Use the **ModHeader** extension (or any HTTP header modification tool) to add an Authorization header:
     - **Name:** `Authorization`
     - **Value:** `Basic SG9sYmVydG9u`
   - Navigate to:
     ```
     http://localhost:5000/api/v1/users
     ```
   - You should see the JSON response:
   ```json
   {
     "error": "Unauthorized"
   }
   ```

   - Update the header value to `Basic SG9sYmVydG9uIFNjaG9vbA==` and refresh the page.
   - You should see the JSON response:
   ```json
   {
     "error": "Forbidden"
   }
   ```

#### **Testing with Postman:**

   - Open Postman and create a new request:
     - **Method:** GET
     - **URL:** `http://localhost:5000/api/v1/users`
   - Go to the **Headers** tab and add a new header:
     - **Key:** `Authorization`
     - **Value:** `Basic SG9sYmVydG9u`
   - Click **Send** to make the request.
   - You should see a JSON response:
   ```json
   {
     "error": "Unauthorized"
   }
   ```

   - Update the **Authorization** header value to `Basic SG9sYmVydG9uIFNjaG9vbA==`.
   - Click **Send** again to make the request.
   - You should see a JSON response:
   ```json
   {
     "error": "Forbidden"
   }
   ```

### Explanation

- **Method Behavior:**  
  The `extract_base64_authorization_header` method extracts the Base64 part of the Authorization header if it starts with "Basic ".
  - Returns `None` if the input is `None`, not a string, or does not start with "Basic ".
  - Returns the Base64 part of the header if it is correctly formatted.

### Note

- **Terminate the Server Between Tasks:**  
  Remember to terminate the server between tasks to avoid any issues with the port being busy or the old configuration being used.

</details>


<details>
<summary><strong>Task 8: Basic - Base64 Decode</strong></summary>

This task involves adding a method to the `BasicAuth` class that decodes a Base64-encoded string to its UTF-8 representation. The method will handle different cases, such as invalid inputs or non-Base64 strings.

### Step-by-Step Instructions

1. **Update the `BasicAuth` Class:**


   ```python
   def decode_base64_authorization_header(
       self, base64_authorization_header: str
   ) -> str:
       """
       Decodes a Base64 string to its UTF-8 representation.
       """
       if base64_authorization_header is None or not isinstance(
           base64_authorization_header, str
       ):
           return None
       try:
           base64_bytes = base64_authorization_header.encode('utf-8')
           decoded_bytes = base64.b64decode(base64_bytes)
           return decoded_bytes.decode('utf-8')
       except Exception:
           return None
   ```

2. **Test the `decode_base64_authorization_header` Method:**

   - Use `main_3.py`t:

   ```python
   #!/usr/bin/env python3
   """ Main 3
   """
   from api.v1.auth.basic_auth import BasicAuth

   a = BasicAuth()

   print(a.decode_base64_authorization_header(None))
   print(a.decode_base64_authorization_header(89))
   print(a.decode_base64_authorization_header("Holberton School"))
   print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
   print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
   print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))
   ```

3. **Ensure `main_3.py` is Executable:**

   - Make the script executable to run it from the command line:
     ```bash
     chmod +x main_3.py
     ```

4. **Run the Script to Test the Method:**

   - Execute the script to test the `decode_base64_authorization_header` method:
     ```bash
     ./main_3.py
     ```

   - The expected output should be:
     ```
     None
     None
     None
     Holberton
     Holberton School
     Holberton School
     ```

5. **Test Using `curl`, Postman, or Web Browser:**

   - These tools do not apply for this task, as it involves a backend method that doesn't directly interact with HTTP requests.


### Explanation

- **`decode_base64_authorization_header` Method:**
  - This method decodes a Base64 string to a UTF-8 string. It handles several edge cases:
    - Returns `None` if the input is `None` or not a string.
    - Returns `None` if the input is not a valid Base64 string.
    - Otherwise, it decodes the Base64 string and returns its UTF-8 representation.


</details>

<details>
<summary><strong>Task 10: Basic - User Object</strong></summary>

This task involves adding a method to the `BasicAuth` class that returns a `User` instance based on the provided email and password credentials.

### Step-by-Step Instructions

1. **Update the `BasicAuth` Class:**

   - Open the file `api/v1/auth/basic_auth.py` and add the `user_object_from_credentials` method:

   ```python
   def user_object_from_credentials(
           self, user_email: str, user_pwd: str) -> TypeVar('User'):
       """
       Returns the User instance based on the user's email and password.
       """
       if user_email is None or not isinstance(user_email, str):
           return None
       if user_pwd is None or not isinstance(user_pwd, str):
           return None

       try:
           from models.user import User
           users = User.search({'email': user_email})
       except Exception:
           return None

       if not users:
           return None

       for user in users:
           if user.is_valid_password(user_pwd):
               return user
       return None
   ```

2. **Test File:**

   -  Use `main_5.py`:

   ```python
   #!/usr/bin/env python3
   """ Main 5
   """
   import uuid
   from api.v1.auth.basic_auth import BasicAuth
   from models.user import User

   """ Create a user test """
   user_email = str(uuid.uuid4())
   user_clear_pwd = str(uuid.uuid4())
   user = User()
   user.email = user_email
   user.first_name = "Bob"
   user.last_name = "Dylan"
   user.password = user_clear_pwd
   print("New user: {}".format(user.display_name()))
   user.save()

   """ Retrieve this user via the class BasicAuth """
   a = BasicAuth()

   u = a.user_object_from_credentials(None, None)
   print(u.display_name() if u is not None else "None")

   u = a.user_object_from_credentials(89, 98)
   print(u.display_name() if u is not None else "None")

   u = a.user_object_from_credentials("email@notfound.com", "pwd")
   print(u.display_name() if u is not None else "None")

   u = a.user_object_from_credentials(user_email, "pwd")
   print(u.display_name() if u is not None else "None")

   u = a.user_object_from_credentials(user_email, user_clear_pwd)
   print(u.display_name() if u is not None else "None")
   ```

3. **Make `main_5.py` Executable:**

   - To ensure that you can run the script from the command line, make it executable:

   ```bash
   chmod +x main_5.py
   ```

4. **Run the Script to Test the Method:**

   - Execute the script to test the `user_object_from_credentials` method:

   ```bash
   ./main_5.py
   ```

   - The expected output should be:

   ```plaintext
   New user: Bob Dylan
   None
   None
   None
   None
   Bob Dylan
   ```

### Explanation

- The `user_object_from_credentials` method:
  - **Validates Input:** Returns `None` if `user_email` or `user_pwd` is `None` or not a string.
  - **Searches for the User:** Searches for a `User` instance by email using the `User.search` method.
  - **Checks the Password:** Returns `None` if no user is found or if the password is incorrect.
  - **Returns User Instance:** Otherwise, it returns the `User` instance.

### Testing with `curl`, Postman, and Web Browser:

**Note:** This task involves backend logic that does not directly affect any endpoint, so there is no need for specific `curl` commands, Postman tests, or web browser interactions. The testing should be performed using the Python script `main_5.py`.

</details>

<details>
<summary><strong>Task 11: Basic - Overload current_user - and BOOM!</strong></summary>

This task involves overloading the `current_user` method in the `BasicAuth` class to retrieve the `User` instance for a given request. This will fully implement Basic Authentication for the API.

### Step-by-Step Instructions

1. **Update the `BasicAuth` Class:**

   - Open `api/v1/auth/basic_auth.py` and add the `current_user` method:

   ```python
   def current_user(self, request=None) -> TypeVar('User'):
       """
       Retrieves the User instance for a given request.
       """
       auth_header = self.authorization_header(request)
       if auth_header is None:
           return None

       base64_header = self.extract_base64_authorization_header(auth_header)
       if base64_header is None:
           return None

       decoded_header = self.decode_base64_authorization_header(base64_header)
       if decoded_header is None:
           return None

       user_email, user_pwd = self.extract_user_credentials(decoded_header)
       if user_email is None or user_pwd is None:
           return None

       return self.user_object_from_credentials(user_email, user_pwd)
   ```

2. ** Test File:**

   - Use `main_6.py`:

   ```python
   #!/usr/bin/env python3
   """ Main 6
   """
   import base64
   from api.v1.auth.basic_auth import BasicAuth
   from models.user import User

   """ Create a user test """
   user_email = "bob@hbtn.io"
   user_clear_pwd = "H0lbertonSchool98!"
   user = User()
   user.email = user_email
   user.password = user_clear_pwd
   print("New user: {} / {}".format(user.id, user.display_name()))
   user.save()

   basic_clear = "{}:{}".format(user_email, user_clear_pwd)
   print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
   ```

3. **Make `main_6.py` Executable:**

   - To ensure that you can run the script from the command line, make it executable:

   ```bash
   chmod +x main_6.py
   ```

4. **Run the Script to Create a User and Generate Base64 Credentials:**

   - Execute the script:

   ```bash
   ./main_6.py
   ```

   - The expected output should be:

   ```plaintext
   New user: <user_id> / bob@hbtn.io
   Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
   ```

5. **Run the Server with the Correct Environment Variable:**

   - Start the API server with `AUTH_TYPE` set to `basic_auth`:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

6. **Test the Basic Authentication Using `curl`:**

   - Use `curl` commands to test the endpoints:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   # Expected output: {"status": "OK"}

   curl "http://0.0.0.0:5000/api/v1/users"
   # Expected output: {"error": "Unauthorized"}

   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
   # Expected output: {"error": "Forbidden"}

   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
   # Expected output: {"error": "Forbidden"}

   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
   # Expected output: User details in JSON format.
   ```

   - **Result:** The output from the `curl` command should look similar to this:
   
   ```json
   [
     {
       "created_at": "2024-09-15T20:19:46",
       "email": "bob@hbtn.io",
       "first_name": null,
       "id": "9b162846-34a8-425e-914b-f6e35ca26162",
       "last_name": null,
       "updated_at": "2024-09-15T20:19:46"
     }
   ]
   ```

7. **Test Basic Authentication in Postman:**

   - Open Postman and create a new request.
   - Set the request type to **GET**.
   - Enter the request URL:
     ```
     http://localhost:5000/api/v1/users
     ```
   - Under the **Authorization** tab:
     - Choose **Basic Auth** as the type.
     - Enter the **Username** as `bob@hbtn.io` and **Password** as `H0lbertonSchool98!`.
   - Click **Send**.
   - The expected output should be the user details in JSON format:

   ```json
   [
     {
       "created_at": "2024-09-15T20:19:46",
       "email": "bob@hbtn.io",
       "first_name": null,
       "id": "9b162846-34a8-425e-914b-f6e35ca26162",
       "last_name": null,
       "updated_at": "2024-09-15T20:19:46"
     }
   ]
   ```

8. **Test Basic Authentication in the Browser:**

   - Follow the steps mentioned in previous tasks to use the **ModHeader** extension to add the `Authorization` header:
     - **Name:** `Authorization`
     - **Value:** `Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh`
   - Navigate to:
     ```
     http://localhost:5000/api/v1/users
     ```
   - You should see the JSON response with user details.

### Explanation

- The `current_user` method performs the following tasks:
  - **Uses Helper Methods:** Leverages existing methods like `authorization_header`, `extract_base64_authorization_header`, `decode_base64_authorization_header`, `extract_user_credentials`, and `user_object_from_credentials` to validate the request and retrieve the authenticated user.
  - **Returns User Instance:** Returns the `User` instance associated with the request if authentication is successful.

### Note

- **Remember to Terminate the Server Between Tasks:**  
  To avoid any issues with the port being busy or the old configuration being used, make sure to terminate the server before starting the next task.

</details>

