'''
@Author: your name
@Date: 2020-01-28 15:19:23
@LastEditTime : 2020-01-28 15:29:48
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\random_walk.py
'''
from random import choice
class Randomwalk():
    def __init__(self,num=5000):
        self.num=num
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        while len(self.x_values)<self.num:
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            
            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
            
            if x_step==0 and y_step==0:
                continue
            
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    