#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary.values())
        best_student = [key for key, value in a_dictionary.items() if value == max_score]
        return best_student[0]
    return None
