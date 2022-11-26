#读取cookie
import pickle;
def readCookies():
    with open('./.cookies','rb') as f:

        print('(*****************)');
        a=pickle.load(f);
        print(a);
        return a;
