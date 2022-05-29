from entity import Entity, entities
from bullet import Bullet

class ShooterEntity(Entity):
    def __init__(self, model, hitbox_radius):
        super().__init__(model, hitbox_radius)

    def shoot(self):
        bullet = Bullet(self)
        bullet.position = self.position
        bullet.rotation = self.rotation

        entities.append(bullet)

