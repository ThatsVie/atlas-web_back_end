#!/usr/bin/env python3
'''
This module contains a function for securely hashing passwords
using the bcrypt package.
'''

import bcrypt  # For password hashing


def hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt with a salt.

    Args:
        password (str): The plain text password to be hashed.

    Returns:
        bytes: A salted, hashed password as a byte string.
    '''
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
