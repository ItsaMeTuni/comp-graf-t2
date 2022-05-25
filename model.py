from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

pixel_size = 1

class Model:

    def __init__(self, file_path):
        #file = open(file_path)
        #lines = file.readlines()
        # TODO: implement parser

        self.colors = [(1, 0, 0), (1, 1, 1)]
        self.width = 3
        self.height = 3
        self.pixels = [1, 1, 1, 1, 0, 1, 1, 1, 1]


    def render(self):
        glBegin(GL_QUADS)

        for x in range(self.width):
            for y in range(self.height):
                pixel = self.pixels[y * self.width + x]
                glColor3f(*self.colors[pixel])

                local_x = (x - self.width/2) * pixel_size
                local_y = (y - self.height/2) * pixel_size


                half_pixel = pixel_size / 2
                glVertex3f(local_x - half_pixel, local_y - half_pixel, 0)
                glVertex3f(local_x + half_pixel, local_y - half_pixel, 0)
                glVertex3f(local_x + half_pixel, local_y + half_pixel, 0)
                glVertex3f(local_x - half_pixel, local_y + half_pixel, 0)

        glEnd()
