'''
@Author: your name
@Date: 2020-02-06 09:26:11
@LastEditTime : 2020-02-06 15:53:54
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\json测试\another.py
'''
import requests
import json
import pygal

#json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
#req = requests.get(json_url)

with open (r'vscode_python_test\练习\json测试\btc_json_2017.json') as f:
    #f.write(req.text)
    btc_data = json.load(f)
    #print(btc_data)

#print(req.json())
'''
#列表分解
for btc_dict in btc_data:
    """   #这个多行注释是分别对应的
    date=btc_dict['date']
    month=btc_dict['month']
    week=btc_dict['week']
    weekday=btc_dict['weekday']
    close=btc_dict['close']
    """
    #上下两种用法一样
    date=btc_dict.get('date')
    month=btc_dict.get('month')
    week=btc_dict.get('week')
    weekday=btc_dict.get('weekday')
    close=btc_dict.get('close')
    #print('{}is month{}week,{},the close price is {}RMB'.format(date,month,week,weekday,close))
'''
    
def btc_close_2017_01():
    #filename = "btc_close_2017.json"
    with open(r'vscode_python_test\练习\json测试\btc_json_2017.json') as f:
        btc_data = json.load(f)
    for btc_dict in btc_data:
        date = btc_dict['date']
        month = btc_dict['month']
        week = btc_dict['week']
        weekday = btc_dict['weekday']
        close = btc_dict['close']
        print ("{} is month {} week{},{},the close price is {}RMB".format(date,month,week,weekday,close))

# 将字符转化为数字
def btc_close_2017_02():
    #filename = "btc_close_2017.json"
    with open(r'vscode_python_test\练习\json测试\btc_json_2017.json') as f:
        btc_data = json.load(f)
    for btc_dict in btc_data:
        date = btc_dict['date']
        month = int(btc_dict['month'])
        week = int(btc_dict['week'])
        weekday = btc_dict['weekday']
        close = int(float(btc_dict['close']))
        print ("{} is month {} week{},{},the close price is {}RMB".format(date,month,week,weekday,close))

# 绘制收盘价折线图
def btc_close_2017_03():
    #filename = "btc_close_2017.json"
    with open(r'vscode_python_test\练习\json测试\btc_json_2017.json') as f:
        btc_data = json.load(f)
    dates = []
    month = []
    week = []
    weekday = []
    close = []
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        month.append(int(btc_dict['month']))
        week.append(int(btc_dict['week']))
        weekday.append(btc_dict['weekday'])
        close.append(int(float(btc_dict['close'])))

    line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
    line_chart.title = "收盘价（￥）"
    line_chart.x_labels = dates
    N = 20
    line_chart.x_labels_major = dates[::N]
    line_chart.add("收盘价",close)
    line_chart.render_to_file('收盘价折线图.svg')

import math
#导入python标准库中模块itertools的函数groupby
from itertools import groupby
#计算收盘价均值
def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    #将x轴,y轴数据合并排序再用groupby分组，分组之后求出均值
    for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
        y_list = [v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    #将xy_map中x轴,y轴数据分离
    x_unique,y_mean = [*zip(*xy_map)]
    #实例化折线图对象并画图
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+".svg")
    return line_chart

def btc_close_2017_04():
    #filename = "btc_close_2017.json"
    with open(r'vscode_python_test\练习\json测试\btc_json_2017.json') as f:
        btc_data = json.load(f)
    dates = []
    month = []
    week = []
    weekday = []
    close = []
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        month.append(int(btc_dict['month']))
        week.append(int(btc_dict['week']))
        weekday.append(btc_dict['weekday'])
        close.append(int(float(btc_dict['close'])))

    #x轴日期标签旋转20度，不用显示x轴所有标签
    line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
    line_chart.title = "收盘价对数变换（￥）"
    line_chart.x_labels = dates
    #x轴每隔20天显示一次
    N = 20
    line_chart.x_labels_major = dates[::N]
    #利用对数变换剔除非线性趋势之后，整体上涨更接近线性增长
    close_log = [math.log10(_) for _ in close]
    line_chart.add("log收盘价",close_log)
    line_chart.render_to_file('收盘价对数变换折线图.svg')

    # 收盘价月日均图
    idx_month = dates.index('2017-12-01')
    line_chart_month = draw_line(month[:idx_month],close[:idx_month],'收盘价月日均图','月日均值')


btc_close_2017_04()
"""
btc_close_2017_03()
btc_close_2017_02()
btc_close_2017_01()
"""