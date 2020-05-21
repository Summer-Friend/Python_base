'''
@Author: your name
@Date: 2020-01-28 11:12:18
@LastEditTime : 2020-01-28 12:15:01
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\pygal_test.py
'''
import pygal
x=[]
y=[1,2]
x.append(y)
hist = pygal.Bar()
#hist.xlabels=['a','b']
hist.title="result"
hist.x_label_rotation=45
hist.x_labels=['a','b']
hist.add('res',y)
hist.render_to_file('visual.svg')
'''
import pygal                                                       # 导入 pygal
bar_chart = pygal.Bar()                                            # 创建一个换图对象
bar_chart.add('FirsrtTry', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # 添加一些值和对应的序列
bar_chart.add('SecondTry', [55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0])  # 再添加另一个序列
bar_chart.render_to_file('bar_chart.svg')    
''' 
