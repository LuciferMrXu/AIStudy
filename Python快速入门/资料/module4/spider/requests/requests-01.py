#-*- conding:utf-8 -*-
import requests

#请求新浪微博手机端
result = requests.get('https://m.weibo.cn/')
# print(type(result)) # 查看返回类型
# print(result.status_code)  # 查看返回的状态码  200  表示请求成功
# print(result.encoding) # 查看编码
# print(result.cookies) # 查看返回的cookie
# print(result.text) # 字符串方式的响应体，会自动根据响应头部的字符串进行解码
print(result.content.decode('utf-8')) # 字节方式的响应体，会自动为你解码gzip和deflate压缩



