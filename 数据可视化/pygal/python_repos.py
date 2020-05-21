'''
@Author: your name
@Date: 2020-01-28 15:37:40
@LastEditTime : 2020-01-28 17:24:18
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\python_repos.py
'''
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'#存储API调用的URL
r=requests.get(url) #获得URL对象
print("Status code:",r.status_code) #判断请求是否成功（状态码200时表示请求成功）
response_dict=r.json() #API返回json格式的信息（将响应存储到变量中）
print("Total repositories:",response_dict['total_count'])
#探索有关仓库的信息
repo_dicts=response_dict['items']
names,stars=[],[]     #获得项目的名称和星数
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
#可视化
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_lable_rotation=45,show_legend=False)#创建一条简单的条形图
chart._title='Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status Code:",r.status_code)
response_dict=r.json()
print("total repositors:",response_dict['total_count'])
repo_dicts=response_dict['items']
names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
#my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(my_config,style=my_style)
chart._title='most_stars_chart'
chart.x_labels=names
chart.add('stars',stars)
chart.render_to_file('python1_repos.svg')
