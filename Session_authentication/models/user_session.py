#!/usr/bin/env python3
"""
This module contains UserSession for storing session information in a database
"""
from models.base import Base
from datetime import datetime


class UserSession(Base):
    """UserSession class for storing session data."""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a UserSession instance."""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        self.created_at = kwargs.get('created_at', datetime.now())
