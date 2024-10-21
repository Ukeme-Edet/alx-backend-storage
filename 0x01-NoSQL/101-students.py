#!/usr/bin/env python3
"""
List all documents in Python
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of students
    """
    [
        student
        for student in mongo_collection.aggregate(
            [
                {
                    "$project": {
                        "name": 1,
                        "averageScore": {"$avg": "$topics.score"},
                    },
                },
                {
                    "$sort": {"averageScore": -1},
                },
            ]
        )
    ]
