#!/usr/bin/env python3
"""
This module contains the view for handling Session Authentication
routes in the API. It provides login and logout routes that create,
manage, and destroy session IDs for authenticated users.
"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """POST /api/v1/auth_session/login
    Creates a new session for a user.
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
