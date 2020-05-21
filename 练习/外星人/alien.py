'''
@Author: your name
@Date: 2020-02-15 13:31:39
@LastEditTime: 2020-02-15 13:31:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\alian.py
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化外星人图像并设定起始位置
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        #加载图像并设置rect属性
        self.image=pygame.image.load(r'E:\vscode_code\vscode_python_test\练习\外星人\敌人0.png')
        self.rect=self.image.get_rect()
        
        #将外星人放在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x=float(self.rect.x)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """向左或向右移动外星人"""
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)