#!/usr/bin/env python3
"""Update a document in Python"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name: (string) school name to update
        topics: (list of strings) list of topics approached in the school

    Returns:
        Nothing
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
