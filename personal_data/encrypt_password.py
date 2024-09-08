#!/usr/bin/env python3
'''
This module contains a function for securely hashing passwords
using the bcrypt package.
'''

import bcrypt  # For password hashing


def hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt with a salt.
    '''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
