#!/usr/bin/env python3
"""A python function that list all
document in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all doc in a collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
