#!/usr/bin/env python3
'''
This module handles user authentication.
It provides:
User registration with duplicate email checks.
Password hashing using bcrypt for security.
'''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password, returns the User object.
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
