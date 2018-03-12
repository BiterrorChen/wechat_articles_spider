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
    official_cookie = "pgv_pvi=1487669248; pt2gguin=o1050048500; RK=HNKpqqlUfZ; ptcz=03619fd2cc87c821a05dd74db64c811b966c7bcf016c6be390035d7d0df5eda5; ptui_loginuin=1050048500; pgv_pvid=2310676148; tvfe_boss_uuid=e2b03ce7b83825f9; o_cookie=1050048500; mobileUV=1_161e20fc4e3_33a5f; ua_id=obXJMwa09a4Dr4T2AAAAAFgyhtDKX159iISsLMBtsjI=; mm_lang=zh_CN; pgv_si=s114059264; cert=zA4thAMovE1wyGxvJiSVrnz21RxpUP1U; pgv_info=ssid=s3277169200; rewardsn=; wxuin=707586660; devicetype=iMacMacBookPro121OSXOSX10.12build(16A323); version=12030a10; lang=zh_CN; wxtokenkey=015d93ba85f86daf0ac91da2f1534462e42ae6ac477be2e99017732a9cc702d2; pass_ticket=AQq/t4QbI7UvEOJ0M/RAhTQ2wF2pI1H9uZgB4vO0QLPgpiFyJrNPNcuUMvYOkm8L; wap_sid2=COTUs9ECElxfZFQ0T0MyRWN6ZUFrR0R2eGZIQVVkMG5vOUU0T1BJRVFFZ3BRaXVSaG9xLU5sMG5kenBMQWdxdk5TM0RVeDFFeGQ5dW0tRHFGMjByLWlreW10Q0JXTE1EQUFBfjDUuorVBTgNQJVO; ptisp=ctc; uin=o1050048500; noticeLoginFlag=1; remember_acct=cqwzchenchao%40163.com; uuid=0e22c659ac3a9a886e01af4b05a2c5a8; xid=5aa3f39a06ca41cf1b0ec7190dd301d4; skey=@qf34DZ6kI; sig=h01e38e87afbb75aa216e45809796769011501c78f02187110d80686867ff416876521869578561ead1; data_bizuin=3546731367; data_ticket=1s8cy0LFMINHNEeGXuEsMkKOt0NmM4UWRgJ5O8f9yxEaf6BOIhr6a9SEoN3wf7Xg; master_key=upf+3wG8p7uPtRi0Dzxb8GiF+b7V04+u559zBUfZGLg=; master_user=gh_1b8c5acce870; master_sid=emQ4TVdUcllPaEZmM1ZRQUhZZHB1OXVKN2ttUjZUWWdNd2JXaWZyeVFnZFpqUDN5U25udlp0U0Zra01kTWVRQ3U5MkhIN3lIT0NxSmp2ZDhmeVViM1YyM0RmQXl5ZllqWEh6eHNMS0FwV2xidElPWmxwSVUwd3FMT25WeXBpRzhONllZZU1FdjYwNW1keUhW; master_ticket=6a5e105a5f4fb01474e51acbb40fe7bf; slave_user=gh_d75f63bde891; slave_sid=c2t6bU9jcDNIa1ZsemJuUm9JcWFBZmxrNFFjWWJ5V2VXTWJQYUlBOTZDMkxfOE9pQnkyRU1aZmtydFkySUQ2akpmZkRuXzRET2p1RW9tZklMU2pzQThReDBYOTFEOVhKbm9Xc2g4Q1NEX3pCMW14Ym5kUEpvSDJia2YxZ2ozVGNtQzRRMGFFY0M5SnBkMHlh; bizuin=3585491970"
    token = "584178091"
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
    i = 300
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
    
