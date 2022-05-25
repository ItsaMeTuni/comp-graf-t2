from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from random import uniform

pixel_size = 0.5

class Model:

    def __init__(self, width, height, colors, pixels):
        #file = open(file_path)
        #lines = file.readlines()
        # TODO: implement parser

        self.colors = colors
        self.width = width
        self.height = height
        self.pixels = pixels


    def render(self):

        glPushMatrix()
        glScalef(pixel_size, pixel_size, pixel_size)

        glBegin(GL_QUADS)
        for x in range(self.width):
            for y in range(self.height):
                pixel_color = self.pixels[y * self.width + x]
                glColor3f(*self.colors[pixel_color])

                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y - 1), 0)
                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y - 1), 0)
        glEnd()

        glPopMatrix()

player_model = Model(3, 3, [(0, 0, 0), (1, 0, 0)], [0, 1, 0, 1, 1, 1, 1, 1, 1])
