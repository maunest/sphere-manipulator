import unittest
from app.opengl_utils import set_lighting, set_background_color
from OpenGL.GL import *
import pygame


class OpenGLUtilsTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    def tearDown(self):
        pygame.quit()

    def test_set_lighting(self):
        initial_light_position = [200, 200, 100, 0.0]
        set_lighting(initial_light_position)

        expected_light_position = glGetLightfv(GL_LIGHT0, GL_POSITION)
        expected_light_position = [expected_light_position[i] for i in range(4)]

        self.assertEqual(initial_light_position, expected_light_position,
                         "Проверка установки позиции света")

        # Проверка включения света и освещения
        self.assertTrue(glIsEnabled(GL_LIGHT0), "Проверка включения света")
        self.assertTrue(glIsEnabled(GL_LIGHTING), "Проверка включения освещения")

    def test_set_background_color(self):
        initial_background_color = glGetFloatv(GL_COLOR_CLEAR_VALUE)
        initial_background_color = [initial_background_color[i] for i in range(3)]  # Преобразование в список RGB

        set_background_color(0.5, 0.5, 0.5)
        expected_background_color = [0.5, 0.5, 0.5, 1.0]

        actual_background_color = glGetFloatv(GL_COLOR_CLEAR_VALUE)
        actual_background_color = [actual_background_color[i] for i in range(4)]  # Преобразование в список RGBA

        self.assertEqual(actual_background_color[:3], expected_background_color[:3],
                         "Проверка установки цвета фона (RGB)")

        # Установка альфа-канала в 0.0
        glClearColor(initial_background_color[0], initial_background_color[1], initial_background_color[2], 0.0)
        glClear(GL_COLOR_BUFFER_BIT)
        reset_background_color = glGetFloatv(GL_COLOR_CLEAR_VALUE)
        reset_background_color = [reset_background_color[i] for i in range(4)]  # Преобразование в список RGBA

        self.assertEqual(reset_background_color, initial_background_color + [0.0],
                         "Проверка сброса цвета фона (RGB с установкой альфа-канала в 0.0)")


if __name__ == '__main__':
    unittest.main()
