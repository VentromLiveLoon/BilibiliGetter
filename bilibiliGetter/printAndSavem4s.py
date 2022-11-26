
def printAndSavem4s(video_url,audio_url):
    # 输出vedio.m4s和audio.m4s的视频和音频链接,并且保存在文件中
    print(video_url);
    with open('vidio_m4s','a') as file:
        file.write(video_url);
        file.write("\n");
    print();
    print(audio_url);
    with open('audio_m4s','a') as file:
        file.write(audio_url);
        file.write("\n");