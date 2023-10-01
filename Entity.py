from enum import Enum

class EntityType(Enum):
    CORE = 1
    USER = 2
    LOGIC = 3
    

class Entity():
    def __init__(self, name) -> None:
        self._name = name