#-*- conding:utf-8 -*-
import requests
import random
import json
import time

startUrl = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd={0}&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin={1}&ein={2}'

rnd = random.random()
sin = 0
ein = 29
'''
   一、请求歌单首页，获取所有的歌单信息  dissid 
'''
while True:
    headers = {
            # 浏览器的信息   身份信息
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

    headers['referer'] = 'https://y.qq.com/portal/playlist.html'

    dissList = requests.get(startUrl.format(rnd,sin,ein),headers = headers).text
    dissList = json.loads(dissList.strip('getPlaylist()'))
    # print(dissList)


    for i in dissList['data']['list']:
        dissid = i['dissid']
        dissName = i['dissname']


        '''
            二、通过disstid 获取  songmid  strMediaMid
        '''
        dissurl= 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid={0}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'

        headers['referer'] = 'https://y.qq.com/n/yqq/playsquare/{0}.html'.format(dissid)

        song = requests.get(dissurl.format(dissid),headers = headers).text
        song = json.loads(song.strip('playlistinfoCallback()'))

        num = 1
        for s in song['cdlist'][0]['songlist']:
            # 获取songMid
            songMid = s['songmid']
            # 获取歌曲名
            songName = s['songname']
            # 获取filename
            filename = 'C400'+str(s['strMediaMid'])+'.m4a'


            '''
                三、获取vkey
            '''
            vkeyUrl = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback&uin=0&songmid={0}&filename={1}&guid=1093240106'


            # 发送请求
            headers['referer'] = 'https://y.qq.com/portal/player.html'
            responses = requests.get(vkeyUrl.format(songMid,filename),headers = headers).text
            responses = json.loads(responses.strip('MusicJsonCallback()'))


            # 提取vkey
            for vk in responses['data']['items']:
                vkey = vk['vkey']
                filenames =  vk['filename']

                '''
                    四、通过vkey下载音乐
                '''

                musicUrl = 'http://dl.stream.qqmusic.qq.com/{0}?vkey={1}&guid=1093240106&uin=0&fromtag=66'
                # print(musicUrl.format(filenames,vkey))
                del headers['referer']

                music = requests.get(musicUrl.format(filenames,vkey),headers = headers,stream = True).raw.read()

                with open('music/'+songName+'.mp3','wb') as file:
                    file.write(music)

                # time.sleep(1)

                print('{0}歌单的第{1}首歌-歌曲名称：{2}'.format(dissName,num,songName))
                num+=1

    if sin < dissList['data']['sum']:
        sin+=30
        ein+=30
        rnd = random.random()
        time.sleep(1)
    else:
        break































