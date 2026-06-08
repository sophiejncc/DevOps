from typing import List
from idea import Idea


class DecisionEngine:
    def __init__(self):
        self.ideas: List[Idea] = []

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def update_status(self):
        for idea in self.ideas:
            score = idea.score()

            if score >= 4:
                idea.status = "Approved"
            elif 2 <= score < 4:
                idea.status = "Under Review"
            else:
                idea.status = "Rejected"
