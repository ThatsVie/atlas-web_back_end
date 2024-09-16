#!/usr/bin/env python3
"""
This module contains the Auth class for managing API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if a given path requires authentication."""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize path to compare with excluded paths
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                # Match the path prefix with excluded path
                if normalized_path.startswith(excluded_path[:-1]):
                    return False
            elif normalized_path == excluded_path:
                # Exact match with no wildcard
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
