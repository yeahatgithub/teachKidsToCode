# @Time    : 2018/5/27 7:41
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame

pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("笑脸")
# looping = True
color_dict = {}
smiley_jpg = pygame.image.load("smiley-80x80.png")
for r in range(smiley_jpg.get_height()):
    for c in range(smiley_jpg.get_width()):
        color_key = smiley_jpg.get_at((c, r))
        if color_key.r >=240 and color_key.g >= 240 and color_key.b >= 240:
            color_key.a = 0
        print(color_key)
        # if color_key in color_dict:
        #     color_dict[color_key] += 1
        # else:
        #     color_dict[color_key] = 1
# print(color_dict)