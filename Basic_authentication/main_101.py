#!/usr/bin/env python3
""" Main 101
"""
from api.v1.auth.auth import Auth

a = Auth()

# Test cases to match the checker's expectations
print(a.require_auth("/api/v1/users", ["/api/v1/us*"]))  # Expected: False
print(a.require_auth("/api/v1/us", ["/api/v1/us*"]))     # Expected: False
print(a.require_auth("/api/v1/us/", ["/api/v1/us*"]))    # Expected: False
print(a.require_auth("/api/v1/uas", ["/api/v1/us*"]))    # Expected: True
print(a.require_auth("/api/v1/usual", ["/api/v1/us*"]))  # Expected: False
