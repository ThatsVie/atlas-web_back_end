#!/usr/bin/env python3
'''
This script provides statistics from the Nginx logs stored in MongoDB.
It displays the total number of logs, the count of each HTTP method,
and how many times GET requests were made to /status.
'''

from pymongo import MongoClient


def log_stats():
    ''' Prints Nginx logs statistics from MongoDB. '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of GET requests to /status
    status_check = collection.count_documents({"method":
                                              "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
