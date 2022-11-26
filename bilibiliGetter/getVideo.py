#!/bin/python

import requests;
import os;
# 请求头
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
}

# 请求链接
video_url=input("请输入vidio_m4s码：：");


# 开始请求声音和视频
video_resp=requests.get(headers=header,url=video_url);


# 关闭请求
video_resp.close();



# 保存请求的内容
with open('video_data.mp4','wb') as file:
    file.write(video_resp.content);



