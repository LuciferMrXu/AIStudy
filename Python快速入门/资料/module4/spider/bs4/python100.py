#-*- conding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

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
response = requests.get(starUrl,headers = headers).content.decode('utf-8')
# print(response)

# 解析 文档
soup = BeautifulSoup(response,'lxml')

# 提取 100个 a 链接
link = []
for i in soup.find(id = 'content').ul.find_all('a'):
    link.append(i['href'])
# print(link[0])


num = 1
# 请求100个 a 链接
for a in link:
    print('第{0}道题'.format(num))
    result = requests.get('http://www.runoob.com'+a,headers = headers).content.decode('utf-8')
    # print(result)

    # 解析源代码
    html = BeautifulSoup(result,'lxml')
    # print(html)

    # 提取内容
    content = {}
    # 标题
    content['Title'] = html.find(id="content").h1.string
    # print(content['Title'])

    # 题目
    content['Subject'] = html.find(id="content").find_all('p')[1].text
    # print(content['Subject'])

    # 程序分析
    content['Analysis'] = html.find(id="content").find_all('p')[2].text
    # print(content['Analysis'])

    # 源代码
    try:
        content['code'] = html.find(class_="hl-main").text
    except:
        content['code'] = html.find('pre').text
    # finally:
    #     print(content['code'])

    # 保存内容
    with open('py100.txt','a+',encoding='utf-8') as file:
        file.write(content['Title']+'\n')
        file.write(content['Subject']+'\n')
        file.write(content['Analysis']+'\n')
        file.write(content['code']+'\n')
        file.write('*'*80+'\n')

    num+=1
