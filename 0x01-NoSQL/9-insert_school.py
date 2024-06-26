#!/usr/bin/env python3
""" A python function that inserts
a new collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a list into a document
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
