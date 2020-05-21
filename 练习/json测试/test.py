'''
@Author: your name
@Date: 2020-02-29 10:38:53
@LastEditTime: 2020-02-29 10:39:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\json测试\test.py
'''
import json 
import pandas as pd 

df = pd.DataFrame()
with open(r'vscode_python_test\练习\json测试\btc_json_2017.json','r',encoding = 'utf-8')as f:
     data = json.load(f)
df = pd.DataFrame(data)
print(df.head())