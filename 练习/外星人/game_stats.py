'''
@Author: your name
@Date: 2020-02-15 14:56:56
@LastEditTime: 2020-02-15 14:56:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\game_stats.py
'''
class GameStats:
    def __init__(self,ai_settings):
        #初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #一开始处于非活动状态
        self.game_active = False
        
    def reset_stats(self):
        #剩下的飞船数目
        self.ship_left = self.ai_settings.ship_limit
        #计分
        self.score = 0
        