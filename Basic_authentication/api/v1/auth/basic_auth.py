#!/usr/bin/env python3
"""This module contains Basic authentication for the API."""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Auth.
        """
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64 string to its UTF-8 representation.
        """
        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
