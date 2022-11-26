
#!/bin/python

# https://xy36x248x55x2xy.mcdn.bilivideo.cn:4483/upgcxcode/60/12/862141260/862141260-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1668447340&gen=playurlv2&os=mcdn&oi=1849029074&trid=000065ad2158a4494968989f78716f3f39e4u&mid=1028449803&platform=pc&upsig=10200c9280c92f20a93f60188bef3113&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=11000057&bvc=vod&nettype=0&orderid=0,3&buvid=&build=0&agrr=1&bw=234535&logo=A0000400


import requests;
import os;
# 请求头
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
}

# 请求链接

audio_url=input("请输入audio_m4s码：：");


audio_resp=requests.get(headers=header,url=audio_url);


audio_resp.close();


# 保存请求的内容
with open('video_data.mp4','wb') as file:
    file.write(audio_resp.content);




