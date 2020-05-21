'''
@Author: your name
@Date: 2020-01-18 20:52:01
@LastEditTime : 2020-01-18 20:53:57
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\format使用.py
'''
print("{} {}".format("hello", "world"))    # 不设置指定位置，按默认顺序
print("{1} {0} {1}".format("hello", "world") ) # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的