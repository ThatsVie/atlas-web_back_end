#!/usr/bin/env python3
"""
Main file to test Auth.destroy_session
"""
from auth import Auth

auth = Auth()

# Assume user has already logged in and session ID is generated
email = 'bob@bob.com'
password = 'MyPwdOfBob'

# Register and create a session
user = auth.register_user(email, password)
session_id = auth.create_session(email)

# Verify that user is logged in with a valid session ID
print(auth.get_user_from_session_id(session_id))  # Should print the user object

# Destroy the session
auth.destroy_session(user.id)

# Verify that the session is destroyed
print(auth.get_user_from_session_id(session_id))  # Should print None
