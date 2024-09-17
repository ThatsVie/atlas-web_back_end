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

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a given user_id."""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        # Store the user_id with the generated session_id
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value."""
        if request is None:
            return None

        # Retrieve session cookie value
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Retrieve the User instance from the database using the user ID
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session (logs out the user)."""
        if request is None:
            return False

        # Retrieve session cookie value
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Check if session ID is linked to any user ID
        if session_id not in self.user_id_by_session_id:
            return False

        # Delete the session ID
        del self.user_id_by_session_id[session_id]

        return True
