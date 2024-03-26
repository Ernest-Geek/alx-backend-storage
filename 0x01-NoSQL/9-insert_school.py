#!/usr/bin/env python3
""" A python function that inserts
a new collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a list into a document
    """
    data = mongo_collection.insertOne(**kwargs)
    return data.inserted_id
