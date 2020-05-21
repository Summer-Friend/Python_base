'''
@Author: your name
@Date: 2020-01-20 13:04:10
@LastEditTime: 2020-03-04 16:58:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\测试.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
s=[1,4,9,16,25,16,9,4,1]
plt.plot(s)
plt.title('图表', fontsize = 24)
plt.xlabel('横坐标', fontsize = 14)
plt.ylabel('纵坐标', fontsize = 14)
plt.show()
