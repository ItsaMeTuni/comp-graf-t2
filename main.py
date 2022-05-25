from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from player import Player
from model import Model

entities = []

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

    entities.append(Player())

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

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    delta = time.time() - last_display_timestamp

    Model("").render()

    for entity in entities:
        entity.tick(delta)
        entity.render()

    last_display_timestamp = time.time()

    glutSwapBuffers()
    glutPostRedisplay()

init()
