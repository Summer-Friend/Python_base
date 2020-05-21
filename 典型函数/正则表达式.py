'''
@Author: your name
@Date: 2020-01-19 20:43:31
@LastEditTime: 2020-03-28 20:59:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\正则表达式.py
'''
import re
import pandas as pd
import numpy as np 

#字符串中的正则使用##########################################
#1.第一个匹配大写，第二个匹配小写，因为有*可以匹配一位或多位
ret = re.match("[A-Z][a-z]*","MMMnMMnnM")
#print(ret.group())
#第一个匹配大写，第二个匹配小写，最后一位匹配M
ret = re.match("[A-Z][a-z]+M","TnnbuMM")
#print(ret.group())
#2.匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线，如果不到八位那就没有匹配成功
ret = re.match("[a-zA-Z0-9_]{8,20}","11155ff66")
#print(ret.group())

string = '<input type="submit" id="su" value="百度一下" class="bg s_btn">'

#字符串换行
string2 = '<a title="天融信2020年春季校园招聘" style="padding:10px 20px;margin-left:-20px;word-wrap: break-word;'\
          'word-break: break-all;" href="/student/jobs/LsWiZqx4VgrP8ofduJ3oEt/detail.html" target="_blank">天融信2020年春季校园招聘</a>'

pattern = re.compile(r'<input type="submit" id="(.*?)" value="(.*?)" class="bg s_btn">')
pattern2 = re.compile(r'<a title="(.*?)" style=.*?target="_blank">天融信(.*?)年春季校园招聘</a>')

result = pattern.findall(string)
result2 = pattern2.findall(string2)
x = result
x2 = result2
print(x)
print(x2)

'''
#3.不用pandas的普通字符串利用括号的区别
#https://www.cnblogs.com/xiaohaodeboke/p/11777984.html
string="abcdefg  acbdgef  abcdgfe  cadbgfe"
#带括号与不带括号的区别
regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
#输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
#输出：['abcdefg', 'abcdgfe']

regex2=re.compile("\w+\s+\w+")
print(regex2.findall(string))
#输出：['abcdefg  acbdgef', 'abcdgfe  cadbgfe']




#pandas里面的正则###############################################
#1.extract使用  #https://blog.csdn.net/claroja/article/details/64929819
#如果提取的规则结果有多组，则会返回数据框，不匹配的返回NaN
s3 = pd.Series(['a1', 'b2', 'c3'])
print(s3.str.extract('([ab])(\d)'))
#print(pd.Series(s3).str.extract('([ab])(\d)', expand=False))
print(pd.Series(['a1', 'b2', 'c3']).str.extract('([ab])(\d)', expand=False))

#2.contains使用正则表达式，https://www.jianshu.com/p/805f20ac6e06
#可以将符合的数据进行提取
#print(s3.str.contains('([ab])(\d)'))
#print(s3[s3.str.contains('([ab])(\d)')].unique())

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':['1.5','1.7','3.6','2.4','2.9'],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
frame = pd.DataFrame(data)

#series是将数据形成一个个的列表
#正则记得加括号
#print(pd.Series(data['pop']).str.extract('(\d+\.?\d)'))

#series和dataframe#####################################################################
#注意：extract在dataframe中也适用，不需要再次series，其实series相当于dataframe的一列而已
#所以，诸如head，unique,describe对于dataframe可用的对于series也可用
#print(frame['pop'].str.extract('(\d+\.?\d)'))
#这两个结果就是一样的
#print(pd.Series(data['pop']),'\n', frame['pop'])

#打换行符的时候，需要用引号弄起来哦
data2 = ['1.5','1.7','3.6','2.4','2.9']
#纯数字列表无法用.str方法
#data2 = [1.5,1.7,3.6,2.4,2.9]

#print(data2, '\n' , pd.Series(data2))
data3 = pd.Series(data2)
#print(data3.str.extract('(\d+\.?\d)'))


#re在字符串和pandas中的应用######################################################
#若是字典，那么键值将充当索引
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}


data = pd.Series(data)
#提取，但是.str只针对dataframe或series形式
#print(data.str[:5])

data.isnull()
data.str.contains('gmail')
pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([a-z]{2,4})'

#这里用加号和括号就可以把正则提取的东西分别存储在列表中
#print(data.str.extract('([a-z0-9._%+-]+)(@+)([a-z0-9.-]+)\\.([a-z]{2,4})'))

#使用正则表达式，还可以加上任意re选项（如IGNORECASE）,这个貌似不看大小写吧好像
#print(data.str.findall(pattern, flags=re.IGNORECASE))

#获取true或false
matches = data.str.match(pattern, flags=re.IGNORECASE)



#例子########################################################
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    #'https://([\w.])+'也是对的
    return url 
      
 
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))
'''
