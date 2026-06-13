from src.idea import Idea
from src.engine import DecisionEngine
import pytest

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

def test_invalid_impact_raises_error():
    with pytest.raises(ValueError) as exc_info:
        Idea("Bad idea", impact = 6, resource = 3, alignment = 3)
    assert "impact" in str(exc_info.value)

def test_invalid_resource_raises_error():
    with pytest.raises(ValueError) as exc_info:
        Idea("Bad idea", impact = 3, resource = 0, alignment = 3)
    assert "resource" in str(exc_info.value)


def test_invalid_alignment_raises_error():
    with pytest.raises(ValueError) as exc_info:
        Idea("Bad idea", impact = 3, resource = 3, alignment = 10)
    assert "alignment" in str(exc_info.value)
