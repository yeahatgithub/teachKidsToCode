# @Time    : 2018/5/26 21:31
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
green = (0, 200, 0)
is_mouse_down = False
looping = True
radius = 10

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            is_mouse_down = False
    if is_mouse_down:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, green, spot, radius)
    pygame.display.update()

pygame.quit()