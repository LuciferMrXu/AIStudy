# -*- conding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
mydb = client['mydb']
Python100例 = mydb['Python100例']
'''
    1.明确需求
        爬去python100例
            标题
            题目
            程序分析
            源代码
    2.分析源码
        入口地址：http://www.runoob.com/python/python-100-examples.html
        1.获取100道题的a链接
        2.分别请求这个100个链接获取对应的详细页面

    3.代码实现
'''

starUrl = 'http://www.runoob.com/python/python-100-examples.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 请求入口地址 获取100个A链接的href
response = requests.get(starUrl, headers=headers).content.decode('utf-8')
# print(response)

# 解析 文档
soup = BeautifulSoup(response, 'lxml')
# 提取 100个 a 链接
link = []
for i in soup.select('#content ul a'):
    link.append(i['href'])
print(link)


num = 1
# 2. 请求100个 a 链接
for a in link:
    print('第{0}道题'.format(num))
    result = requests.get('http://www.runoob.com' + a, headers=headers).content.decode('utf-8')

    # 解析源代码
    html = BeautifulSoup(result, 'lxml')

    # 提取内容
    content = {}
    # 标题
    content['题号'] = html.select("#content h1")[0].text

    # 题目
    content['Title'] = html.select("#content p")[1].text

    # 程序分析
    content['Analysis'] = html.select("#content p")[2].text

    # 源代码
    try:
        content['Subject'] = html.select(".hl-main")[0].text
    except:
        content['Subject'] = html.select('pre')[0].text

    # 保存内容
    data = {
        '题号':content['题号'],'Title': content['Title'],'Analysis':content['Analysis'],'Subject':content['Subject']
    }

    Python100例.insert(data)
    num+=1