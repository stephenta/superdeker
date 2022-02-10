from fileinput import filename
import json
import os

class Score():
    def __init__(self, username, score, date):
        self.username = username
        self.score = score
        self.date = date

def read_scores(filename):
    if not os.path.exists(filename):
        return None

    with open(filename) as f:
        data = json.load(f)
    
    scores = []
    for d in data:
        s = Score(d['username'], d['score'], d['date'])
        scores.append(s)

    return scores

def get_recent_scores(filename, number_of_scores):
    # assume json file is in order of date (most recent is last)
    scores = read_scores(filename)

    if number_of_scores < len(scores):
        ind = len(scores) - number_of_scores
        return scores[ind:]
    else:
        return scores

def get_high_scores(filename, number_of_scores):
    scores = read_scores(filename)
    scores.sort(key=lambda x: x.score, reverse=True)

    return scores[0:number_of_scores]
