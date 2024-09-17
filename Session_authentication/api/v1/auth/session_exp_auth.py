#!/usr/bin/env python3
"""
This module contains the SessionExpAuth class that adds expiration
functionality to session-based authentication.
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class for handling session authentication with expiration.
    """

    def __init__(self):
        """Initialize SessionExpAuth with session duration."""
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session with expiration."""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Store session information with expiration
        session_info = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_info
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return a User ID based on a Session ID with expiration check."""
        if session_id is None:
            return None

        session_info = self.user_id_by_session_id.get(session_id)
        if session_info is None:
            return None

        if self.session_duration <= 0:
            return session_info.get('user_id')

        if 'created_at' not in session_info:
            return None

        # Check if session has expired
        created_at = session_info.get('created_at')
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return session_info.get('user_id')
