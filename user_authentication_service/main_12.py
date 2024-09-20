#!/usr/bin/env python3
"""
Main file to test Auth.get_user_from_session_id
"""
from auth import Auth

auth = Auth()

# Assume user has already logged in and session ID is generated
email = 'bob@bob.com'
password = 'MyPwdOfBob'

# Register and create a session
auth.register_user(email, password)
session_id = auth.create_session(email)

# Retrieve user from session ID
print(auth.get_user_from_session_id(session_id))  # Should print the user object

# Test invalid session ID
print(auth.get_user_from_session_id("invalid_session_id"))  # Should print None

# Test None session ID
print(auth.get_user_from_session_id(None))  # Should print None
