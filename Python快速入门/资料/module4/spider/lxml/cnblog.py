#-*- conding:utf-8 -*-
from lxml import etree
import requests
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mydb
collection=db.blog
'''
    1.需求分析
        1.帖子标题
        2.获取帖子内容
    2.源码分析
        入口：https://www.cnblogs.com/
        获取帖子链接：//div[@class='post_item_body']/h3/a
        获取下一页：//div[@class='pager']/a[last()]/text()   获取文本及href属性
                  //div[@class='pager']/a[last()]/@href
                  
        帖子标题：//*[@id='cb_post_title_url']/text()
        帖子内容：string(//*[@id='cnblogs_post_body'])
    3.代码实现
'''

'''
    一、发送请求获取首页帖子 url
'''
starturl = 'https://www.cnblogs.com/'
# proxies = {
#     "http": "http://61.135.217.7:80",
# }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# page=1
num=1
while True:

    response = requests.get(starturl,headers = headers).text
    # print(response)

    # 解析源代码
    html = etree.HTML(response)

    # 获取帖子URL
    href = html.xpath("//div[@class='post_item_body']/h3/a/@href")
    # print(href)

    # 获取下一页的文本已经url
    nextPage = html.xpath("//div[@class='pager']/a[last()]/text()")
    # print(nextPage)
    nextPageUrl = html.xpath("//div[@class='pager']/a[last()]/@href")
    # print(nextPageUrl)

    '''
        二、获取每一篇帖子的内容及标题
    '''
    # num = 1
    for i in href:
        result = requests.get(i,headers = headers).text
        # 解析源码
        contents = etree.HTML(result)

        # 提取帖子标题
        title = contents.xpath("string(//*[@id='cb_post_title_url'])")


        # 提取详情内容
        info = contents.xpath("string(//*[@id='cnblogs_post_body'])")


        '''
            三、保存内容
        '''
        data={
            '序号':num,'标题':title,'内容':info
        }
        collection.insert(data)
        time.sleep(0.5)
        num += 1


        # with open('cnblogs.txt','a+',encoding='utf-8') as file:
        #     file.write(title[0]+'\n')
        #     file.write(info+'\n')
        #     file.write('='*80+'\n')
        # print('第{0}页第{1}篇帖子'.format(page,num))
        # time.sleep(0.5)
        # num+=1

    if nextPage[0] == 'Next >':
        starturl = 'https://www.cnblogs.com'+nextPageUrl[0]
        # page+=1
        print(starturl)
        time.sleep(1)
    else:
        break