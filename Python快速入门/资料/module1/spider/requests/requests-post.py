#-*- conding:utf-8 -*-
import requests

#post 提交参数
# data = {'user':'joe','pwd':'007'}
# result = requests.post('http://httpbin.org/post',data = data)
# print(result.text)




# session
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

#
# import json
# s = requests.session()
# r = s.post('http://123.207.11.209:8080/index.php/Home/Index/checkLogin', data = {'admin_name':'root_python','admin_password':'pythonroot'} ,headers={'x-test2': 'true'})
# print(json.loads(r.content))
#
# r = s.post('http://123.207.11.209:8080/index.php/Home/System/aboutme', headers={'x-test2': 'true'})
# print(r.text)



# 代理
proxies = {
    "http": "http://101.236.23.202:8866",
    # 'https':"https://"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
response = requests.get("http://httpbin.org/get",proxies = proxies)
print(response.text)  #116.231.254.2
                      #101.236.23.202