from OpenGL.GL import *
from vec import Vec

class Entity:
    def __init__(self, model):
        self.model = model
        self.position = Vec(0, 0)
        self.rotation = 0

    def tick(self, delta):
        pass

    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0)
        glRotatef(self.rotation, 0, 0, 1)
        self.model.render()
        glPopMatrix()
        
