# coding: utf-8
import os
import sys
import time
import csv
from pprint import pprint
sys.path.append(os.getcwd())
from wechatarticles.ReadOutfile import Reader
from wechatarticles import ArticlesAPI

if __name__ == '__main__':
    username = "username"
    password = "password"
    official_cookie = ''
    token = ""
    appmsg_token = "appmsg_token"
    wechat_cookie = "wechat_cookie"

    nickname = "DingXiangYiSheng"

    # 手动输入所有参数
    # test = ArticlesAPI(
        # official_cookie=official_cookie,
        # token=token,
        # appmsg_token=appmsg_token,
        # wechat_cookie=wechat_cookie)

    # 输入账号密码，自动登录公众号，手动输入appmsg_token和wechat_cookie
    # test = ArticlesAPI(
        # username=username,
        # password=password,
        # appmsg_token=appmsg_token,
        # wechat_cookie=wechat_cookie)

    # 手动输入official_cookie和token, 自动获取appmsg_token和wechat_cookie
    # print(data.__len__())
    # pprint(data)

    f = open("file1.csv", 'a+')
    w = csv.writer(f, delimiter=',')
    # field_name = ['aid', 'appmsgid', 'cover', 'digest', 'itemidx', 'like_num', 'link', 'read_num', 'title', 'update_time']
    # w.writerow(field_name)
    i = 0
    while(i < 505):
        test = ArticlesAPI(
            official_cookie=official_cookie, token=token, outfile="outfile")

        data = test.get_data(nickname=nickname, begin=str(i))
        if i == 0:
            w.writerow(data[0].keys())
        for d in data:
            w.writerow(d.values())
        i += 5
        print("完成文章数......%d" % (i))
        time.sleep(30)

    f.close()
    
