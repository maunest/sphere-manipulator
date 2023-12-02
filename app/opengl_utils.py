import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init(width, height):
    """
    Инициализирует окно Pygame для работы с OpenGL.

    Args:
    - width (int): Ширина окна.
    - height (int): Высота окна.
    """
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)

    glutInit()

    # Устанавливает перспективу камеры. 45 - угол обзора, (width / height) - соотношение сторон,
    # 0.1 - ближняя плоскость отсечения, 50.0 - дальняя плоскость отсечения.
    gluPerspective(45, (width / height), 0.1, 50.0)

    # Перемещает объекты вдоль оси Z на -5, чтобы они были видны в области экрана.
    glTranslatef(0, 0, -5)

    # Позиция источника света: x=200, y=200, z=100.
    light_position = [200, 200, 100, 0.0]
    set_lighting(light_position)

    # Установка цвета фона на белый (1.0, 1.0, 1.0).
    set_background_color(1.0, 1.0, 1.0)


def set_lighting(light_position):
    """
    Устанавливает параметры освещения.

    Args:
    - light_position (list): Позиция источника света.
    """
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)


def set_background_color(red, green, blue):
    """
    Устанавливает цвет фона.

    Args:
    - red (float): Значение красного цвета (от 0.0 до 1.0).
    - green (float): Значение зеленого цвета (от 0.0 до 1.0).
    - blue (float): Значение синего цвета (от 0.0 до 1.0).
    """
    glClearColor(red, green, blue, 1.0)


def draw_sphere(x, y, z, scale, color, light_position):
    """
    Рисует сферу с заданными параметрами.

    Args:
    - x (float): Позиция по оси X.
    - y (float): Позиция по оси Y.
    - z (float): Позиция по оси Z.
    - scale (float): Масштаб сферы.
    - color (list): Цвет сферы (RGB список значений от 0.0 до 1.0).
    - light_position (list): Позиция источника света.
    """
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(scale, scale, scale)
    glColor3f(color[0], color[1], color[2])

    # Рисует сферу с радиусом 1 и детализацией в 50x50.
    glutSolidSphere(1, 50, 50)

    glPopMatrix()
