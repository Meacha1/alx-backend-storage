#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a collection.
"""
import pymongo


def list_all(mongo_collection: Collection) -> list:
    """
    Lists all documents in the given collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: List of all documents in the collection. Returns an empty list if no documents found.
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
