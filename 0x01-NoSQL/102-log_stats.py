#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":

    # connect to Mongodb
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # get number of documnets
    no_docs = nginx_collection.count_documents({})

    # get GET count
    # Aggregation pipeline to count documents with method set to "GET"
    pipeline = [
        {"$match": {"method": "GET"}},  # Filter for documents with method "GET"
        # Count the matching documents and label the result as "get_requests"
        {"$count": "get_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        get_count = result[0]["get_requests"]
    else:
        get_count = 0

    # get POST count
    # Aggregation pipeline to count documents with method set to "POST"
    pipeline = [
        # Filter for documents with method "POST"
        {"$match": {"method": "POST"}},
        # Count the matching documents and label the result as "get_requests"
        {"$count": "post_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        post_count = result[0]["post_requests"]
    else:
        post_count = 0

    # get PUT count
    # Aggregation pipeline to count documents with method set to "PUT"
    pipeline = [
        # Filter for documents with method "PUT"
        {"$match": {"method": "PUT"}},
        # Count the matching documents and label the result as "get_requests"
        {"$count": "put_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        put_count = result[0]["put_requests"]
    else:
        put_count = 0

    # get PATCH
    # Aggregation pipeline to count documents with method set to "PATCH"
    pipeline = [
        # Filter for documents with method "PATCH"
        {"$match": {"method": "PATCH"}},
        # Count the matching documents and label the result as "get_requests"
        {"$count": "patch_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        patch_count = result[0]["patch_requests"]
    else:
        patch_count = 0

    # get DETLETE count
    # Aggregation pipeline to count documents with method set to "DELETE"
    pipeline = [
        # Filter for documents with method "DELETE"
        {"$match": {"method": "DELETE"}},
        # Count the matching documents and label the result as "get_requests"
        {"$count": "delete_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        delete_count = result[0]["delete_requests"]
    else:
        delete_count = 0

    # get no_status for all documents that has path=/status
    pipeline = [
        # Filter for documents with method "GET"
        {"$match": {"method": "GET"}},
        # Filter for documents with path = /status
        {"$match": {"path": "/status"}},
        # Count the matching documents and label the result as "get_requests"
        {"$count": "get_status_requests"}
    ]

    # Run the aggregation
    result = list(nginx_collection.aggregate(pipeline))
    if result:
        no_status = result[0]["get_status_requests"]
    else:
        no_status = 0

    # print result
    print(f'{no_docs} logs')
    print('Methods:')
    print(f'\tmethod GET: {get_count}')
    print(f'\tmethod POST: {post_count}')
    print(f'\tmethod PUT: {put_count}')
    print(f'\tmethod PATCH: {patch_count}')
    print(f'\tmethod DELETE: {delete_count}')
    print(f'{no_status} status check')

    # Use aggregation to find the top 10 IPs
    pipeline = [
        {
            "$group": {
                "_id": "$ip",  # Group by the IP address
                "count": {"$sum": 1}  # Count occurrences
            }
        },
        {
            "$sort": {
                "count": -1  # Sort by count in descending order
            }
        },
        {
            "$limit": 10  # Limit the results to the top 10
        }
    ]

    top_ips = nginx_collection.aggregate(pipeline)
    # Print the top 10 IPs
    print('IPs:')
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
