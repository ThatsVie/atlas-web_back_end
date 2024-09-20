#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
User registration with duplicate email checks.
Password hashing using bcrypt for security.
Credentials validation to authenticate users.
Session management and reset password tokens.
'''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns its string representation
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
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password and create a new user
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
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Check if the password matches using bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        '''
        Creates a session for the user and returns the session ID
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''
        Retrieves a user based on the session ID
        '''
        if not session_id:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''
        Destroys a user's session by setting the session_id to None
        '''
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        '''
        Generates a reset password token for the user
        '''
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new UUID as reset token
            reset_token = _generate_uuid()
            # Update the user's reset_token field
            user.reset_token = reset_token
            self._db._session.commit()
            return reset_token
        except NoResultFound:
            raise ValueError(f"User {email} does not exist")
