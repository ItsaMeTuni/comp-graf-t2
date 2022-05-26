from entity import Entity
from model import enemy_model
from vec import Vec
import random

class Enemy(Entity):
    def __init__(self):
        super().__init__(enemy_model, 0.75)
        self.position = Vec(random.uniform(-5, 5), random.uniform(-5, 5))
