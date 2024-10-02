#!/usr/bin/env python3
'''
This module contains a function to retrieve all schools with a specific topic.
'''

def schools_by_topic(mongo_collection, topic):
    '''
    Retrieves a list of all schools with the specified topic.
    '''
    return list(mongo_collection.find({"topics": topic}))
