from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time

entities = []

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    window = glutCreateWindow("Matrix Stack")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0, 0, 0, 1)
    glutMainLoop()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, 0.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

last_display_timestamp = time.time() 
def display():
    glClearColor(1, 1, 1, 1)

    delta = time.time() - last_display_timestamp
    
    for entity in entities:
        entity.tick(delta)
        entity.draw()

    last_display_timestamp = time.time()

init()
