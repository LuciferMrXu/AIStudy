#-*- conding:utf-8 -*-
import requests
# GET请求   参数会显示在URL地址当中
# par = {'name':'joe','pwd':'123'}
# result = requests.get('http://httpbin.org/get',params= par) #测试get请求的汪涵
# print(result.text)
# print(result.status_code)

# {"args":{},   参数
#  "headers":{
#      "Accept":"*/*",
#      "Accept-Encoding":"gzip, deflate",
#      "Connection":"close",
#      "Host":"httpbin.org",
#      "User-Agent":"python-requests/2.18.4"
#  },
#  "origin":"116.231.254.2",
# "url":"http://httpbin.org/get"
# http://httpbin.org/get?name=joe&pwd=123
#  }


# GET请求添加头文件伪装浏览器
# headers = {
#     # 'referer':''    表示这个请求从哪里来的
#     # 'host':''
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# result = requests.get('http://httpbin.org/get',headers = headers) #测试get请求的网站
# print(result.text)
# print(result.status_code)

# 请求知乎网站
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# result = requests.get('https://www.zhihu.com',headers = headers)
# print(result.text)


# 解析json数据
# result = requests.get('https://github.com/timeline.json')
# print(result.json())   #将json字符串解析成dict

#GET请求，获取原始响应内容
# 下载音乐
# result = requests.get('http://dl.stream.qqmusic.qq.com/C400002Fjdnk0zz1T6.m4a?vkey=26172D9B9AEAB25FACC98F4CDEDA1E71669A7FE8FD538CCE6D19D8E6597AF29D33BBC348975FB708A2B80B37CBF6381FD34E197133A5F4CC&guid=1093240106&uin=0&fromtag=66',stream = True).raw.read()
# with open('aaaa.mp3','wb') as file:
#     file.write(result)


# 下载图片
# result = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530963714881&di=10af3937f6c51760948a6efe63552b4e&imgtype=0&src=http%3A%2F%2Fimg18.3lian.com%2Fd%2Ffile%2F201705%2F20%2F98410e73b3e4bf5b5474a86e51fab29a.jpg',stream = True).raw.read()
# with open('aaaa.jpg','wb') as file:
#     file.write(result)



# 发送cookie
# headers = {
#     'cookie':'id:007'
# }
# result = requests.get('http://httpbin.org/cookies',headers = headers)
# print(result.text)


