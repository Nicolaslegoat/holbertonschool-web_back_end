#!/usr/bin/env python3
"""No module import"""


def schools_by_topic(mongo_collection, topic):
    """unction that returns the list of school having a specific topic"""
    mongo_collection.find(
        {"topic": topic}
    )
