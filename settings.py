# 设置类
class Settings():
    # 存储猪头入侵所有设置的类

    def __init__(self):
        # 初始化游戏的设置
        self.screen_width = 600
        self.screen_height = 450
        # 设置背景色
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        # 飞船的速度 决定飞船在每次循环时最多移动多少距离
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 1
        self.ship_limit = 3
        self.fleet_drop_speed = 5
        # fleet_direction为1表示右移
        self.fleet_direction = 1
