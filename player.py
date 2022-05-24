from entity import Entity
from keyboard import is_key_pressed

class Player(Entity):

    def __init__(self):
        super().__init__()

    def tick(self, delta):
        super().tick(delta)
