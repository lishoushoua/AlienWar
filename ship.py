import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形(rect对象)
        self.image = pygame.image.load('images/pig.bmp')
        # 加载图像后，使用get_rect()获取相应surface的属性rect
        self.rect = self.image.get_rect()
        # 表示屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # 原点位于屏幕左上角 右下角的坐标(1200,800)
        # 要使游戏元素居中，可设置相应的rect对象的属性center、centerx或centery
        # 要使游戏元素与屏幕边缘对其，可使用属性top、bottom、left、right
        # 要使元素的水平或垂直位置，可使用属性x和y 分别是相应矩形左上角的x和y坐标
        # 飞船的中心的x坐标设置为屏幕的矩形的属性
        self.rect.centerx = self.screen_rect.centerx
        # 飞船下边缘的y坐标设置为表示屏幕的矩形的属性
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志 初始化false
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动标志移动飞船的位置 更新飞船的center值
        # self.rect.right表示飞船外接矩形的右边缘的x坐标  self.screen_rect.right屏幕右边缘
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        # 同理 保证飞船在屏幕内
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        # 飞船屏幕居中
        self.center = self.screen_rect.centerx