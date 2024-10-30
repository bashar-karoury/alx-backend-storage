#!/usr/bin/env python3
""" Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs
        and returns _id of inserted document
    """
    to_insert = {**kwargs}
    return mongo_collection.insert_one(to_insert).inserted_id
