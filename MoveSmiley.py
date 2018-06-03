# @Time    : 2018/5/27 5:47
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("笑脸")
looping = True
smiley_jpg = pygame.image.load("good-900x900.png").convert_alpha()
smiley_jpg = pygame.transform.scale(smiley_jpg, (60, 60))
# color_key = smiley_jpg.get_at((0, 0))
# smiley_jpg.set_colorkey(color_key)
# print(color_key)

pic_x = 0
pic_y = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()
speed_x = 1
speed_y = 1

while looping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False
    # screen.fill(BLACK)

    screen.blit(smiley_jpg, (pic_x, pic_y))
    pygame.display.update()
    pic_x += speed_x
    pic_y += speed_y
    if pic_x <=0 or pic_x + smiley_jpg.get_width() >= 800:
        speed_x = -speed_x
    if pic_y <= 0 or pic_y + smiley_jpg.get_height() >= 600:
        speed_y = -speed_y
    timer.tick(60)   #一秒钟不超过60帧

pygame.quit()