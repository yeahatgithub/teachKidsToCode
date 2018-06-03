# @Time    : 2018/6/2 16:04
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCORE_LABEL_COLOR = WHITE
SCORE_COLOR = (255, 0, 0)
WIDTH = 1200
HEIGHT = 800
BAN_WIDTH = 100
BAN_HEIGHT = 25
MAX_LIVES = 5
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("打乒乓")
    random.seed(int(time.time()))
    looping = True
    clock = pygame.time.Clock()
    smiley_pic = pygame.image.load("smiley-256x256.png").convert_alpha()
    smiley_pic = pygame.transform.scale(smiley_pic, (40, 40))  # 会缩放图片
    game_state = GameState(smiley_pic, screen)

    while looping:
        looping = check_events(game_state)

        screen.fill(BLACK)
        game_state.smiley.draw()
        game_state.smiley.update()

        game_state.paddle.update(pygame.mouse.get_pos())
        if game_state.paddle.has_hitted(game_state.smiley):
            game_state.add_score(1)
            game_state.smiley.bounce_y()
        if game_state.smiley.touch_bottom():
            if game_state.num_lives > 0:
                game_state.lose_life()
                game_state.smiley.reset()
            if game_state.num_lives == 0:
                game_state.stop()

        game_state.paddle.draw()
        draw_lives_score(screen, game_state.num_lives, game_state.score)
        if game_state.stopped:
            draw_restart_tip(screen)
        clock.tick(40)
        pygame.display.update()

def check_events(game_state):
    looping = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looping = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state.stopped:
                game_state.restart_game()   #game_state是可变对象

    return looping

def draw_lives_score(screen, num_lives, score):
    draw_lives(screen, num_lives)
    draw_score(screen, score)

def draw_lives(screen, num_lives):
    lives_label_font = pygame.font.SysFont('simhei', 28)  # 换成'arial'，无法显示中文。
    lives_label_surface = lives_label_font.render(u'生命：', False, SCORE_LABEL_COLOR)
    lives_label_position = (WIDTH // 2 - 100, 20)
    screen.blit(lives_label_surface, lives_label_position)

    lives_font = pygame.font.SysFont('arial', 28)
    lives_surface = lives_font.render(str(num_lives), False, SCORE_COLOR)
    lives_position = (WIDTH // 2 - 20, 20)
    screen.blit(lives_surface, lives_position)


def draw_score(screen, score):
    score_label_font = pygame.font.SysFont('simhei', 28)  # 换成'arial'，无法显示中文。
    score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
    score_label_position = (WIDTH // 2 + 20, 20)
    screen.blit(score_label_surface, score_label_position)

    score_font = pygame.font.SysFont('arial', 28)
    score_surface = score_font.render(str(score), False, SCORE_COLOR)
    score_position = (WIDTH // 2 + 100, 20)
    screen.blit(score_surface, score_position)

def draw_restart_tip(screen):
    stop_font = pygame.font.SysFont('simhei', 32)
    stop_surface = stop_font.render('游戏结束', False, WHITE)
    stop_position = (WIDTH // 2 - 40, HEIGHT // 2 - 20)
    screen.blit(stop_surface, stop_position)

    tip_font = pygame.font.SysFont('simhei', 24)
    tip_surface = tip_font.render('按空格键继续', False, WHITE)
    tip_position = (WIDTH // 2 - 50, HEIGHT // 2 + 30)
    screen.blit(tip_surface, tip_position)

class Smiley():
    def __init__(self, pic, screen):
        self.xvel = random.randrange(-10, 10)
        self.yvel = random.randrange(-10, 10)
        while self.yvel == 0:
            self.yvel = random.randrange(-10, 10)
        self.xpos = 300
        self.ypos = 300
        self.image = pic
        self.rect = self.image.get_rect()
        self.scale = self.rect.w
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x + self.scale >= self.screen.get_width() or self.rect.x <= 0:
            self.xvel = -self.xvel * 1.1
        if self.rect.y + self.scale >= self.screen.get_height():
            self.yvel = -self.yvel
        elif  self.rect.y <= 0:
            self.yvel = -self.yvel + 1

    def stop(self):
        self.xvel = 0
        self.yvel = 0

    def touch_bottom(self):
        return self.rect.y + self.scale >= self.screen.get_height()

    def bounce_x(self):
        self.xvel = -self.xvel

    def bounce_y(self):
        self.yvel = -self.yvel

    def reset(self):
        if self.xvel < 0:
            self.xvel = -5
        else:
            self.xvel = 5
        self.yvel = -5


class Paddle():
    def __init__(self, screen):
        self.screen = screen

    def update(self, mouse_pos):
        self.x = mouse_pos[0] - BAN_WIDTH // 2
        self.y = mouse_pos[1] - BAN_HEIGHT // 2

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, BAN_WIDTH, BAN_HEIGHT))

    def has_hitted(self, smiley):
        bottom_y = smiley.rect.y + smiley.rect.h
        middle_x = smiley.rect.x + smiley.rect.w // 2
        if bottom_y >= self.y and bottom_y <= self.y + BAN_HEIGHT and smiley.yvel > 0:
            if middle_x >= self.x and middle_x <= self.x + BAN_WIDTH:
                return True
        return False

class GameState():
    def __init__(self, smiley_pic, screen):
        self.num_lives = MAX_LIVES
        self.score = 0
        self.image = smiley_pic
        self.smiley = Smiley(smiley_pic, screen)
        self.paddle = Paddle(screen)
        self.screen = screen
        self.stopped = False

    def add_score(self, score):
        self.score += score

    def lose_life(self):
        self.num_lives -= 1

    def restart_game(self):
        self.num_lives = MAX_LIVES
        self.score = 0
        self.smiley = Smiley(self.image, self.screen)

    def stop(self):
        self.smiley.stop()
        self.stopped = True

if __name__ == "__main__":
    main()
