'''
@Author: your name
@Date: 2020-03-04 11:26:58
@LastEditTime: 2020-03-04 15:54:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\jiaba\test.py
'''
import jieba 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

a = ['alevel','ok','ok','right','boy','cat','啊行吧', '好吧', 'right', 'right']
b = (' '.join(a))
wc = WordCloud(background_color = 'white').generate(b)

plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
#plt.show()

text = '完了尼玛我炸了'
str_text = '我炸了凉了凉了'
word = jieba.cut(text, cut_all=False)

for ele in word:
    if ele not in str_text:
        print(ele+'a')
