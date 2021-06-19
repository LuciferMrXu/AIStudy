#-*- conding:utf-8 -*-
import requests
import time
import json
import re

pn = 0
rn = 30
gsm = str(hex(pn))[-2:]
times = int(time.time()*1000)
qw = input('请输入关键字：')
page = 1
while True:
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={0}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={1}&rn=30&gsm={2}&{3}='

    # 发送请求
    print(url.format(qw,pn,gsm,times))
    responses = requests.get(url.format(qw,pn,gsm,times)).content.decode('utf-8','ignore')
    responses = json.loads(responses)
    num = 1
    for i in responses['data']:
        # 获取图片名称
        if i :
            imgName = i['fromPageTitleEnc']
            pattern = re.compile("[\?\\\|,()\">]+")
            imgName = pattern.sub('',imgName)
            print(imgName)
            # 获取图片地址
            middleURL = i['middleURL']
            # 发送请求获取图片资源
            image = requests.get(middleURL,stream = True).raw.read()
            # 保存图片

            with open('img/'+imgName+'.jpg','wb') as file:
                file.write(image)

            print('第{0}页第{1}张图片'.format(page,num))
            num+=1

    if pn<responses['displayNum']:
        pn+=30
        gsm = str(hex(pn))[-2:]
        times = int(time.time() * 1000)
        page+=1
    else:
        break


