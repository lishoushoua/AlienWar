import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # 加载外星人图像
        self.image = pygame.image.load('images/reallyPig.bmp')
        self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect()
        # 外星人初始位置
        # self.rect.x = self.screen_rect.centerx
        # 左边距设置为外星人的宽度
        self.rect.x = self.rect.width
        # 上边距设置为外星人的高度
        self.rect.y = self.rect.height
        # 存储外星人准确位置
        self.x = float(self.rect.x)

    def biltme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # 如果外星人位于屏幕边缘，就返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return  True


    def update(self):
        # 向右移动外星人
        self.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction
        self.rect.x = self.x
