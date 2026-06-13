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
    
    
    def __post_init__(self):
        for field_name in ["impact", "resource", "alignment"]:
            value = getattr(self, field_name)
            if not 1 <= value <= 5:
                raise ValueError(f"{field_name} must be between 1 and 5")
            