from dataclasses import dataclass


@dataclass
class TestCase:
    name: str = None

    def __str__(self):
        return self.name
