from datetime import datetime
from enum import Enum

class VisibilityType(Enum):
    PUBLIC = 1
    RESTRICTED = 2
    PRIVATE = 3
    HIDDEN = 4


class Node():
    def __init__(self, authorId : str, givenUID : str, name : str, visib = VisibilityType.PUBLIC):
        self._authorId = authorId
        self._uid = givenUID
        self._name = name
        self._visibility = visib
        self._creationDate = datetime.now()

        print("")

    @property
    def name(self):
        if self._visibility != VisibilityType.PUBLIC:
            return None
        return self._name

    def setPSD(self, t : datetime) -> bool:
        if t > datetime.now():
            return False
        self.destruct = t
        return True
