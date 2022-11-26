#!/bin/python

# url='https://www.bilibili.com/video/BV15K4y1Q7vL/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=d6a2c7236ac768f11e6fe146a6f1a009'



def main():

    #初始化环境
    from initialization import initialization
    initialization();

    #输入和初始化部分
    url=input("\n\n请输入视频的url：：");

    #浏览器渲染获取源代码
    from seleniumGetter import seleniumGetter
    page_source,name=seleniumGetter(url=url);

    #格式化name
    from nameFormator import nameFormator
    name = nameFormator(name=name);

    #获取video.m4s和audio.m4s的视频链接
    from getm4s import getm4s
    video_url,audio_url = getm4s(page_source=page_source);

    # 输出vedio.m4s和audio.m4s的视频和音频链接,并且保存在文件中
    from printAndSavem4s import printAndSavem4s
    printAndSavem4s(video_url, audio_url);

    #下载视频并且保存在文件中
    from downloader import downloader
    downloader(video_url, audio_url, name);



if __name__=='__main__':
    main();

