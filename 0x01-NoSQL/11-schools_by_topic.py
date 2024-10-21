#!/usr/bin/env python3
"""List all documents in Python"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic: (string) topic searched

    Returns:
        list of schools
    """
    return [doc for doc in mongo_collection.find({"topics": topic})]
