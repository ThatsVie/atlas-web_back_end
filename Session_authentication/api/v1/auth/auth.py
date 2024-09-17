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
        """
        if request is None:
            return None

        cookie_name = getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(cookie_name)
