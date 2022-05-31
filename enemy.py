from shooter_entity import ShooterEntity
from entity import entities
from model import enemy_model_1, enemy_model_2, enemy_model_3
from vec import Vec
import random

def choose_random_model():
    chance = random.uniform(0, 3)
    if chance < 1:
        return enemy_model_1
    elif chance < 2:
        return enemy_model_2
    else:
        return enemy_model_3



class Enemy(ShooterEntity):
    def __init__(self, player_instance):
        super().__init__(1, choose_random_model(), 0.75)
        self.player_instance = player_instance
        
        self.min_cooldown = 1
        self.max_cooldown = 2.3 
        self.set_cooldown()

        self.random_position()

    def random_position(self):
        while True:
            self.position = Vec(random.uniform(-8, 8), random.uniform(-8, 8))
            for entity in entities:
                if self.do_collision_test(entity):
                    continue

            break

    def tick(self, delta):
        super().tick(delta)

        self.remaining_cooldown -= delta 

        self.look_at(self.player_instance.position)

        if self.remaining_cooldown <= 0:
            self.shoot()
            self.set_cooldown()

    def set_cooldown(self):
        self.remaining_cooldown = random.uniform(self.min_cooldown, self.max_cooldown)


    def look_at(self, point):
        offset = point - self.position

        angle = Vec(0, 1).angle_between(offset)
        self.rotation = angle
