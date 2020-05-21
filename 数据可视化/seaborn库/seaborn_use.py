'''
@Author: your name
@Date: 2020-01-31 20:57:35
@LastEditTime: 2020-03-19 13:05:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\seaborn_use.py
'''
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

'''
sns.set()
#构建数据
#每次运行代码时设置相同的seed，则每次生成的随机数也相同，如果不设置seed，则每次生成的随机数都会不一样
np.random.seed(0)
x = np.random.randn(100)
"""
案例1：显示默认绘图，其中包含内核密度估计值和直方图
"""
#g = sns.FacetGrid(data_salary, row="teacher_type", size=4, aspect=2, xlim=(0,20))
#g.map(sns.distplot, "salary_clean", rug=False)

#多个图
fig, axes = plt.subplots(1,2)
sns.distplot(x, ax = axes[0], kde=True,hist=True)
sns.kdeplot(x, ax = axes[1], shade=True)     
plt.show()
'''

sns.set()
rs = np.random.RandomState(10)
d = rs.normal(size=100)
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
sns.distplot(d, color="m", ax=axes[1, 1])
plt.show()

