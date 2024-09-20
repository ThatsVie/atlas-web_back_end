#!/usr/bin/env python3
"""
Main file for testing task 16
"""
from auth import Auth

auth = Auth()

# Test user registration
email = "bob@bob.com"
password = "MyPwdOfBob"
auth.register_user(email, password)

# Generate reset password token
try:
    token = auth.get_reset_password_token(email)
    print(f"Reset token for {email}: {token}")
except ValueError as e:
    print(e)

# Test non-existing user
try:
    token = auth.get_reset_password_token("nonexistent@bob.com")
    print(f"Reset token: {token}")
except ValueError as e:
    print(e)
