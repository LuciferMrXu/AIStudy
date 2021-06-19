#-*- conding:utf-8 -*-
from lxml import etree
import requests
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mydb
collection=db.TX社招

'''
    1.需求分析
        获取详细的招聘内容
            职位名称	职位类别	人数	地点	发布时间
        入口地址：https://hr.tencent.com/position.php
    2.源码分析
        获取所有的行的数据：//tr[@class='even'] | //tr[@class='odd']
        下一页的地址：//a[@id='next']
    3.代码实现
'''
starturl = 'https://hr.tencent.com/position.php'

'''
    一、请求入口地址
'''
headers = {
    # 浏览器的信息   身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
 }

page = 1


while True:
    num = 1
    response = requests.get(starturl,headers = headers).text

    '''
        二、提取内容
    '''
    # 解析源码
    html = etree.HTML(response)

    # 获取所有的行
    tr = html.xpath("//tr[@class='even'] | //tr[@class='odd']")




    # 获取下一页
    nextPage = html.xpath("//a[@id='next']/@href")

    # 遍历获取的每一行的内容
    jobDic = {}
    for i in tr:
        jobDic['title'] = i.xpath('string(td[1])')
        jobDic['type'] = i.xpath('string(td[2])')
        jobDic['num'] = i.xpath('string(td[3])')
        jobDic['address'] = i.xpath('string(td[4])')
        jobDic['date'] = i.xpath('string(td[5])')


        print('第{0}页第{1}条信息'.format(page,num))

        num += 1
        time.sleep(1)

        # 保存数据
        # with open('tencent.txt','a+',encoding='utf-8') as file:
        #     file.write(jobDic['title']+'::')
        #     file.write(jobDic['type']+'::')
        #     file.write(jobDic['num']+'::')
        #     file.write(jobDic['address']+'::')
        #     file.write(jobDic['date']+'\n')
        collection.insert(jobDic)
        jobDic.clear()



    # 翻页 获取下一页的地址
    if nextPage[0] == 'javascript:;':
        break
    else:
        starturl = 'https://hr.tencent.com/'+nextPage[0]
        page+=1


