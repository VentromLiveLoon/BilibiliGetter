# url='https://www.bilibili.com/video/BV15K4y1Q7vL/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=d6a2c7236ac768f11e6fe146a6f1a009'

# url=input("请输入视频的url：：");
url = 'https://www.bilibili.com/video/BV1nG4y1p7XU/?spm_id_from=333.788&vd_source=d6a2c7236ac768f11e6fe146a6f1a009';
url2='https://www.bilibili.com/video/BV1nG4y1p7XU/?spm_id_from=333.788&vd_source=d6a2c7236ac768f11e6fe146a6f1a009'




from selenium import webdriver;
from time import sleep;
import re;
browser = webdriver.Chrome();


browser.get(url='https://www.bilibili.com');
sleep(10);

print(browser.page_source);