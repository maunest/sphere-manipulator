import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init(width, height):
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)

    # Инициализация GLUT
    glutInit()

    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    # Устанавливаем свет
    light_position = [200, 200, 100, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Устанавливаем белый фон
    glClearColor(1.0, 1.0, 1.0, 1.0)


def draw_sphere(x, y, z, scale, color, light_position):
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(scale, scale, scale)
    glColor3f(color[0], color[1], color[2])
    glutSolidSphere(1, 50, 50)
    glPopMatrix()