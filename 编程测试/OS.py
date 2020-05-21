'''
@Author: your name
@Date: 2020-01-18 19:54:47
@LastEditTime : 2020-01-18 19:58:42
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\OS.py
'''
import os, sys

# 假定 /tmp/foo.txt 文件存在，并有读写权限

ret = os.access("vscode_python_test\编程测试\测试.txt", os.F_OK)
print ("F_OK - 返回值 %s"% ret)

ret = os.access("vscode_python_test\编程测试\测试.txt", os.R_OK)
print ("R_OK - 返回值 %s"% ret)

ret = os.access("vscode_python_test\编程测试\测试.txt", os.W_OK)
print ("W_OK - 返回值 %s"% ret)

ret = os.access("vscode_python_test\编程测试\测试.txt", os.X_OK)
print ("X_OK - 返回值 %s"% ret)