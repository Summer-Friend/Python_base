'''
@Author: your name
@Date: 2020-02-15 12:46:14
@LastEditTime: 2020-02-15 12:46:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\bullet.py
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    """管理子弹"""
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        
        #创建一个矩形子弹
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储位置
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        self.y -=self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)