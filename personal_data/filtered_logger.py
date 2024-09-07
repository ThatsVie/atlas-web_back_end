#!/usr/bin/env python3
'''
This module contains functions and classes for filtering log messages,
creating loggers that redact sensitive information, and connecting securely
to a MySQL database.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations
import os  # For environment variable access
import mysql.connector  # For connecting to the MySQL database
from mysql.connector import Error  # For handling MySQL errors


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
        Formats the log record, redacting specified fields.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


# Define a tuple containing fields considered as PII in user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logger named user_data that logs up to INFO level,
    does not propagate to other loggers, and uses a StreamHandler with
    RedactingFormatter to format log records.
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Connects to a secure MySQL database using credentials from environment
    variables and returns a MySQLConnection object.
    '''
    # Check for missing environment variables
    if not all([os.getenv("PERSONAL_DATA_DB_USERNAME"),
                os.getenv("PERSONAL_DATA_DB_PASSWORD"),
                os.getenv("PERSONAL_DATA_DB_HOST"),
                os.getenv("PERSONAL_DATA_DB_NAME")]):
        raise ValueError("Some required environment variables are missing.")

    try:
        # Create a MySQL database connection using environment variables
        connector = mysql.connector.connect(
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            database=os.getenv("PERSONAL_DATA_DB_NAME")
        )
        return connector
    except Error as e:
        # For MySQL connection errors
        print(f"Error connecting to MySQL: {e}")
        return None
