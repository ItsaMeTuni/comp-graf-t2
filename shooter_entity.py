from entity import Entity, entities
from bullet import Bullet

class ShooterEntity(Entity):
    def __init__(self, model, hitbox_radius):
        super().__init__(model, hitbox_radius)
        self.bullet_count = 0

    def shoot(self):
        bullet = Bullet(self, self.bullet_destroyed)
        bullet.position = self.position
        bullet.rotation = self.rotation

        entities.append(bullet)

        self.bullet_count += 1

    def bullet_destroyed(self):
        self.bullet_count -= 1
