#-*- conding:utf-8 -*-
import time

# print(time.altzone)

# print(time.asctime())   # 可以传递时间元组

# print(time.clock())
#
# for i in range(100000000):
#     pass
#
# print(time.clock())


# print(time.ctime())  # 返回可读形式的时间

# 时间戳  1970 1 1 0 0 0

# print(time.gmtime())   # 返回一个时间元组

# 接受时间戳返回当地时间的时间元组
# print(time.localtime())

# 获取时间元组   可以将时间戳转换为时间元组
# tup_time = time.localtime()
# print(tup_time)

# 可以将时间元组转换为时间戳
# print(time.mktime(tup_time))  # 传递时间元组 返回时间戳


# 接受时间元组，将时间元组转换为自定义的可以读形式的时间字符串
# tup_time = time.localtime()
# print(tup_time)
# print(time.strftime('%Y-%m-%d %H:%M:%S',tup_time))


# 将字符串时间转换为时间元组
# time_str = '2018-06-30 09:59:26'
# print(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
# tup_time = time.strptime(time_str,'%Y-%m-%d %H:%M:%S')
# print(time.mktime(tup_time))


# 获取时间戳
# print(time.time())

#
# for i in range(1,5):
#     print('第%d课子弹'%i)
#     time.sleep(3)



'''
    课堂练习
    1.将字符串的时间"2017-10-10 23:40:00"转换为时间戳和时间元组

    2.字符串格式更改。如提time = "2017-10-10 23:40:00",想改为 time= "2017/10/10 23:40:00"
    
    3.获取当前时间戳转换为指定格式日期
    
    4.获得三天前的时间
 

'''

# 1
# time_str = "2017-10-10 23:40:00"
# print(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
# print(time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S')))

# 2
# time_str = "2017-10-10 23:40:00"
# print(time.strptime(time_str,'%Y-%m-%d %H:%M:%S'))
# tup_time = time.strptime(time_str,'%Y-%m-%d %H:%M:%S')
# print(time.strftime('%Y/%m/%d %H/%M/%S',tup_time))

# 3
# timestmpe = time.time()
# print(timestmpe)
# # 转换时间戳为时间元组
# tup_time = time.localtime(timestmpe)
# # 将时间元组转换为可读形式时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',tup_time))

# timestmpe = time.time()
# threedayago = timestmpe - 60*60*24*3
# tup_time = time.localtime(threedayago)
# 将时间元组转换为可读形式时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',tup_time))

import numpy as np
