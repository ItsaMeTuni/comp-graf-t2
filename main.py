from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from player import Player
from entity import entities
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

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
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

    collisions = []

    for entity in entities:
        if entity.is_destroyed:
            continue

        entity.tick(delta)
        entity.render()

        for other in entities:
            if other is entity or entity.is_destroyed:
                continue

            if (other, entity) in collisions:
                continue
            
            collides = entity.do_collision_test(other)
            if collides:
                entity.collision_enter(other)
                other.collision_enter(entity)

            collisions.append((entity, other))

    for entity in entities:
        if entity.is_destroyed:
            entities.remove(entity)

    glutSwapBuffers()
    glutPostRedisplay()


init()
