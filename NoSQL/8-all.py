#!/usr/bin/env python3
'''
This module contains function that lists all documents in MongoDB collection.
list_all connects to a MongoDB collection and retrieves all documents.
If no documents are found, it returns an empty list.
'''


def list_all(mongo_collection):
    '''
    List all documents in a MongoDB collection.
    Return an empty list if no documents are found.
    '''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
