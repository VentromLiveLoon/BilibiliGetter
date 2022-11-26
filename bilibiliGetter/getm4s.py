import re

def getm4s(page_source):
    #正则表达式初始化
    find_url=re.compile(r'<script>(?P<video_url>.*?)</script>',re.S);
    video_url=re.compile(r'"video":(?P<videos_quality>.*?),"baseUrl":"(?P<video_url>.*?)",',re.S);
    #获取script中的源码
    script=find_url.search(page_source);
    script_content=script.group('video_url');
    #获取视频的链接，从script_content中获取视频的m4s和视频的质量。
    videos_quality = video_url.search(script_content).group('videos_quality');
    print();
    print(f"The videos quality is {videos_quality}");
    print();
    video_url=video_url.search(script_content).group('video_url');


    #正则表达式初始化
    audio_url=re.compile(r'"audio":.*?{"id":.*?,"baseUrl":"(?P<audio_url>.*?)"',re.S);
    #获取音频的m4s链接，从script_content获取
    audio_url=audio_url.search(script_content).group('audio_url');

    return video_url,audio_url;