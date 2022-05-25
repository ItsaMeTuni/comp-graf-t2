from entity import Entity
from keyboard import is_key_pressed
from model import player_model
from vec import Vec

speed = 8
rotation_speed = 270 

class Player(Entity):

    def __init__(self):
        super().__init__(player_model)
        self.position = Vec(0, 0)
        self.rotation = 0 

    def tick(self, delta):
        super().tick(delta)

        dist = 0 
        rot = 0

        if is_key_pressed(b'w'):
            dist += 1

        if is_key_pressed(b's'):
            dist -= 1

        if is_key_pressed(b'd'):
            rot -= 1
        
        if is_key_pressed(b'a'):
            rot += 1

        self.rotation += rot * rotation_speed * delta
        self.position += Vec(0, dist).rotate(self.rotation) * speed * delta

