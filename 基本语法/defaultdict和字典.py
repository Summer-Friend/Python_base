'''
@Author: your name
@Date: 2020-02-23 14:47:18
@LastEditTime: 2020-02-23 14:50:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\defaultdict.py
'''
#https://blog.csdn.net/weixin_30725467/article/details/97111675?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

import collections

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

# Use dict and setdefault    
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)

# Use dict
e = {}
for k, v in s:
    e[k] = v

##list(d.items())
##list(g.items())
##list(e.items())

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

#list(d.items())