from entity import Entity
from model import bullet_model
from vec import Vec

speed = 20
world_size = 10

class Bullet(Entity):
    
    def __init__(self, owner):
        super().__init__(bullet_model, 0.3)
        self.owner = owner

    def tick(self, delta):
        self.position += Vec(0, 1).rotate(self.rotation) * speed * delta

        if (self.position.x < -world_size or self.position.x > world_size or
           self.position.y < -world_size or self.position.y > world_size):
            self.destroy()

    def collision_enter(self, other):
        if other is not self.owner and not isinstance(other, Bullet):
            self.destroy()
