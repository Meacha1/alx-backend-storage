#!/usr/bin/env python3
"""
Script that provides statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Retrieves statistics about Nginx logs from MongoDB and displays the results.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get the count of each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Get the count of logs with method=GET and path=/status
    count_status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count_status_check} status check")
