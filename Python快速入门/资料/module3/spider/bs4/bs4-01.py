#-*- conding:utf-8 -*-
from bs4 import BeautifulSoup
import requests


# response = requests.get('http://www.aidu.com').content.decode('utf-8')
# print(response)

# 使用 beautifulsoup 解析 请求到的html文档
# soup = BeautifulSoup(response,'html.parser')  # lxml   解析速度快 容错率高
# print(type(soup))
# print(soup.prettify())  # 格式美化
# print(soup)



# 解析 web.html

result = BeautifulSoup(open('web.html',encoding='utf-8'),'html.parser')
# 四大对象之 Tag
# print(type(result.html.body.div.span))   # 默认会找第一个名字叫这个的Tag

# 四大对象之 NavigableString    标签中的文本
# print(result.html.body.div.span.a.string)  # 使用string必须保证里面没有字标签
# print(result.html.body.div.span.a.string)
# print(result.html.body.div.span.strings)   # 有子标签的情况下使用 可以获取到所有的文本内容
# strs = result.html.body.div.span.strings
# for i in strs:
#     print(i)


'''
    遍历文档树
'''
#获取直接子节点
# print(result.html.body.div.contents)  # 可以获取到该节点下的所有子节点 包括换行符
# print(result.html.body.div.children)
# for i in result.html.body.div.children:
#     print(i)

# 递归获取子孙节点
# print(result.html.body.div.descendants)
# for i in result.html.body.div.descendants:
#     print(i)


# 获取标签内容
# print(result.html.body.div.span.a.string)  # 没有子节点的情况下
# print(result.html.body.div.span.text)  # 获取该标签下的所有文本

# 获取父节点
# print(result.html.body.div.span.a)
# print(result.html.body.div.span.a.parent.parent)
# print(result.html.body.div.span.a.parents)
# for i in result.html.body.div.span.a.parents:
#     print(i)


#获取兄弟节点   可以自主选择你需要的标签节点
# print(result.html.body.div.next_sibling.next_sibling.next_sibling.next_sibling)
# print(result.html.body.div.next_sibling.next_sibling.next_sibling.next_sibling.contents[1].string)
# print(result.html.body.div.next_sibling.next_sibling.next_sibling.next_sibling.text)

# 1. 发送请求获取源码 2. 解析源码  3.提取相关标签以及文本内容



# find_all获取所有的子节点
# print(result.find_all('a'))  # 传递字符串  表示标签名
# print(result.find_all(name = 'a'))  # 传递字符串  表示标签名
# print(result.html.body.div.find_all('span'))  # 获取第一个div里面所有的span标签


# print(result.find_all(['a','span']))  # 获取多个标签的方式
# print(result.find_all(id = 'foot'))
# print(result.find_all(class_ = 'one',attrs = {'name':'aa'}))  # name 表示标签名

# 标签选择器  id选择器  class选择器   就是相当于给标签取名字
# id的名称是不能重复的  class可以重复
# print(result.find_all(text = 'haha'))

# find 查找单个节点
# print(result.find(class_ = 'right').find_all('a')[2:])  # 进行定位
# for i in result.find(class_ = 'right').find_all('a')[2:]:
#     print(i.string)

#
# print(result.find(class_ = 'right').find_all('a'))  # 进行定位
# for i in result.find(class_ = 'right').find_all('a')[2:]:  # 提取属性
#     print(i['href'])   # 第一种
#     print(i.string)
#     print(i.attrs['href'])  # 第二种

# print(result.find(id = 'content').div.next_sibling.next_sibling.find_all('a'))

# print(result.find(class_ = 'right').find_all('a',limit = 2))

'''
    CSS选择器
'''
# 1.通过标签名查找
# print(result.select('a'))
# print(result.find_all('a'))

# 2.通过类名查找
# print(result.select('.left'))   # 都是保存在列表当中
# print(result.find(class_ = 'left'))

# 3.通过 id 名查找
# print(result.select('#menu'))
# print(result.find(id = 'menu'))

# #content   id = 'content'
# .left     class = 'left'


# 4.通过属性进行查找
# print(result.select('a[name="aa"]'))
# print(result.find(name = 'a',attrs={'name':'aa'}))

# 5.组合查找
# print(result.select('#content .left a')[0])
# print(result.find(id='content').find(class_='left').find_all('a')[0])

# 6.获取文本
# print(result.select('a[name="aa"]')[0].get_text())  #第一种
# print(result.select('a[name="aa"]')[0].text)  # 第二种

# 7.获取属性
# print(result.select('a[name="aa"]')[0]['href'])  #第一种
# print(result.select('a[name="aa"]')[0].attrs['href'])  #第二种


# print(result.select('#content .left a')[3].text)
# print(result.select('#content .right a')[1].text)


