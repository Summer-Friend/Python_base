'''
@Author: your name
@Date: 2020-01-28 15:18:43
@LastEditTime : 2020-01-28 15:29:10
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\随机漫步.py
'''
import matplotlib.pyplot as plt 
from random_walk import Randomwalk
rw=Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()