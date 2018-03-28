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
    official_cookie = "pgv_pvi=1487669248; pt2gguin=o1050048500; RK=HNKpqqlUfZ; ptcz=03619fd2cc87c821a05dd74db64c811b966c7bcf016c6be390035d7d0df5eda5; ptui_loginuin=1050048500; pgv_pvid=2310676148; tvfe_boss_uuid=e2b03ce7b83825f9; o_cookie=1050048500; mobileUV=1_161e20fc4e3_33a5f; ua_id=obXJMwa09a4Dr4T2AAAAAFgyhtDKX159iISsLMBtsjI=; mm_lang=zh_CN; noticeLoginFlag=1; ts_uid=5632414182; remember_acct=cqwzchenchao%40gmail.com; pgv_si=s6457426944; uuid=59ee3f77e5948760611a96da4c04b6bb; ticket=8c34900138d79c9e3a1814004db75ba449a8829b; ticket_id=gh_d75f63bde891; cert=08t5C19vkf7tN1CCT5T0dHzNrKIgu1Kv; data_bizuin=3546731367; bizuin=3585491970; data_ticket=vJQ2wP7Za934oN3vDoYdCOAWOjKGUdgfYMO0urws2hZDEYMNoauQOh5f9R4dMA3f; slave_sid=cWZ3am1fYmN5ZFd1ZmFzaXVpa2tkYnFvVUxBdEVlenh0TjZwZHRsb1ZZVjlsY2JwaEtkWlZmMENHWVo5ZDRXYnl1UUtuVndIZ1QyeVMzdkpNYjJ0WGFsWFd3NG1Da3gxUzkxSlIxbThiWVJnbFM5dGJESUw5VWFRQWtLUUo0SkRRTUIxNklpOHZIMm43T0h3; slave_user=gh_d75f63bde891; xid=b9366cd4714293524d360445c3a32a5d; openid2ticket_oZ9Nm0-zZIB3OT42X000EgyWXY48=Uk0vyqDYzpSs0tKTmMHZNowT/mYJ5U7JcWewdhAivR8="
    token = "107321640"
    appmsg_token = "appmsg_token"
    wechat_cookie = "wechat_cookie"

    nickname = "shaoshangchaoren"

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

    f = open("shaoshangchaoren.csv", 'a+')
    w = csv.writer(f, delimiter=',')
    # field_name = ['aid', 'appmsgid', 'cover', 'digest', 'itemidx', 'like_num', 'link', 'read_num', 'title', 'update_time']
    # w.writerow(field_name)
    i = 80
    while(i < 300):
        test = ArticlesAPI(
            official_cookie=official_cookie, token=token, outfile="outfile")

        data = test.get_data(nickname=nickname, begin=str(i))
        if i == 0:
            w.writerow(data[0].keys())
        for d in data:
            w.writerow(d.values())
        i += 5
        print("完成文章数......%d" % (i))

    f.close()
    
