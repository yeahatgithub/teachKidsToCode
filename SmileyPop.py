# @Time    : 2018/5/31 15:36
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def main():
    pygame.init()
    pygame.mixer.init()
    pop = pygame.mixer.Sound("pop.ogg")
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("笑脸")
    looping = True

    clock = pygame.time.Clock()
    smiley_pic = pygame.image.load("good-900x900.png").convert_alpha()
    sprite_list = pygame.sprite.Group()
    smiley_created = 0
    smiley_popped = 0

    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:   #鼠标左键按下时为真
                    add_sprite(screen, smiley_pic, sprite_list)
                    smiley_created += 1
                elif pygame.mouse.get_pressed()[2]:  #鼠标右键按下时为真
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    if len(clicked_smileys) > 0:
                        pop.play()
                        smiley_popped += len(clicked_smileys)
                    sprite_list.remove(clicked_smileys)

        screen.fill(BLACK)
        sprite_list.update()   #调用每个sprite的update()
        sprite_list.draw(screen)   #绘制每一个sprite，image属性决定内容，rect属性决定显示位置和区域
        draw_created_popped(screen, smiley_created, smiley_popped)
        clock.tick(40)   #每秒不多于40帧
        pygame.display.update()   #刷新屏幕

    pygame.quit()

def draw_created_popped(screen, smiley_created, smiley_popped):
    if smiley_created > 0:
        c_p_font = pygame.font.SysFont('simhei', 24)
        c_p_text = '总数：' + str(smiley_created) + ',  刺破：' + str(smiley_popped)
        c_p_text += ',  比例：' + str(round(smiley_popped / smiley_created*100, 1)) + '%'
        c_p_surface = c_p_font.render(c_p_text, False, WHITE)
        c_p_position = (375, 20)
        screen.blit(c_p_surface, c_p_position)

def add_sprite(screen, smiley_pic, sprite_list):
    speedx = random.randint(-5, 5)  # 水平移动速度
    speedy = random.randint(-5, 5)  # 垂直移动速度
    new_smiley = Smiley(screen, smiley_pic, pygame.mouse.get_pos(), speedx, speedy)
    sprite_list.add(new_smiley)  # 加入精灵列表

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


