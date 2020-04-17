import requests
import random
import re


def get_html(url):
    req = requests.Session()
    response = req.get(url)
    response.encoding = 'utf-8'
    return response


def register(url, data):
    req = requests.Session()
    response = req.post(url, data=data)
    response.encoding = 'utf-8'
    print(response.json()['msg'])
    if (response.json()['ret'] == 0):
        exit()


def login(url, data):
    req = requests.Session()
    response = req.post(url, data=data)
    response.encoding = 'utf-8'
    print(response.json()['msg'])
    if (response.json()['ret'] == 0):
        exit()
    return req


def sign(url, req):
    response = req.post(url)
    response.encoding = 'utf-8'
    print(response.json()['msg'])


def get_sub(response):
    ssr_list = list(set(re.findall('"(https://.*?link.*?\?.*?=[\d|\w]&??.*?)[?!>]?"', response.text)))
    for ssr in ssr_list:
        print(ssr)


def get_url(url, type, req):
    response = req.get(url + type)
    response.encoding = 'utf-8'
    if type == 'v2ray':
        type = 'vmess'
    if type + '://' in response.text:
        print(response.text)


def get_usr(url, req):
    response = req.get(url)
    response.encoding = 'utf-8'
    print('剩余：' + re.findall('((\d+?|\d+.\d+)(MB|GB|TB))', response.text)[0][0])
    get_sub(response)
    return response


def main():
    # url = 'https://ufocloud.xyz'
    # url = 'https://jxka.net'
    # code = 'lanmang'
    # url = 'https://d9cloud.pw'
    url = input('请输入机场网址：').strip()
    code = input('请输入邀请码(没有留空)：').strip()
    reg_url = url + '/auth/register'
    log_url = url + '/auth/login'
    usr_url = url + '/user'
    sign_url = url + '/user/checkin'
    get_link_url = url + '/user/getUserAllURL?type='
    name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 10))
    wechat = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 10))
    email = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 10)) + '@qq.com'
    data = {
        'email': email,
        'name': name,
        'passwd': '11111111',
        'repasswd': '11111111',
        'wechat': wechat,
        'imtype': '1',
        'code': code
    }
    register(reg_url, data)
    data = {
        'email': email,
        'passwd': '11111111'
    }
    req = login(log_url, data)
    try:
        sign(sign_url, req)
    except:
        pass
    response = get_usr(usr_url, req)
    if 'ssr://' in response.text:
        print('\n'.join(re.findall('ssr://[\d|\w]+', response.text)))
    else:
        get_url(get_link_url, 'ssr', req)
    if 'vmess://' in response.text:
        print('\n'.join(re.findall('vmess://[\d|\w]+?==')))
    else:
        get_url(get_link_url, 'v2ray', req)


if __name__ == '__main__':
    main()
    input()
