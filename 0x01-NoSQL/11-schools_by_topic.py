#!/usr/bin/env python3
"""
Module that provides a function to return a list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic) ->:
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        topic (str): The topic to search for.

    Returns:
        List[dict]: The list of schools having the specific topic.
    """
    query = {"topics": topic}
    schools = list(mongo_collection.find(query))
    return schools
