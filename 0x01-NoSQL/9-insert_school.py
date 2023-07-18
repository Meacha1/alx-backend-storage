#!/usr/bin/env python3
"""
Module that provides a function to insert a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the given collection based on keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        **kwargs: Keyword arguments representing the fields and values of the document.

    Returns:
        Any: The new _id of the inserted document.
    """
    document = kwargs
    result = mongo_collection.insert_one(document)
    new_id = result.inserted_id
    return new_id
