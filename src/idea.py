from dataclasses import dataclass, field

@dataclass
class Idea:
    title: str
    impact: int
    resource: int
    alignment: int
    status: str = field(default="Submitted")

    def score(self) -> float:
        return (self.impact * 0.6) + (self.alignment * 0.5) - (self.resource * 0.2)