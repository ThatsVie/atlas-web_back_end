#!/usr/bin/env python3
"""
Main file for testing Auth.update_password
"""

from auth import Auth

# Initialize Auth
auth = Auth()

# Register a new user
email = "bob@bob.com"
password = "SuperSecurePwd"
user = auth.register_user(email, password)

# Generate a reset token
reset_token = auth.get_reset_password_token(email)
print(f"Generated reset token: {reset_token}")

# Test updating the password
try:
    auth.update_password(reset_token, "NewSuperSecurePwd")
    print("Password updated successfully")
except ValueError as e:
    print(f"Error updating password: {e}")

# Try updating the password with an invalid token
try:
    auth.update_password("invalid_token", "NewSuperSecurePwd")
except ValueError as e:
    print(f"Expected error: {e}")
