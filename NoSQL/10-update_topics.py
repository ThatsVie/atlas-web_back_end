#!/usr/bin/env python3
'''
This module contains a function to update the topics of a document
in the MongoDB collection based on the name of the school.
'''


def update_topics(mongo_collection, name, topics):
    '''
    Update all topics of the school document with the given name.
    '''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
