from entity import Entity
from model import bullet_model
from vec import Vec

speed = 20
world_size = 10

class Bullet(Entity):
    
    def __init__(self, owner, on_destroy):
        super().__init__(bullet_model, 0.3)
        self.owner = owner
        self.on_destroy = on_destroy

    def tick(self, delta):
        self.position += Vec(0, 1).rotate(self.rotation) * speed * delta

        if (self.position.x < -world_size or self.position.x > world_size or
           self.position.y < -world_size or self.position.y > world_size):
            self.destroy()

    def collision_enter(self, other):
        from enemy import Enemy
        from player import Player

        if other is not self.owner and not isinstance(other, Bullet):
            if ((isinstance(self.owner, Player) and isinstance(other, Enemy))
                or (isinstance(self.owner, Enemy) and isinstance(other, Player))):
                self.destroy()
                other.take_damage()

    def destroy(self):
        if self.on_destroy is not None:
            self.on_destroy()

        super().destroy()
