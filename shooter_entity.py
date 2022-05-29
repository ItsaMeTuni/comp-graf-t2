from entity import Entity, entities
from bullet import Bullet

class ShooterEntity(Entity):
    def __init__(self, lives, model, hitbox_radius):
        super().__init__(model, hitbox_radius)
        self.bullet_count = 0
        self.lives = lives

    def shoot(self):
        bullet = Bullet(self, self.bullet_destroyed)
        bullet.position = self.position
        bullet.rotation = self.rotation

        entities.append(bullet)
        
        self.bullet_count += 1

    def bullet_destroyed(self):
        self.bullet_count -= 1

    def collision_enter(self, other):
        super().collision_enter(other)

        if isinstance(other, Bullet) and other.owner is not self:
            self.take_damage()

    def take_damage(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.lives)
            self.destroy()
