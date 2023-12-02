import pygame
from pygame.locals import *
from app.opengl_utils import *


def handle_key_events(sphere_position, sphere_scale, sphere_color, light_position, event):
    """
    Обрабатывает события нажатия клавиш.

    Args:
    - sphere_position (tuple): Позиция сферы по осям X, Y, Z.
    - sphere_scale (float): Масштаб сферы.
    - sphere_color (list): Цвет сферы в формате RGB.
    - light_position (list): Позиция источника света.
    - event (pygame.event.Event): Событие клавиатуры.

    Returns:
    - tuple: Обновленные значения позиции сферы, масштаба, цвета и позиции источника света.
    """
    sphere_x, sphere_y, sphere_z = sphere_position
    sphere_change = 0.3  # Изменение позиции сферы при нажатии клавиш

    if event.type == pygame.KEYDOWN:
        if event.key == K_w:
            sphere_y += sphere_change
        elif event.key == K_s:
            sphere_y -= sphere_change
        elif event.key == K_a:
            sphere_x -= sphere_change
        elif event.key == K_d:
            sphere_x += sphere_change
        elif event.key == K_q:
            sphere_scale -= sphere_change
            if sphere_scale < sphere_change:
                sphere_scale = sphere_change
        elif event.key == K_e:
            sphere_scale += sphere_change
        elif event.key == K_r:
            sphere_color = [1.0, 0.0, 0.0]  # Красный цвет
        elif event.key == K_g:
            sphere_color = [0.0, 1.0, 0.0]  # Зеленый цвет
        elif event.key == K_b:
            sphere_color = [0.0, 0.0, 1.0]  # Синий цвет
        elif event.key == K_LEFT:
            light_position[0] -= 10000  # Изменение позиции источника света по оси X
        elif event.key == K_RIGHT:
            light_position[0] += 10000  # Изменение позиции источника света по оси X
        elif event.key == K_UP:
            light_position[1] += 10000  # Изменение позиции источника света по оси Y
        elif event.key == K_DOWN:
            light_position[1] -= 10000  # Изменение позиции источника света по оси Y

    return [sphere_x, sphere_y, sphere_z], sphere_scale, sphere_color, light_position


def main():
    """
    Основная функция программы.
    """
    pygame.init()
    width, height = 800, 600
    init(width, height)

    sphere_position = (0, 0, 0)  # Позиция сферы по осям X, Y, Z
    sphere_scale = 1.0  # Начальный масштаб сферы
    sphere_color = [1.0, 0.0, 0.0]  # Начальный цвет сферы: красный
    light_position = [200, 200, 100, 0.0]  # Позиция источника света

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                # Обработка событий нажатия клавиш
                sphere_position, sphere_scale, sphere_color, light_position = handle_key_events(
                    sphere_position, sphere_scale, sphere_color, light_position, event
                )

        # Рисует сферу с заданными параметрами
        draw_sphere(sphere_position[0], sphere_position[1], sphere_position[2],
                    sphere_scale, sphere_color, light_position)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()
