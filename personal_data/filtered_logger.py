#!/usr/bin/env python3
'''
This module contains functions and classes for filtering log messages and
creating loggers that redact sensitive information.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.
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
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record and redacts specified fields.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


# Define a tuple containing fields considered as PII in user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logger named "user_data" that logs up to INFO level,
    does not propagate to other loggers, and uses a StreamHandler with
    RedactingFormatter to format log records.
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Prevent the logger from propagating messages

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
