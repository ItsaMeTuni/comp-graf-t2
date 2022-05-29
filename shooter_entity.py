from entity import Entity, entities
from bullet import Bullet

cooldown = 0.08

class ShooterEntity(Entity):
    def __init__(self, model, hitbox_radius):
        super().__init__(model, hitbox_radius)
        self.remaining_cooldown = 0


    def tick(self, delta):
        super().tick(delta)

        self.remaining_cooldown -= delta

    def shoot(self):
        if self.remaining_cooldown > 0:
            return

        self.remaining_cooldown = cooldown

        bullet = Bullet(self)
        bullet.position = self.position
        bullet.rotation = self.rotation

        entities.append(bullet)

