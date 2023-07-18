#!/usr/bin/env python3
"""
Function that returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Retrieves all students from the MongoDB collection and sorts them by average score.
    Returns a list of students with their average score included.
    """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "averageScore": -1
            }
        }
    ])
