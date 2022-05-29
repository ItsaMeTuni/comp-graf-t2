from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from player import Player
from model import Model
from entity import entities
from bullet import Bullet
from enemy import Enemy

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    window = glutCreateWindow("Matrix Stack")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard.on_down)
    glutKeyboardUpFunc(keyboard.on_up)

    player = Player()
    entities.append(player)
    entities.append(Enemy(player))
    entities.append(Enemy(player))
    entities.append(Enemy(player))

    glClearColor(0, 0, 0, 1)
    glutMainLoop()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

last_display_timestamp = time.time() 
def display():
    global last_display_timestamp
    global entities

    delta = time.time() - last_display_timestamp
    last_display_timestamp = time.time()

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    for entity in entities:
        if entity.is_destroyed:
            continue

        entity.tick(delta)
        entity.render()

        for other in entities:
            if other is entity or entity.is_destroyed:
                continue
            
            entity.do_collision_test(other)

    #entities = [entity for entity in entities if not entity.is_destroyed]

    glutSwapBuffers()
    glutPostRedisplay()


init()
