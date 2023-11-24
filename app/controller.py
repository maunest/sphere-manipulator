import pygame
from pygame.locals import *
from opengl_utils import *

def main():
    pygame.init()
    width, height = 800, 600
    init(width, height)

    sphere_x, sphere_y, sphere_z = 0, 0, 0  # Позиция сферы по осям X, Y, Z
    sphere_change = 0.3
    sphere_scale = 1.0
    sphere_color = [1.0, 0.0, 0.0]  # Начальный цвет: красный

    light_position = [200, 200, 100, 0.0]

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_w:
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
                    light_position[0] -= 10000
                elif event.key == K_RIGHT:
                    light_position[0] += 10000
                elif event.key == K_UP:
                    light_position[1] += 10000
                elif event.key == K_DOWN:
                    light_position[1] -= 10000

        draw_sphere(sphere_x, sphere_y, sphere_z, sphere_scale, sphere_color, light_position)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()