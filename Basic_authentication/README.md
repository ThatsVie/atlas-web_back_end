
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

**Important:**  
Between tasks, make sure to terminate the running server before starting a new one to test the next task. If you don't terminate the server, the port (`5000`) will be busy, and the new instance of the server will not start correctly. To stop the server, use `CTRL+C` in the terminal where the server is running.

<details>
<summary><strong>Task 0: Simple-basic-API</strong></summary>

### Description

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

5. **Test the API:**
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
     * HTTP 1.0, assume close after body
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
     - This confirms that the API server is running correctly and responding to HTTP GET requests.

![Screenshot 2024-09-10 164300](https://github.com/user-attachments/assets/b9fde9c9-05f8-4d07-9228-72609de2f789)

</details>

<details>
<summary><strong>Task 1: Error handler: Unauthorized</strong></summary>

### Description

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
       """ Not found handler
       """
       return jsonify({"error": "Not found"}), 404

   @app.errorhandler(401)
   def unauthorized(error) -> str:
       """ Unauthorized handler
       """
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
   """ Module of Index views
   """
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
     * HTTP 1.0, assume close after body
     < HTTP/1.0 401 UNAUTHORIZED
     < Content-Type: application/json
     < Content-Length: 25
     < Access-Control-Allow-Origin: *
     < Server: Werkzeug/1.0.1 Python/3.10.12
     < Date: Tue, 10 Sep 2024 20:59:56 GMT
     < 
     {"error":"Unauthorized"}
     * Closing connection 0
     ```

   - This confirms that the API server is running and the 401 error handler is working correctly.
    - **Using a Web Browser:**
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
   
![Screenshot 2024-09-10 164313](https://github.com/user-attachments/assets/4d9e2908-8b38-4194-872f-683949861ca3)


</details>

<details>
<summary><strong>Task 2: Error handler: Forbidden</strong></summary>

### Description

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
       * HTTP 1.0, assume close after body
       < HTTP/1.0 403 FORBIDDEN
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

</details>
