# import the functions required

from engine import DecisionEngine
from idea import Idea

def main():

    # initialise engine

    engine = DecisionEngine()

    # add example idea submissions

    engine.add_idea(Idea("Automate reporting dashboard", impact = 5, resource = 2, alignment = 5))
    engine.add_idea(Idea("New intranet homepage", impact = 3, resource = 4, alignment = 3))
    engine.add_idea(Idea("Manual data cleanup task", impact = 2, resource = 5, alignment = 2))

    # Apply decision rules

    engine.update_status()

    # print prioritised results

    print("=== Idea Prioritisation Results ===")
    for idea in engine.prioritise():
        print(f"{idea.title} | Score: {round(idea.score(), 2)} | Status: {idea.status}")

# only run when executed directly, not during testing or import

if __name__ == "__main__":
    main()
