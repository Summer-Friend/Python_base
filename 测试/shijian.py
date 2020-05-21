'''
@Author: your name
@Date: 2020-01-19 16:04:59
@LastEditTime : 2020-01-19 16:06:52
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\测试\shijian.py
'''
import time  # 引入time模块
import calendar
ticks = time.time()
print ("当前时间戳为:", ticks)
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
#日历模块
cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)