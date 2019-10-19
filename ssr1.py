import re
import requests
from bs4 import BeautifulSoup
import random
def RandomEmail( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email
def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt
if __name__ == '__main__':
    n = int(input("请输入抓取数目："))
    a = input("是否抓取订阅地址（y or n）：")
    b = input("是否抓取ssr链接（y or n）：")
    c = input("是否输出txt（y or n）：")
    while n!=0:
        base_url = 'https://starryjisu.com'
        url = base_url + '/auth/register'
        email = RandomEmail(emailType='@qq.com', rang=20)
        name = ranstr(6)
        wechat = ranstr(6)
        passwd = 'aa123456'
        data = {"email": email, "name": name, "passwd": passwd, "repasswd": passwd, "wechat": wechat, "imtype": 1}
        req = requests.Session()
        response = req.post(url, data=data)
        url = base_url + '/auth/login'
        data = {"email": email, "passwd": passwd}
        response = req.post(url, data=data)
        url = base_url + "/user"
        response = req.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        if a == 'y':
            print("订阅地址：" + soup.find("input")["value"])
        ssr1=re.findall("</i>(.*?)</a>", str(soup.select("a.btn-dl")[1]))[0] + ":\n" + soup.select("a.btn-dl")[1]["data-clipboard-text"]
        ssr2=re.findall("</i>(.*?)</a>", str(soup.select("a.btn-dl")[2]))[0] + ":\n" + soup.select("a.btn-dl")[2]["data-clipboard-text"]
        if b == 'y':
            print(ssr1)
            print(ssr2)
        if c == 'y':
            with open("1.txt", "a") as f:
                if a == 'y':
                    f.write("订阅地址：" + soup.find("input")["value"]+"\n")
                if b == 'y':
                    f.write(ssr1+"\n")
                    f.write(ssr2+"\n")
        n=n-1
