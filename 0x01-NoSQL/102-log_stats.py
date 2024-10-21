#!/usr/bin/env python3
"""Log stats in Python"""
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
logs = client.logs
nginx_logs = logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def count_logs(mongo_collection):
    """
    Counts the total number of documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB\
            collection to count documents in.

    Returns:
        int: The total number of documents in the collection.
    """
    return mongo_collection.count_documents({})


def count_method(mongo_collection, method):
    """
    Counts the number of documents in a MongoDB collection that match a\
        specified method.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB\
            collection to query.
        method (str): The method to count within the collection.

    Returns:
        int: The count of documents that match the specified method.
    """
    return mongo_collection.count_documents({"method": method})


def count_check(mongo_collection):
    """
    Counts the number of documents in a MongoDB collection that match the\
        specified criteria.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB\
            collection to query.

    Returns:
        int: The count of documents where the method is "GET" and the path is \
            "status".
    """
    return mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )


def count_ips(mongo_collection):
    """
    Counts the occurrences of each IP address in the provided MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection containing log entries.

    Returns:
        dict: A dictionary where the keys are IP addresses and the values are the counts of occurrences of those IP addresses in the collection.
    """
    ip_count = {}
    logs = mongo_collection.find()
    for log in logs:
        ip = log.get("ip")
        if ip:
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1
    return ip_count


if __name__ == "__main__":
    print(f"{count_logs(nginx_logs)} logs")
    print("Methods:")
    [
        print(f"\tmethod {method}: {count_method(nginx_logs, method)}")
        for method in methods
    ]
    print(f"{count_check(nginx_logs)} status check")
    ip_count = count_ips(nginx_logs)
    print("IPs:")
    for ip, count in sorted(
        ip_count.items(), key=lambda x: x[1], reverse=True
    )[:10]:
        print(f"\t{ip}: {count}")
