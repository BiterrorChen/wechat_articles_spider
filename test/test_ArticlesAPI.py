# coding: utf-8
import os
import sys
from pprint import pprint
sys.path.append(os.getcwd())
from wechatarticles.ReadOutfile import Reader
from wechatarticles import ArticlesAPI

if __name__ == '__main__':
    username = "username"
    password = "password"
    official_cookie = "pgv_pvi=1487669248; pt2gguin=o1050048500; RK=HNKpqqlUfZ; ptcz=03619fd2cc87c821a05dd74db64c811b966c7bcf016c6be390035d7d0df5eda5; ptui_loginuin=1050048500; pgv_pvid=2310676148; tvfe_boss_uuid=e2b03ce7b83825f9; o_cookie=1050048500; mobileUV=1_161e20fc4e3_33a5f; ua_id=obXJMwa09a4Dr4T2AAAAAFgyhtDKX159iISsLMBtsjI=; mm_lang=zh_CN; pgv_si=s114059264; cert=zA4thAMovE1wyGxvJiSVrnz21RxpUP1U; pgv_info=ssid=s3277169200; sig=h018f7669f5088d7cdecf9c2bd4ccefd7ce7b73c30a4fb0ffa3878b18c3b9d7faff3fe821eaff5719cb; master_key=foHEw5x3ZVy4qD/K187UaWgH0L8Dft+BCijswI/0+Ns=; rewardsn=; wxuin=707586660; devicetype=iMacMacBookPro121OSXOSX10.12build(16A323); version=12030a10; lang=zh_CN; wxtokenkey=015d93ba85f86daf0ac91da2f1534462e42ae6ac477be2e99017732a9cc702d2; pass_ticket=AQq/t4QbI7UvEOJ0M/RAhTQ2wF2pI1H9uZgB4vO0QLPgpiFyJrNPNcuUMvYOkm8L; wap_sid2=COTUs9ECElxfZFQ0T0MyRWN6ZUFrR0R2eGZIQVVkMG5vOUU0T1BJRVFFZ3BRaXVSaG9xLU5sMG5kenBMQWdxdk5TM0RVeDFFeGQ5dW0tRHFGMjByLWlreW10Q0JXTE1EQUFBfjDUuorVBTgNQJVO; ptisp=ctc; uin=o1050048500; skey=@s8XMusXV6; uuid=3eda7d6ba0749098145692fbf846e20c; ticket=54173aeb6fa321b6cc70101d3335d78b00e5d718; ticket_id=gh_49cd2aabab1d; noticeLoginFlag=1; remember_acct=cqwzchenchao%40163.com; data_bizuin=3545725163; bizuin=3576487635; data_ticket=YlPnrp7u6fupM/9Fen9qhTHlJ8+zzgsdDfYg6GwPaweSWTEIqmR663SuOjCtaZtg; slave_sid=UXdqM29zN1NwWWo0a1RwVFJjd3BRQ2FnaVhocWVsT1JBWm9DTzJHZWxkZndoWHVycmtWOWhaZDN1MGVuNW9Sb2hmb1dZeFJfSmZzRktNRHRsRnJhQlNQdXh3Q2hWU3ZCQXpQQ2tkWU94aE9JSXZ2OUc0ZjhnRHozc0FBQkdDcUhocG0yWWhTU01Vakw0cVp2; slave_user=gh_49cd2aabab1d; xid=110dab884e674a1b560ae04440a1570e; openid2ticket_o63hX079u0qcxYSy_w_WFZyNkpeY=3ud7mSBnKEGSnLCphme9+0Y3JEfdx3SoKgvNJ8vUpeY="
    token = "973814043"
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
    test = ArticlesAPI(
        official_cookie=official_cookie, token=token, outfile="outfile")

    data = test.get_data(nickname=nickname, begin="0")
    print(data.__len__())
    pprint(data)
