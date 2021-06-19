#-*- conding:utf-8 -*-
from lxml import etree
import requests
import time
import re
'''
    1.需求分析
        title gsmc gz address jy xl fuli
        入口地址：https://www.zhaopin.com/
        
    2.源码分析
        所有的职位分类标签：//div[@class='zp-jobNavigater-pop-list']/a
        职位详细列表：
        https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%96%E8%B4%B8%E5%8A%A9%E7%90%86&kt=3&lastUrlQuery=%7B%22jl%22:%22489%22,%22kw%22:%22%E5%A4%96%E8%B4%B8%E5%8A%A9%E7%90%86%22,%22kt%22:%223%22%7D
    3.代码实现
'''

# 1.获取职位标签
def get_job_tag(url):

    headers = {
        # 浏览器的信息   身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url, headers=headers).text

    # 解析源码
    HTML = etree.HTML(response)
    # 获取所有的职位分类标签
    job_tag = HTML.xpath("//div[@class='zp-jobNavigater__pop--list']/a/text()")
    return job_tag



# 2.获取职位信息
def get_job_info(url,start,kw):
    headers = {
        # 浏览器的信息   身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    info_html = requests.get(infoUrl.format(start,kw), headers=headers).json()

    job_Dic = {}

    for i in info_html['data']['results']:
        job_Dic['city'] = i['city']['items'][0]['name']
        job_Dic['companyName'] = i['company']['name']
        job_Dic['companySize'] = i['company']['size']['name']
        job_Dic['companyType'] = i['company']['type']['name']
        job_Dic['eduLevel'] = i['eduLevel']['name']
        job_Dic['emplType'] = i['emplType']
        job_Dic['jobName'] = i['jobName']
        job_Dic['jobType'] = i['jobType']['display']
        job_Dic['salary'] = i['salary']
        job_Dic['welfare'] = i['welfare']
        job_Dic['updateDate'] = i['updateDate']
        job_Dic['workingExp'] = i['workingExp']['name']

        # 保存
        if unique_data(job_Dic):
            job_Dic = clearn_data(job_Dic)
            save_data(job_Dic)

        # time.sleep(0.5)

    return info_html['data']['numFound']


# 过滤重复数据
companyList = []
jobNameList = []
def unique_data(data):
    if (data['jobName'] in jobNameList) & (data['companyName'] in companyList):
        return False
    else:
        companyList.append(data['companyName'])
        jobNameList.append(data['jobName'])
        return data


# 数据清洗
def clearn_data(data):
    # welfare
    data['welfare'] = '/'.join([str(i) for i in data['welfare']])

    # companySize
    pattern = re.compile('[\u4E00-\u9FA5]+')
    data['companySize'] = pattern.sub('',data['companySize'])


    return data


# 保存数据
def save_data(data):
    data = '::'.join([str(i) for i in data.values()])
    print(data)

    with open('zlzp.txt','a+',encoding='utf-8') as file:
        file.write(data+'\n')




if __name__ == '__main__':
    '''
        一、请求首页
    '''
    starturl = 'https://www.zhaopin.com/'
    job_tag_list = get_job_tag(starturl)

    '''
        二、获取职位详细列表页面
    '''

    start = 0

    page = 1
    while True:
        infoUrl = 'https://fe-api.zhaopin.com/c/i/sou?start={0}pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={1}&kt=3'
        numFound = get_job_info(infoUrl,start,job_tag_list[0])

        print('第{0}页'.format(page))
        if start<numFound:
            start+=60
            page+=1
            time.sleep(1)
        else:
            break





