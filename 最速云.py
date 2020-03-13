import requests
import random
import re
def get_html(url):
    req = requests.Session()
    response = req.get(url)
    response.encoding = 'utf-8'
    return response
def register(url,data):
    req=requests.Session()
    response=req.post(url,data=data)
    response.encoding='utf-8'
    print(response.json()['msg'])
    if(response.json()['ret']==0):
        exit()
def login(url,data):
    req=requests.Session()
    response=req.post(url,data=data)
    response.encoding = 'utf-8'
    print(response.json()['msg'])
    if (response.json()['ret'] == 0):
        exit()
    return req
def sign(url,req):
    response=req.post(url)
    response.encoding = 'utf-8'
    print(response.json()['msg'])
    print('剩余：%.3fG'%(float(response.json()['msg'].split(' ')[1])/1000+10))
def get_ssr(url,req):
    response=req.get(url)
    response.encoding='utf-8'
    ssr=re.findall('<a class="dropdown-item copy-text" href="##" data-clipboard-text="(.*?)"> 复制 SSR 订阅链接</a>',response.text)[0]
    print(ssr)
def main():
    reg_url='https://zuisucloud.live/auth/register'
    log_url='https://zuisucloud.live/auth/login'
    usr_url='https://zuisucloud.live/user'
    sign_url='https://zuisucloud.live/user/checkin'
    name=''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890',10))
    email = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 10))+'@qq.com'
    wechat=''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890',10))
    data={
        'email':email,
        'name': name,
        'passwd': '11111111',
        'repasswd': '11111111',
        'wechat': wechat,
        'imtype': 1,
        'code': 0
    }
    register(reg_url,data)
    data={
        'email': email,
        'passwd': '11111111'
    }
    req=login(log_url,data)
    sign(sign_url,req)
    get_ssr(usr_url,req)
if __name__ == '__main__':
    main()
