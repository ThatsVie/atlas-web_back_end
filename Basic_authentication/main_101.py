#!/usr/bin/env python3
""" Main 101
"""
from api.v1.auth.auth import Auth

a = Auth()

# Case: Path "/api/v1/users" is not in excluded_paths ["api/v1/stat*"]
print(a.require_auth("/api/v1/users", ["/api/v1/stat*"]))  # Expected: True

# Case: Path "/api/v1/status" matches excluded_paths pattern ["api/v1/stat*"]
print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))  # Expected: False

# Case: Path "/api/v1/stats" matches excluded_paths pattern ["api/v1/stat*"]
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))  # Expected: False

# Case: Path "/api/v1/users" matches exactly in excluded_paths ["/api/v1/users", "/api/v1/stat*"]
print(a.require_auth("/api/v1/users", ["/api/v1/users", "/api/v1/stat*"]))  # Expected: False

# Additional Checks to ensure robustness
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))  # Expected: False
print(a.require_auth("/api/v1/stats", ["/api/v1/stats/"]))  # Expected: False
