'''
从分类歌单开始下载每一个歌单的内容

一、音乐下载地址
http://dl.stream.qqmusic.qq.com/
C400002cey4V27XJ2h.m4a?
vkey=082B18541A5FCD27D4CA9C68F78DDC22E8089F3B6C72B2448B34581B897E5FFA0A4559286ED1590DF76B811FE1ADA11FE6C8370BB335E26C
&guid=1093240106&uin=0&fromtag=66


filename：C400002cey4V27XJ2h.m4a？
vkey：
决定了音乐资源的不同  

二、
https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback1305856641857932&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback1305856641857932&uin=0&songmid=001HaDeD4aFlS2&filename=C400002cey4V27XJ2h.m4a&guid=1093240106
该请求可以返回   
filename  
vkey 

但是该请求雨这么多参数！！！！ 如何设置？  通过比对法可以确定剩下两个参数是不同的
songmid: 001HaDeD4aFlS2        
filename: C400002cey4V27XJ2h.m4a    
这两个参数如何获取

songmid：001HaDeD4aFlS2   
strMediaMid：002cey4V27XJ2h

三、 下面这个请求可以获得 songmid  strMediaMid
该请求是获取整个歌单的信息
https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=4100249474&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0
    
需要：disstid: 4100249474



四、
https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.8018595900941323&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin=0&ein=29
返回dissid
rnd:
sin: 0
ein: 29

'''

