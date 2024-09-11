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
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user."""
        return None
