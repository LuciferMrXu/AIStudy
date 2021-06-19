#-*- conding:utf-8 -*-
import requests
import json

# # post 提交参数
# data = {'user':'joe','pwd':'007'}   # 参数放在'from':''里面,让服务器进行验证
# result = requests.post('http://httpbin.org/post',data = data)
# print(result.text)                  # url地址中不带参数,保证安全性


# # post发送文件
# url='http://httpbin.org/post'
# files={'file': open('壁纸.jpg','rb')}
# r=requests.post(url,files=files)
# print(r.text)

# # post请求,发送json数据
# url='http://httpbin.org/post'
# payload={'some':'data'}
# r=requests.post(url,data=json.dumps(payload))
# print(r.text)

# # post请求,发送cookie
# url='http://httpbin.org/post'
# cookies=dict(cookies_are='working')
# r=requests.post(url,cookies=cookies)   # 设置cookie
# print(r.cookies)
# print(r.text)


# # session会话
# res = requests.get('http://www.mywebs.com/setcookie')
# print(res.text)

#刚刚设置好了cookie 现在看看它设置的是什么
# res = requests.get('http://www.mywebs.com/cookie')
# print(res.text)


# 这是两个独立的请求
# s = requests.session()
# res = s.get('http://www.mywebs.com/setcookie')
# print(res.text)
#
# res = s.get('http://www.mywebs.com/cookie')
# print(res.text)



# # json模拟登陆
# s = requests.session()
# r = s.post('http://123.207.11.209:8080/index.php/Home/Index/checkLogin', data = {'admin_name':'root_python','admin_password':'pythonroot'} ,headers={'x-test2': 'true'})
# print(json.loads(r.content))
#
# r = s.post('http://123.207.11.209:8080/index.php/Home/System/aboutme', headers={'x-test2': 'true'})
# print(r.text)




# 代理请求
proxies = {
    "http": "http://61.135.217.7:80",
    # 'https':"https://"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
response = requests.get("http://httpbin.org/get",proxies = proxies)
print(response.text)  #116.231.254.2
                      #61.135.217.7



# # SSL验证
# result=requests.get('https://www.12306.cn',verify=False) # 关闭SSL进行验证
# print(result.status_code)
# print(result.content.decode('utf-8'))