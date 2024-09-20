#!/usr/bin/env python3
'''
This module sets up a basic Flask app with user registration, login,
session management, and profile retrieval functionality.
'''

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    '''Handles GET request and returns a JSON message'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    '''Handles user registration via POST /users route'''
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    '''Handles user login via POST /sessions route'''
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    # Create a session ID for the user
    session_id = AUTH.create_session(email)

    # Set the session_id as a cookie in the response
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    '''Handles user logout via DELETE /sessions route'''
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    # Destroy the user's session
    AUTH.destroy_session(user.id)

    # Redirect the user to the home page
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    '''Handles user profile retrieval via GET /profile route'''
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    # Return the user's email in the response
    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
