'''
@Author: your name
@Date: 2020-01-29 17:10:47
@LastEditTime : 2020-01-30 19:22:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\settings.py
'''
class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船剩余数量设置
        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        #限制子弹数量
        self.bullet_allowed = 5
        #外星人出界后的修正速度
        self.fleet_drop_speed = 10
        
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #得分提高倍数
        self.score_scale = 2
        
        self.initial_dynamic_settings()
        
    def initial_dynamic_settings(self):
        #初始化速度
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 0.5
        #1表示右移，-1表示左移
        self.fleet_direction = 1
        #计分
        self.alien_points = 50
        
    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points*self.score_scale)
        