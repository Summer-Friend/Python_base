'''
@Author: your name
@Date: 2020-01-29 20:03:50
@LastEditTime: 2020-03-08 00:20:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\pyeceshi.py
'''
from pyecharts import Bar,Line
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
bar=Bar('我的第一个图表','副标题')
bar.add("服装",["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],[5,20,36,10,75,90])
bar.show_config()
bar.render('柱状图.html')

attr = ['学历不限\nAny education', '高中', '大专\nAssociate',
        '本科\nBachelor', '硕士\nMaster']
value1 = [13.9, np.NaN, 12.8, 16.3, 21.3]
value2 = [7.5, 4.4, 6.4, 9.2, 11.0]

bar = Bar("不同学历的英语外教与中教工资对比", width = 700,height=500)
bar.add("外教", attr, value1, xaxis_label_textsize=15, legend_top=30,
        yaxis_label_textsize=20, is_label_show=True)
bar.add("中教", attr, value2, xaxis_label_textsize=15, legend_top=30,
        yaxis_label_textsize=20, is_label_show=True)
bar.render('学历图.html')
print(np.NaN)
'''

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
#line.show_config()
line.render('折线图2.html')