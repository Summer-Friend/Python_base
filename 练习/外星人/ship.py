'''
@Author: your name
@Date: 2020-01-29 17:15:37
@LastEditTime : 2020-01-30 19:27:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\ship.py
'''
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        #self.image=pygame.image.load(r'E:\vscode_code\vscode_python_test\练习\外星人\微信图片.jpg')
        self.image=pygame.image.load(r'E:\vscode_code\vscode_python_test\练习\外星人\英雄.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        #将新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery = 600
        #self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        #允许移动
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
     
    #根据键盘确定飞船的位置   
    def update(self):
        '''
        #移动飞船
        if self.moving_right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center-=self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.rect.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.rect.centery+=self.ai_settings.ship_speed_factor
        '''    
        #防止飞船碰壁
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center-=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.centery > self.screen_rect.top:
            self.rect.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.rect.centery+=self.ai_settings.ship_speed_factor
            
        #更新rect对象
        self.rect.centerx=self.center
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        #飞船居中
        self.center = self.screen_rect.centerx
        