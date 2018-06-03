# @Time    : 2018/5/26 21:15
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
dot_color = (255, 0, 0)
looping = True
radius = 15

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            pygame.draw.circle(screen, dot_color, spot, radius)
    pygame.display.update()

pygame.quit()