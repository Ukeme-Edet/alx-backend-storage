#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """
    List all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of documents or empty list
    """
    return [doc for doc in mongo_collection.find()]
