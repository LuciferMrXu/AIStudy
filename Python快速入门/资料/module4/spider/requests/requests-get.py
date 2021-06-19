#-*- conding:utf-8 -*-
import requests

# # GET请求   参数会显示在URL地址当中
# par = {'name':'joe','pwd':'123'}    #传递参数，可用于搜索验证（登陆验证不用get，不安全，用post请求）
# result = requests.get('http://httpbin.org/get',params= par) #测试get请求的网站
# print(result.text)
# print(result.status_code)

{
   "args": {},        #参数
  "headers": {        #请求头信息
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "Host": "httpbin.org",         #发送的服务器
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"    #发送者（这里是我的chrome浏览器）
  },
  "origin": "222.195.5.230",       #当前IP地址
  "url": "http://httpbin.org/get"  #传递参数后显示在url地址中，问号后面就是参数
}



# # GET请求添加头文件伪装浏览器
# headers = {
#     # 'cookie':''     验证网站cookie
#     # 'referer':''    表示这个请求从哪里来的
#     # 'host':''       验证服务器主机地址,这三个验证直接从浏览器里的Network中的Headers里找到对应项,粘贴
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# result = requests.get('http://httpbin.org/get',headers = headers)  # 测试get请求的网站
# print(result.text)
# print(result.status_code)


# # 请求微博网站
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# result = requests.get('https://weibo.com',headers = headers)
# print(result.text)

# # 发送cookie
# headers = {
#     'cookie':'id:007'
# }
# result = requests.get('http://httpbin.org/cookies',headers = headers)
# print(result.text)


# # 获取网页cookie
# result = requests.get('http://www.ibeifeng.com')
# print(result.cookies)
# print(result.cookies['ECS[visit_times]'])



# # 设置cookies
# # 1.开启session
# s=requests.session()
# # 2.检查有没有cookie
# r=s.get('https://weibo.com/cookie')
# print(r.text)
# # 3.从服务器的setcookIE里要一个cookie
# r=s.get('https://weibo.com/setcookie')
# print(r.text)
# print(r.cookies)
# # 4.检查有没有cookie
# r=s.get('https://weibo.com/cookie')
# print(r.text)




# # 解析json数据(还可以引入json模块进行操作)
# result = requests.get('https://github.com/timeline.json')
# print(result.text)     # 字符串
# print(type(result.text))
# print(result.json())   # 将json字符串解析成dict



#GET请求，获取原始响应内容
'''
原始响应内容
在罕见的情况下,你可能想获取来自服务器的原始套接字响应
那么你可以访问 r.raw 
如果你确实想这么干,请确保在初始请求中设置了 stream=True
'''
# r = requests.get('https://github.com/timeline.json',stream=True)
# print(r.raw.read(100))


# # 下载音乐
# result = requests.get('http://183.213.28.133/65729DD465E3882F3081313F03/03000A03005B8E042D2E66F06257BBDAFE5255-9C42-44F2-A16D-9830ABDEACDD.mp4?ccode=0502&duration=390&expire=18000&psid=d120f88f3e76db700b448a3945223752&ups_client_netip=701beea5&ups_ts=1541595799&ups_userid=1323239232&utid=51MnFETOfgsCAd7DBeYHRXRL&vid=XOTA5MjQ0NTc2&vkey=A8657dd4c2f78d508d3c1423f6f252142&s=7e99324aa12a11e4b432&sp=',stream = True).raw.read()
# with open('a.mp4','wb') as file:
#     file.write(result)


# # 下载图片
# result = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1541500956076&di=792ead154f83d935f580cfdc1695b749&imgtype=0&src=http%3A%2F%2Fww2.sinaimg.cn%2Flarge%2F6d5225b9jw1er9kro53j8j21hc0u00wm.jpg',stream = True).raw.read()
# with open('壁纸.jpg','wb') as file:
#     file.write(result)






