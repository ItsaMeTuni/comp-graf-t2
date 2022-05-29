from entity import Entity
from model import enemy_model
from vec import Vec
import random

class Enemy(Entity):
    def __init__(self, player_instance):
        super().__init__(enemy_model, 0.75)
        self.player_instance = player_instance

        self.position = Vec(random.uniform(-5, 5), random.uniform(-5, 5))

    def tick(self, delta):
        super().tick(delta)

        self.look_at(self.player_instance.position)


    def look_at(self, point):
        offset = point - self.position

        angle = Vec(0, 1).angle_between(offset)
        self.rotation = angle
