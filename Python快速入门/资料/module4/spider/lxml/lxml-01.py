#-*- conding:utf-8 -*-
from lxml import etree
import requests

# 创建lxml对象
html = etree.HTML(open('web.html',encoding='utf-8').read())  # 标签自动补全，容错率高,推荐使用该方式解析
# html = etree.parse(open('web.html',encoding='utf-8'))
# html = etree.fromstring(open('web.html',encoding='utf-8').read())
# print(html)


# # 将lxml 对象 字符串序列化
# result = etree.tostring(html,pretty_print=True,encoding='utf-8').decode('utf-8')
# print(result)


'''
    选取节点
'''
# print(html.xpath('//div'))
# print(len(html.xpath('//div')))

# print(html.xpath('/html/body/div')) # 从根节点开始查找，不方便，不推荐
# print(len(html.xpath('/html/body/div')))

# print(html.xpath('//div/a'))          # 从全文中开始查找，推荐使用
# print(len(html.xpath('//div/a')))


# print(html.xpath('//div/a/..')) # 两个点是查找该节点的父节点 （几个div下面有a标签，返回的是div）
# print(html.xpath('//div/a/.'))  # 一个点返回该节点自己



# print(html.xpath("//div[@class='left']/a"))     # //*[@class='xxx']  查找属性
#
# print(html.xpath("//div[@class='right']/a")[0]) # 通过下标获取某个元素
# print(html.xpath("//div[@class='right']/a[1]")) # 返回一个列表，通过下标获取某个元素（从1开始计）
# print(html.xpath("//div[@class='right']/a[last()]")) # 获取最后一个元素


# print(html.xpath("//div[@class='right']/a[position()<3]]")) # 获取前两个元素


# print(html.xpath("//div[@id='menu']/a[span='haha']")) # 获取a标签里面span的文本等于haha
# print(html.xpath("//*[@id='menu']/a[span='haha']"))   # * 表示任意标签

# print(html.xpath("//*[@id='menu']/a[span='haha'] | //div[@class='left']/a[1]"))   # | 表示几个标签取或运算的结果集
# print(html.xpath("//*[@id='menu']/a[span=11] + //*[@id='menu']/a[span=50]"))      # + 表示几个span的值取和运算


'''
                bs4       lxml
    没有子节点  string    text()
    有子节点    text      string()
'''
# # 获取文本
# print(html.xpath("//div[@class='left']/a[1]/text()"))  # 里面没有子节点使用text()方法获取
# print(html.xpath("string(//div[@class='left'])"))      # 有子节点的情况下使用string()方法获取


# 获取属性
print(html.xpath("//div[@class='left']/a[1]/@href"))
