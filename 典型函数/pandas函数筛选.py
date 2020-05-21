'''
@Author: your name
@Date: 2020-02-16 19:23:56
@LastEditTime: 2020-02-28 19:22:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\典型函数\pandas函数筛选.py
'''
import pandas as pd
import numpy as np
import re

#针对于字符串的替换筛选###########################################
salary = ['8千-1万', '5千-8千', '面议', '1.5万-2万', '1.5万-3万', '1万-1.5万', '7千-1.5万',
       '1.5万-2.5万', '1万-2万', '8千-1.5万', '2.5万以上', '7千-1万', '3千-8千',
       '2千-1万', '5千-1万', '4千-1万', '5千-6千', '3千-5千', '2万-2.5万', '6千-1万']
salary = pd.Series(salary)

def process_k(data):
    if '千' in data:
        return float(data.replace('千', '')) * 1000
    elif '万' in data:
        return float(data.replace('万', '')) * 10000


def process_salary(data):
    if data == '面议':
        return np.nan
    if '万以上' in data:
        return float(data.replace('万以上', '')) * 10000
    if '千以下' in data:
        return float(data.replace('千以下', '')) * 1000
    if '-' in data:
        low, high = data.split('-')
        return (process_k(low) + process_k(high))/2
    
salary_clean = salary.apply(process_salary)
#salary_clean = salary_clean[salary_clean>10000]
print(salary_clean)
#print(salary_clean.unique())

#针对于数字和字符串的清洗筛选############################################
data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH']
}
frame = pd.DataFrame(data)


def get_salary_jlc(data):
    pat_jlc = r"(.*)K/MTH - (.*)K/MTH"
    if '00' in data:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2/1000
    else:
        low, high = re.findall(pattern=pat_jlc, string=data)[0]
        return (float(low)+float(high))/2
    
frame['salary_clean'] = frame['salary'].apply(get_salary_jlc)

#print(frame.head())
#print(frame['salary'].iloc[:3])
x = re.findall("(.*)K/MTH - (.*)K/MTH", '1000K/MTH - 20000K/MTH')
#print(x)
low, high = re.findall("(.*)K/MTH - (.*)K/MTH", '1000K/MTH - 20000K/MTH')[0]
#print(low,' ', high)
