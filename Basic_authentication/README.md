# Basic Authentication

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

</details>

