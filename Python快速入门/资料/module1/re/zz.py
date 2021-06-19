#-*- conding:utf-8 -*-
import re

'''
    正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、
    及这些特定字符的组合，组成一个“规则字符串”，
    这个“规则字符串”用来表达对字符串的一种过滤逻辑
'''
# 正则表达式进行格式验证
# 字母开头、字母数字下划线  6 18
# 用户名：  a11334fdf
# 密码:6-18    规则字符串

# 正则表达式如何制定规则


'''
    compile
'''
# pattern = re.compile('\w?')
# print(type(pattern))


'''
    match  只匹配开头
'''
# pattern = re.compile('\d')  # 1个数字
# strs = '1abc'
# print(re.match(pattern,strs).group())  # 查看匹配结果需要使用 group
# 如果符合天剑使用group 查看匹配结果


# pattern = re.compile('(\d)[a-z]+(\d)')  # 1个数字
# strs = '1abc2fsfs'
# print(re.match(pattern,strs).group(0))  # 返回完整的正则表达式的匹配结果
# print(re.match(pattern,strs).group(1))  # 返回第一个分组的匹配结果
# print(re.match(pattern,strs).group(2))  # 返回第二个分组的匹配结果


'''
   serach 
'''
# pattern = re.compile('(\d)[a-z]+(\d)')  # 1个数字
# strs = 'MMMM1abc2NNNN3abc4KKKKK'
# 使用match    Match 只匹配开头部分
# print(re.match(pattern,strs))  # 返回完整的正则表达式的匹配结果

# 使用serach    只匹配一次成功则停止匹配
# print(re.search(pattern,strs).group(0))  # 返回完整的正则表达式的匹配结果
# print(re.search(pattern,strs).group(1))  # 返回第一个分组的匹配结果
# print(re.search(pattern,strs).group(2))


'''
    findall 遍历匹配
'''
# pattern = re.compile('\d[a-z]+\d')  # 1个数字
# strs = 'MMMM1abc2NNNN3abc4KKKKK'
# # findall
# print(re.findall(pattern,strs))  # 返回符合条件的所有内容 保存在列表中

# pattern = re.compile('(\d)[a-z]+(\d)')  # 1个数字
# strs = 'MMMM1abc2NNNN3abc4KKKKK'
# # findall
# print(re.findall(pattern,strs)) # findall 如果规则中有分组则只返回分组匹配的结果


'''
    finditer
'''
pattern = re.compile('(\d)[a-z]+(\d)')  # 1个数字
strs = 'MMMM1abc2NNNN3abc4KKKKK'
# findall
for i in re.finditer(pattern,strs):
    print(i.group(0)) #查看完整匹配结果
    print(i.group(1))
    print(i.group(2))
