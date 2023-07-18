#!/usr/bin/env python3
"""
Module that provides a function to update topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        name (str): The name of the school to update.
        topics (List[str]): The list of topics to set for the school.
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)
