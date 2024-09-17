#!/usr/bin/env python3
"""
This module contains SessionDBAuth class for handling session authentication
with database storage.
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta

class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class for session management stored in database."""
    
    def create_session(self, user_id=None):
        """Create and store a new session instance in the database."""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Create a new UserSession instance and store it in the database
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the User ID associated with a session ID, considering expiration."""
        if session_id is None:
            return None
        
        # Search for UserSession in the database
        try:
            user_sessions = UserSession.search({'session_id': session_id})
            if not user_sessions:
                return None
            user_session = user_sessions[0]

            # Check if the session has expired
            if self.session_duration <= 0:
                return user_session.user_id

            if not hasattr(user_session, 'created_at'):
                return None

            created_at = user_session.created_at
            if created_at + timedelta(seconds=self.session_duration) < datetime.now():
                user_session.remove()  # Remove expired session from the database
                return None

            return user_session.user_id
        except Exception:
            return None

    def destroy_session(self, request=None):
        """Destroy a UserSession based on the session ID."""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Search for UserSession in the database
        try:
            user_sessions = UserSession.search({'session_id': session_id})
            if not user_sessions:
                return False
            user_session = user_sessions[0]
            user_session.remove()  # Remove session from the database
            return True
        except Exception:
            return False
