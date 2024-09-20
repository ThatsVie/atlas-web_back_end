#!/usr/bin/env python3
'''
This module handles user authentication:
User registration with duplicate email checks.
Password hashing using bcrypt for security.
Credentials validation to authenticate users.
Session management for user login and logout.
Profile retrieval using session IDs.
Password reset functionality including token generation and validation.
Secure password update using reset tokens.
'''


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid4())


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
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''Creates a session ID for a user'''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''Finds the user corresponding to a session_id'''
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''Destroys a user's session'''
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        '''Generates a reset password token for a user'''
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            user.reset_token = reset_token
            self._db._session.commit()
            return reset_token
        except NoResultFound:
            raise ValueError(f"User {email} does not exist")

    def update_password(self, reset_token: str, password: str) -> None:
        '''Updates a user's password using the reset token'''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            user.hashed_password = hashed_password
            user.reset_token = None  # Clear the reset token after update
            self._db._session.commit()
        except NoResultFound:
            raise ValueError(f"Invalid reset token")
