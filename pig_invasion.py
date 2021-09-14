# 使用sys退出游戏
import sys
# 模块pygame包含开发游戏所需的功能
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建Setting实例
    ai_settings = Settings()
    # 创建游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("The  War")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建存储子弹的编组
    bullets = Group()
    # 创建一只猪
    # alien = Alien(ai_settings, screen)
    # 创建外星人编组
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, aliens, ship)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        gf.check_events(ship, ai_settings, screen, bullets, stats, play_button,aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(ai_settings, aliens, screen, ship, stats, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats)


run_game()
