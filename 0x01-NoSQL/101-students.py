#!/usr/bin/env python3
"""
Top students
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of students
    """
    students = mongo_collection.aggregate(
        [
            {
                "$project": {
                    "_id": 1,
                    "name": 1,
                    "averageScore": {
                        "$avg": {
                            "$avg": "$topics.score",
                        },
                    },
                    "topics": 1,
                },
            },
            {
                "$sort": {"averageScore": -1},
            },
        ]
    )
    return students
