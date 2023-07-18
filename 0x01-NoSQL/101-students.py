#!/usr/bin/env python3
"""
Function that returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Retrieves all students from the MongoDB collection and sorts them by average score.
    Returns a list of students with their average score included.
    """
    students = mongo_collection.find()

    # Calculate the average score for each student
    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score

    # Sort the students by average score in descending order
    sorted_students = sorted(students, key=lambda student: student['averageScore'], reverse=True)

    return sorted_students
