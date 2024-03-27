#!/usr/bin/env python3
"""
changes the topics of a school
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update document with a specific attr: value
    """
    return mongo_collection.updateMany({
        "name": name
        },
        {
            "$set": {
                "topics": topics
                }
        })
