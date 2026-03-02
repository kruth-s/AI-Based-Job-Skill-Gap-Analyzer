# Data models or ORM definitions for the project

from typing import List


class Profile:
    def __init__(self, name: str, skills: List[str]):
        self.name = name
        self.skills = skills
