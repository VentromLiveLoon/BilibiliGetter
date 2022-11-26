
#!/bin/python

# 变量写入文件的库类
import pickle;

def writeCookies():
    # 网页地址
    url = 'https://www.bilibili.com/';

    #打开网页
    from selenium import webdriver;
    broswer = webdriver.Chrome();
    broswer.get(url=url);

    #等待用户登录
    input("************************\nPlease login this page then Press any key to continue !\n*************************");

    #刷新页面得到cookies
    broswer.refresh();
    cookies = broswer.get_cookies();
    broswer.close();

    # 写入cookie
    with open('./.cookies','wb') as f:
        pickle.dump(cookies, f);

    #读取cookie
    print('You cookies is ::');
    with open('./.cookies','rb') as f:

        print('(*****************)');
        a=pickle.load(f);
        print(a);




