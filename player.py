from keyboard import is_key_pressed
from model import player_model
from vec import Vec
from bullet import Bullet
from shooter_entity import ShooterEntity

rotation_speed = 270 
acceleration = 40
drag = 10

class Player(ShooterEntity):

    def __init__(self):
        super().__init__(player_model, 0.75)
        self.position = Vec(0, 0)
        self.rotation = 0 
        self.momentum = Vec(0, 0)

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

        if is_key_pressed(b' '):
            self.shoot()

        self.rotation += rot * rotation_speed * delta
        self.momentum += Vec(0, dist).rotate(self.rotation) * acceleration * delta
        self.momentum -= self.momentum.normalized() * 10 * delta

        self.position += self.momentum * delta

