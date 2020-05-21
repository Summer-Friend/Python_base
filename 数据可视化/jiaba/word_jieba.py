'''
@Author: your name
@Date: 2020-03-03 20:11:54
@LastEditTime: 2020-03-04 15:57:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\数据可视化\word_jieba.py
'''
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

'''
str = "明明知识点都熟记于心，可是在考试的时候脑子一片空白，什么都想不起来了"
#使用自定义字典
#jieba.load_userdict('dict.txt') 
ex_list1 = jieba.cut(str)
ex_list2 = jieba.cut(str , cut_all= True)
ex_list3 = jieba.cut_for_search(str)
print("精准模式:"+'/'.join(ex_list1)) 
print("全模式:"+'/'.join(ex_list2))
print("搜索引擎模式："+'/'.join(ex_list3))
'''
# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open(r'E:\vscode_code\vscode_python_test\数据可视化\jiaba\stopwords.txt', 'r', encoding='UTF-8') as f:
        str_text = f.read()
        #unicode_text = unicode(str_text, 'utf-8')  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。貌似不加也没事
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格

# 打开词源的文本文件
#这里如果不加encoding='UTF-8'会报错
#UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 4: illegal multibyte sequence
text = open(r'E:\vscode_code\vscode_python_test\数据可视化\jiaba\word.txt', 'r', encoding='UTF-8').read()

text = stop_words(text)

wc = WordCloud(background_color='white',  # 背景颜色,什么yellow啥的也行
               max_words=1000,  # 最大词数
               #mask=mask,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )

wc.generate(text)
# 基于彩色图像生成相应彩色
#image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云

#plt.axis('off')
plt.show()

