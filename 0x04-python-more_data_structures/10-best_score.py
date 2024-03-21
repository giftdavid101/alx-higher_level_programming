#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != 0:
        score = 0
        person = 0
    for k in a_dictionary.keys():
        if score == 0 or a_dictionary[k] > score:
            score = a_dictionary[k]
            person = k
    return person
