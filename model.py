from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from random import uniform

pixel_size = 0.5

class Model:

    def __init__(self, width, height, colors, pixels):
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
                glColor4f(*self.colors[pixel_color])
                
                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y - 1), 0)
                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y - 1), 0)

        glEnd()

        glPopMatrix()


def parse_model(file_path):
    file = open(file_path)

    # skip first line
    file.readline()

    colors = []
    color_count = int(file.readline())
    for _ in range(color_count):
        channels = [int(color) for color in file.readline().split(' ')]

        alpha = 1
        if len(channels) == 5:
            alpha = channels[4]

        colors.append((channels[1], channels[2], channels[3], alpha))

    # skip blank line
    file.readline()

    # skip section name
    file.readline()
   
    pixels = []
    [row_count, col_count] = [int(value) for value in file.readline().split(' ')]
    for _ in range(row_count):
        row_pixels = [int(pixel) - 1 for pixel in file.readline().split(' ')]
        pixels.extend(row_pixels)

    return Model(col_count, row_count, colors, pixels)



#player_model = Model(3, 3, [(0, 0, 0), (1, 0, 0)], [0, 1, 0, 1, 1, 1, 1, 1, 1])
player_model = parse_model('test_model.txt')
enemy_model = Model(3, 3, [(0, 0, 0, 0), (1, 0.6, 0, 1)], [0, 1, 0, 1, 1, 1, 0, 1, 0])
bullet_model = Model(1, 1, [(0, 0.7, 0.7, 1)], [0])
