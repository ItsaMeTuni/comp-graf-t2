from shooter_entity import ShooterEntity
from model import enemy_model
from vec import Vec
import random

class Enemy(ShooterEntity):
    def __init__(self, player_instance):
        super().__init__(1, enemy_model, 0.75)
        self.player_instance = player_instance
        
        self.min_cooldown = 1
        self.max_cooldown = 2.3 
        self.set_cooldown()

        self.position = Vec(random.uniform(-5, 5), random.uniform(-5, 5))

    def tick(self, delta):
        super().tick(delta)

        self.remaining_cooldown -= delta 

        self.look_at(self.player_instance.position)

        if self.remaining_cooldown <= 0:
            #self.shoot()
            self.set_cooldown()

    def set_cooldown(self):
        self.remaining_cooldown = random.uniform(self.min_cooldown, self.max_cooldown)


    def look_at(self, point):
        offset = point - self.position

        angle = Vec(0, 1).angle_between(offset)
        self.rotation = angle
