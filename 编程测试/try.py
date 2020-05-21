'''
@Author: your name
@Date: 2020-01-17 16:10:04
@LastEditTime : 2020-01-17 16:12:11
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\try.py
'''
a='abc'
try:
    print(a[9])
except IOError as e:
    print('AAA')
except IndexError as e:
    print('BBB')
else:
    print('CCC')
finally:
    print('DDD')
#上面a[9] 会导致IndexError，即try语句块报IndexError异常，
# 那么去第一个except找对应的错误，第一个是IOError，
# 不匹配，继续从下面的except找，第二个是IndexError，匹配，
# 执行该语句块，打印‘BBB’，然后打印finally语句。