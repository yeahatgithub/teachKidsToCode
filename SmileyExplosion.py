# @Time    : 2018/5/31 15:36
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
import random

def main():
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("笑脸")
    looping = True
    mouse_down = False

    clock = pygame.time.Clock()
    smiley_pic = pygame.image.load("good-900x900.png").convert_alpha()
    sprite_list = pygame.sprite.Group()

    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

        screen.fill(BLACK)
        sprite_list.update()   #调用每个sprite的update()
        sprite_list.draw(screen)   #绘制每一个sprite，image属性决定内容，rect属性决定显示位置和区域
        clock.tick(40)   #每秒不多于40帧
        pygame.display.update()   #刷新屏幕
        if mouse_down:
            speedx = random.randint(-5, 5)   #水平移动速度
            speedy = random.randint(-5, 5)   #垂直移动速度
            new_smiley = Smiley(screen, smiley_pic, pygame.mouse.get_pos(), speedx, speedy)
            sprite_list.add(new_smiley)   #加入精灵列表

    pygame.quit()

class Smiley(pygame.sprite.Sprite):   #继承pygame.sprite.Sprite类
    def __init__(self, screen, pic, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)   #调用父类的构造方法
        self.image = pic   #Sprite类有image属性
        self.scale = random.randrange(10, 100)   #图片的分辨率是 (self.scale, self.scale)。
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))  #会缩放图片
        self.rect = self.image.get_rect()   #Sprite类有rect属性，决定显示位置和显示区域
        self.pos = pos
        self.rect.x = pos[0] - self.scale / 2   #self.rect是包围图片的四边形。x是左上角的横坐标
        self.rect.y = pos[1] - self.scale / 2   #y是左上角的纵坐标。self.scale是边长
        self.xvel = xvel    #水平移动速度
        self.yvel = yvel    #垂直移动速度
        self.screen = screen

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > self.screen.get_width() - self.scale:
            self.xvel = -self.xvel   #水平方向上，弹回
        if self.rect.y <= 0 or self.rect.y > self.screen.get_height() - self.scale:
            self.yvel = -self.yvel   #垂直方向上，弹回


if __name__ == '__main__':
    main()


