from entity import Entity
from model import bullet_model
from vec import Vec

speed = 20
world_size = 10

class Bullet(Entity):
    
    def __init__(self):
        super().__init__(bullet_model)

    def tick(self, delta):
        self.position += Vec(0, 1).rotate(self.rotation) * speed * delta

        if (self.position.x < -world_size or self.position.x > world_size or
           self.position.y < -world_size or self.position.y > world_size):
            self.destroy()

