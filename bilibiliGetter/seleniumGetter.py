from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.options import Options;
from readCookies import readCookies;
from time import sleep


# 设置浏览器为无头模式
ch_options=Options();
ch_options.add_argument('--headless');
browser = webdriver.Chrome(options=ch_options);

#设置浏览器为有头模式
# browser = webdriver.Chrome();

def seleniumGetter(url):
    # 登录刷新网页
    browser.get(url=url);
    name=browser.find_element(by=By.XPATH,value='//*[@id="viewbox_report"]/h1').text;
    print(f"The title is::{name}");
    name=name[:10];
    sleep(1);

    #设置bilibili的cookie
    browser.delete_all_cookies();
    cookies = readCookies();
    for cookie in cookies:
        browser.add_cookie(cookie_dict=cookie);
    browser.refresh();
    # input("yes?");
    sleep(1);
    page_source=browser.page_source;
    #关闭浏览器
    browser.close();

    #返回网页的源代码
    return page_source,name;
