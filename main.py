from Entity import Entity, EntityType
from Node import Node, VisibilityType

class Chunk(Node):
    def __init__(self, authorId: str, givenUID: str, visib=VisibilityType.PUBLIC):
        super().__init__(authorId, givenUID, f'{authorId}:CHUNK:{givenUID}', visib)

n = Chunk("me", "1231231")

print(n.name)