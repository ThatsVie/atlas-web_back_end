#!/usr/bin/env python3
'''
This module contains a function for filtering log messages and a formatter
class that redacts sensitive information in log records.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): A list of strings representing all fields to
                            obfuscate.
        redaction (str): A string representing the text to replace each field
                         value.
        message (str): A string representing the log line.
        separator (str): A string representing the character that separates
                         fields in the log line.

    Returns:
        str: A string with specified fields obfuscated.
    '''
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )


class RedactingFormatter(logging.Formatter):
    '''
    Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Initializes the formatter with the specified fields to redact.

        Args:
            fields (List[str]): A list of strings representing the fields to
                                obfuscate.
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log record as a string.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)
