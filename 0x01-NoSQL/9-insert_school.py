#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        kwargs: dictionary with data to insert

    Returns:
        _id of the new document or raise an Exception
    """
    return mongo_collection.insert_one(kwargs).inserted_id
