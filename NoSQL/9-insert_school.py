#!/usr/bin/env python3
'''
This module contains a function to insert document into a MongoDB collection.
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document into the MongoDB collection using kwargs.
    Returns the new _id of the inserted document.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
