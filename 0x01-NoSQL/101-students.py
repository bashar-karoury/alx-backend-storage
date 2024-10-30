#!/usr/bin/env python3
""" Top students"""
import pymongo


def top_students(mongo_collection):
    """ function that returns all students sorted by average score
    """

    # Iterate over each document in the collection
    for student in mongo_collection.find():
        # Check if 'scores' is present and is a list
        if "topics" in student and isinstance(student["topics"], list):
            # Calculate the average score
            sum_scores = 0
            for topic in student["topics"]:
                sum_scores += topic["score"]
            average_score = sum_scores / len(student["topics"])
            print(average_score)
            # Update the document with the new 'average' field
            mongo_collection.update_one(
                {"_id": student["_id"]},  # Filter for the current student
                {"$set": {"averageScore": average_score}}  # Set the new field
            )
            print(student)
    return list(mongo_collection.find().sort("averageScore", pymongo.DESCENDING))
