# 视频下载部分
import requests;
import os;
#进度条部分
from tqdm import tqdm
# 请求头
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
}

def downloader(video_url,audio_url,name):

    print("\n\n********************************************\n\n");
    # 开始请求和视频
    video_resp=requests.get(headers=header,url=video_url,stream=True);
    #得到视频的长度
    total = int(video_resp.headers.get('Content-Length'));
    # 保存请求的内容
    with open(f"/home/windstorm/Videos/background/{name}.mp4",'wb') as file,tqdm(
        desc=name,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in video_resp.iter_content(chunk_size=1024):
            size = file.write(data);
            bar.update(size);

    # 关闭请求
    video_resp.close();


    # 开始请求和声音
    audio_resp=requests.get(headers=header,url=audio_url,stream=True);
    #得到视频的长度
    total=int(audio_resp.headers.get('Content-Length'));
    with open(f"/home/windstorm/Music/{name}.mp4",'wb') as file,tqdm(
        desc=name,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in audio_resp.iter_content(chunk_size=1024):
            size = file.write(data);
            bar.update(size);
    # 关闭请求
    audio_resp.close();


    #开始合并视频和声音
    os.system(f"ffmpeg -i /home/windstorm/Music/{name}.mp4 -i /home/windstorm/Videos/background/{name}.mp4 -c copy /home/windstorm/Videos/bilibili/{name}.mp4");

    print("\n\n********************************************\n\n");
    print("Done"); 
