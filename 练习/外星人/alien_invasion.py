'''
@Author: your name
@Date: 2020-01-29 17:04:53
@LastEditTime : 2020-01-30 19:31:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\alian_invasion.py
'''
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf



def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")
    #bg_color=(230,230,230)
    
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    
    #统计游戏信息
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #刻画飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹和外星人的的编组
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个外星人，调试用的
    #alien = Alien(ai_settings,screen)
    
    #游戏主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        
run_game()