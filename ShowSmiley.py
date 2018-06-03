# @Time    : 2018/5/27 5:47
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("笑脸")
looping = True
smiley_jpg = pygame.image.load("smiley-80x80.jpg")

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False

    screen.blit(smiley_jpg, (100, 100))
    pygame.display.update()

pygame.quit()