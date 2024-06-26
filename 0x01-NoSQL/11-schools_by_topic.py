#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find by specific value
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})

