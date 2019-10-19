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
if __name__=='__main__':
    n=int(input("请输入抓取数目："))
    a = input("是否抓取订阅地址（y or n）：")
    b = input("是否抓取ssr链接（y or n）：")
    c = input("是否输出txt（y or n）：")
    while n!=0:
        base_url='https://www.lulula.cn'
        url = base_url+'/auth/register'
        email=RandomEmail(emailType='@qq.com',rang=20)
        name=ranstr(6)
        passwd='aa123456'
        # print("名称："+name)
        # print("账号："+email)
        # print("密码："+passwd)
        data={"email":email,"name":name,"passwd":passwd,"repasswd":passwd}
        req=requests.Session()
        response=req.post(url,data=data)
        if response.json()["ret"]==1:
            #print("注册成功")
            pass
        else:
            #print("注册失败")
            exit()
        url=base_url+'/auth/login'
        data={"email":email,"passwd":passwd}
        response=req.post(url,data=data)
        if response.json()["ret"]==1:
            #print("登录成功")
            pass
        else:
            #print("登录失败")
            exit()
        url=base_url+"/user"
        response=req.get(url)
        soup=BeautifulSoup(response.text,features="html.parser")
        if a=='y':
            print("订阅地址：" + soup.find("input")["value"])
        if b == 'y':
            for i in soup.select("a.btn-dl"):
                print(re.findall("</i>(.*?)</a>",str(i))[0]+":\n"+i["href"])
        if c == 'y':
            with open("ssr.txt","a") as f:
                if a == 'y':
                    f.write("订阅地址：" + soup.find("input")["value"]+"\n")
                if b == 'y':
                    for i in soup.select("a.btn-dl"):
                        f.write(re.findall("</i>(.*?)</a>",str(i))[0]+":\n"+i["href"])
        n=n-1
