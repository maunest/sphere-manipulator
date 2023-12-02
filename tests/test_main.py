import unittest
from app.opengl_utils import set_lighting, set_background_color
from OpenGL.GL import *
import pygame


class OpenGLUtilsTest(unittest.TestCase):
    def setUp(self):
        """
        Настройка окна Pygame для тестов OpenGL.
        """
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    def tearDown(self):
        """
        Очистка Pygame после тестов.
        """
        pygame.quit()

    def test_set_lighting(self):
        """
        Тест функции установки освещения.
        """
        initial_light_position = [200, 200, 100, 0.0]  # Позиция источника света (X, Y, Z, W)
        set_lighting(initial_light_position)

        expected_light_position = glGetLightfv(GL_LIGHT0, GL_POSITION)
        expected_light_position = [expected_light_position[i] for i in range(4)]

        self.assertEqual(initial_light_position, expected_light_position, "Проверка установки позиции света")

        # Проверка включения света и освещения
        self.assertTrue(glIsEnabled(GL_LIGHT0), "Проверка включения света")
        self.assertTrue(glIsEnabled(GL_LIGHTING), "Проверка включения освещения")

    def test_set_background_color(self):
        """
        Тест функции установки цвета фона.
        """

        set_background_color(0.5, 0.5, 0.5)  # Установка цвета фона (R, G, B)
        expected_background_color = [0.5, 0.5, 0.5, 1.0]  # Ожидаемый цвет фона (R, G, B, A)

        # Получение текущего цвета фона (R, G, B, A)
        actual_background_color = glGetFloatv(GL_COLOR_CLEAR_VALUE)
        actual_background_color = [actual_background_color[i] for i in range(4)]

        self.assertEqual(actual_background_color[:3], expected_background_color[:3],
                         "Проверка установки цвета фона (RGB)")


if __name__ == '__main__':
    unittest.main()
