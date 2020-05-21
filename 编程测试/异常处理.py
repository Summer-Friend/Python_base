'''
@Author: your name
@Date: 2020-01-18 17:17:47
@LastEditTime : 2020-01-18 19:54:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\异常处理.py
'''
try:
    #若是未出现，则自动创建
    #换行符\n注意
    fh = open("vscode_python_test\编程测试\测试.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!\n")
    fh.write("这是第二行")
#except(Exception1[, Exception2[,...ExceptionN]]]):
#发生以上多个异常中的一个，执行这块代码
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
  
#普通的写文件操作
#fh = open("vscode_python_test\编程测试\测试.txt", "w")
#fh.write("这是一个测试文件，用于测试异常!!")
# 定义函数
def temp_convert(var):
    try:
        print ("转换成功")
        return int(var)
    except ValueError:
        print ("参数没有包含数字\n")
    else:
        print ("success")

# 调用函数
temp_convert(2)
'''
try:
    x='x'
    print ("转换成功11111")
except ValueError:
    print ("参数没有包含数字\n")
else:
    print ("success")
'''
#这个return语句只能在函数中使用，不然报错： 'return' outside function 
#同时，和c++一样，return代表了函数的结束，后面的语句不再实现
def heihei(x):
    y=1
    print("haha")
    return int(x)+y
    print("niubi")
z=heihei(2)
print(z)
birthday=input("choose a number:")