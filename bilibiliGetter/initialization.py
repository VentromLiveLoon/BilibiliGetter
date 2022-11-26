from os.path import exists
from os import system

def initialization():
    
    # 如果cookies不存在
    if not exists('./.cookies'):
        from writeCookies import writeCookies
        writeCookies();
    #如果videos不存在
    if not exists("./videos"):
        system("mkdir -p ./videos");
    
# initialization();
