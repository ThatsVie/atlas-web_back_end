#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
- User registration with duplicate email checks.
- Password hashing using bcrypt for security.
- Credentials validation to authenticate users.
- Generates UUIDs for unique user identification.
- Creates session IDs for user authentication.
- Retrieves users based on session IDs.
- Destroys user sessions by setting session ID to None.
'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        '''
        Creates a new session ID for a user based on their email.
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''
        Retrieves a user from the session ID.
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''
        Destroys a user session by setting the session ID to None.
        '''
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass
