#!/usr/bin/env python3
""" function list_all list all documents"""


def list_all(mongo_collection):
    """  function that lists all documents in a collection """
    return mongo_collection.find()
