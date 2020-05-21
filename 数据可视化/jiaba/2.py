'''
@Author: your name
@Date: 2020-03-03 22:11:08
@LastEditTime: 2020-03-04 08:47:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\jiaba\2.py
'''
import pandas as pd 
import numpy as np 
#from pyecharts import WordCloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from PIL import Image


text = '''文案 文案
The  抱抱 Zen of LOVE 抱抱 Python, 快乐 by Tim Peters
公众号 公众号 Python 最好的 语言 语言
一辈子 is better LOVE than 一辈子.
喵小姐 is 爱你 than  implicit.爱你 喵小姐
蟹先生 is 爱你 than complex.
一辈子 is 蟹先生  than complicated.
二中 is 喵小姐 我想你了 than nested. 二中 蟹先生
清湖 is 胜于 than 清湖.
思旺 counts. 想你
Special 喵小姐 我想你了 aren't special enough 思旺 break 思旺 rules.
别生气 practicality beats 厨艺好.
Errors should 我想你了 never pass 小龙虾 silently. 运营
别生气 explicitly 好不好. LOVE
In the face of ambiguity, 程序员 the 厨艺好 to guess.龙华 龙华
There 快乐 should be one-- 我想你了 and preferably 红烧肉 only one 小龙虾--obvious way to do it.运营
Although 共享单车 way may not 我想你了 be obvious at first unless you're Dutch. 新媒体 地铁
Now is better 红烧肉 than never.
程序员 Although 共享单车 is often 高铁 than 东莞 now. 高铁 地铁
If the implementation 想你 is hard to explain, it's a bad idea. 想你了
If 成都 implementation is 想你 easy to explain, it may be a good idea.
Namespaces are 端午one 端午 honking great idea -- 成都 do more of those! 想你了
深圳 晚安 深圳 新媒体
'''

# the font from github: https://github.com/adobe-fonts
font = r'C:\Windows\Fonts\simfang.ttf'
#上下两种都行
mask = np.array(Image.open(r'E:\vscode_code\vscode_python_test\数据可视化\jiaba\20190131160157591.jpg'))
mask2 = plt.imread(r'E:\vscode_code\vscode_python_test\数据可视化\jiaba\20190131160157591.jpg')

wc = WordCloud(collocations=False, width=1400, height=1400, margin=2, mask = mask).generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

#wc.to_file('show_Chinese.png')  # 把词云保存下来 
