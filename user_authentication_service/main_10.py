#!/usr/bin/env python3
"""
Main file to test Auth.create_session
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))  # Expected output: A valid UUID (session ID)
print(auth.create_session("unknown@email.com"))  # Expected output: None
