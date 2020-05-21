'''
@Author: your name
@Date: 2020-01-13 17:09:26
@LastEditTime : 2020-01-19 15:50:50
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\ceshi.py
'''
import requests
from lxml import etree

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
def crawl(url):
    response = requests.get(url,headers=headers)
    selector = etree.HTML(response.text)
    book=selector.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]')
    ''' 
    for element in book:
        name = element.xpath('div[1]/a/text()')[0]
        author = element.xpath('p[1]/text()')[0]
        star = element.xpath('div[2]/span[2]/text()')[0]
        
        name = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/text()')[0]
        author = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[1]/text()')[0]
        star = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[2]/text()')[0]
        print(name," ",author," ",star)
        '''
    name = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/text()')[0]
    author = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[1]/text()')[0]
    star = selector.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[2]/text()')[0]
    print(name," ",author," ",star)                      

if __name__=='__main__':
    for i in range(10):
     url='https://book.douban.com/top250?start={}'.format(i*25)
     print('第{}页爬取完毕'.format(i+1))
     crawl(url)