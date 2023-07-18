#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a collection.
"""
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> list:
    """
    Lists all documents in the given collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: List of all documents in the collection. Returns an empty list if no documents found.
    """
    documents = list(mongo_collection.find())
    return documents


if __name__ == "__main__":
    """
    Main function to test the list_all function.
    """
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

