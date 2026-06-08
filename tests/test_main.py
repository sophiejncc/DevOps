from src.idea import Idea
from src.engine import DecisionEngine

# Arrange
# Act
# Assert

def test_high_priority_idea():
    idea = Idea("High priority", impact = 5, resource = 1, alignment = 5)
    assert idea.score() >= 4

def test_low_priority_idea():
    idea = Idea("Low priority", impact = 1, resource = 5, alignment = 1)
    assert idea.score() < 2

def test_status_update():
    engine = DecisionEngine()
    idea = Idea("Test idea", impact = 5, resource = 1, alignment = 5)

    engine.add_idea(idea)
    engine.update_status()

    assert idea.status =="Approved"
