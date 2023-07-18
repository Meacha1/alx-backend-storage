#!/usr/bin/env python3
"""
Script that provides statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def count_documents(mongo_collection, query):
    """
    Counts the number of documents in the collection that match the given query.
    Returns the count.
    """
    return mongo_collection.count_documents(query)


def get_top_ips(mongo_collection, limit=10):
    """
    Retrieves the top N most present IPs in the collection.
    Returns a list of tuples containing the IP and its count.
    """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": limit}
    ]
    result = mongo_collection.aggregate(pipeline)
    top_ips = [(entry['_id'], entry['count']) for entry in result]
    return top_ips
