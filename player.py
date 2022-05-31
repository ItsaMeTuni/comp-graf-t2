from keyboard import is_key_pressed
from model import player_model
from vec import Vec
from bullet import Bullet
from shooter_entity import ShooterEntity
from debug_utils import debug_vector

rotation_speed = 270 
acceleration = 30
drag = 30
max_bullets = 10

class Player(ShooterEntity):

    def __init__(self):
        super().__init__(3, player_model, 0.75)
        self.position = Vec(0, 0)
        self.rotation = 0 
        self.momentum = Vec(0, 0)
        self.can_shoot = False

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


        shoot_pressed = is_key_pressed(b' ')
        if shoot_pressed and self.can_shoot and self.bullet_count < max_bullets:
            self.can_shoot = False
            self.shoot()

        if not shoot_pressed:
            self.can_shoot = True

        self.rotation += rot * rotation_speed * delta
        self.momentum += Vec(0, dist).rotate(self.rotation) * acceleration * delta

        if dist == 0:
            self.momentum -= self.momentum.normalized() * drag * delta

        self.position += self.momentum * delta

        self.check_bounds_collision()

    def check_bounds_collision(self):
        bounds = 10
       
        if self.position.x + self.hitbox_radius >= bounds:
            self.position.x = bounds - self.hitbox_radius 
            self.momentum.x = 0
            
        elif self.position.x - self.hitbox_radius <= -bounds:
            self.position.x = -bounds + self.hitbox_radius 
            self.momentum.x = 0

        if self.position.y + self.hitbox_radius >= bounds:
            self.position.y = bounds - self.hitbox_radius 
            self.momentum.y = 0

        elif self.position.y - self.hitbox_radius <= -bounds:
            self.position.y = -bounds + self.hitbox_radius 
            self.momentum.y = 0

