'''
@Author: your name
@Date: 2020-02-13 12:57:17
@LastEditTime: 2020-02-29 18:59:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\进制.py
'''

print(int('1101',2))  #二进制转十进制：
print(bin(0o37))    #0o37   0：阿拉伯数字0   o：八进制表示
bin(0x33)   #十六进制
oct(0b10110011111)

#仅适用于格式化字符串，对于数字不适用，所以引号得用上
a = 2
print('%s' %a)
print('{}'.format(a))

#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
m = 'a'
m_ascii = ord(m)
print(m_ascii)
 
m_cha=chr(m_ascii)
print(m_cha)
 
m_ascii +=1
print(m_ascii)
 
m_cha=chr(m_ascii)
print(m_cha)

a = 2
print(a >> 1)

n = 3
print(int("{:032b}".format(n), 2))
print(type("{:032b}".format(n)))

x = '00002002'
n = (int(x,16))
y = ("{:032b}".format(n))
print(y[30:31])