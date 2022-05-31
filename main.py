from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from player import Player
from entity import entities
from enemy import Enemy
import ctypes

enemy_count = 5

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

    for _ in range(enemy_count):
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

def draw_string(s):
    for c in s:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(c)))

last_display_timestamp = time.time() 
lost_game = False
won_game = False
def display():
    global last_display_timestamp
    global entities
    global lost_game, won_game

    delta = time.time() - last_display_timestamp
    last_display_timestamp = time.time()

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glColor3f(1, 1, 1)
    if lost_game:
        glRasterPos2f(0.5, 0.5)
        draw_string('You lost')

    if won_game:
        glRasterPos2f(0.5, 0.5)
        draw_string('You won')

    if lost_game or won_game:
        glutSwapBuffers()
        return

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
    
    lost_game = True
    won_game = True
    for entity in entities:
        if entity.is_destroyed:
            entities.remove(entity)

        if isinstance(entity, Enemy):
            won_game = False

        if isinstance(entity, Player):
            lost_game = False

    

    glutSwapBuffers()
    glutPostRedisplay()


init()
