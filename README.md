# 微信公众号文章爬虫

实现思路:

1. 从微信公众号平台获取微信公众所有文章的url

2. 登录微信PC端获取文章的阅读数、评论等信息

完整思路可以参考我的博客: [微信公众号爬虫](http://blog.csdn.net/wnma3mz/article/details/78570580)

## 第三方包

- `requests`: 爬取内容

**支持两种微信公众号登录方式**

下面微信公众号登录方式选用其一即可

1. 账号密码爬虫，输入账号密码后，扫描二维码登录。自动获取cookie和token。此方法需要安装`matplotlib`和`PIL`用于显示二维码图片

2. cookie、token登录，手动复制cookie和token。

**url支持三种存储方式**

1. txt存储（不建议）

2. sqlite3存储。自带模块，不需要额外安装

3. mongo存储。需要安装`pymongo`

## API实例

以下具体代码见`test/`目录下的实例代码。

关于变量名的说明

|     变量名      |        作用        |
| :-------------: | :----------------: |
|    usernmae     |  个人公众号的账号  |
|    password     |  个人公众号的密码  |
| official_cookie | 个人公众号的cookie |
|    token     |  个人公众号的token  |
|    appmsg_token     |  个人微信号的appmsg_token  |
| wechat_cookie | 个人微信号的cookie |
|    nickname     |  需要获取文章的公众号名称  |
|    query     | 筛选公众号文章的关键词  |
| outfile | mitmproxy抓包获取请求的保存文件 |
| begin | 从第几篇文章开始爬取 |
| count | 每次爬取的文章数(最大为5, 但是返回结果可能会大于５) |


official_cookie和token获取方式见[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_cookie_token.md)

wechat_cookie和appmsg_token手动获取的介绍，可以参考[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_appmsg_token.md)

wechat_cookie和appmsg_token自动获取的介绍(需要安装`mitmproxy`)，可以参考[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/关于自动获取微信参数.md)。

wechat_cookie和appmsg_token建议获取每天或者每半天获取一次即可。此处通过上面获取到的url即可无限爬取，没有次数限制

```python
# 导入模块
import sys
sys.path.append(path + "/wechat_articles_spider")
from wechatarticles import OfficialWeChat
from wechatarticles import LoginWeChat
from wechatarticles import ReadOutfile
from wechatarticles import ArticlesAPI
```

### 一次性获取文章的信息(阅读、点赞、评论信息)

```python
# 下面三种方式任选一种即可

# 手动输入所有参数
test = ArticlesAPI(
    official_cookie=official_cookie,
    token=token,
    appmsg_token=appmsg_token,
    wechat_cookie=wechat_cookie)

# 输入账号密码，自动登录公众号，手动输入appmsg_token和wechat_cookie
test = ArticlesAPI(
    username=username,
    password=password,
    appmsg_token=appmsg_token,
    wechat_cookie=wechat_cookie)

# 手动输入official_cookie和token, 自动获取appmsg_token和wechat_cookie
test = ArticlesAPI(
    official_cookie=official_cookie, token=token, outfile=outfile)

data = test.get_data(nickname=nickname, begin="0")
```

### 分解步骤
#### 步骤一: 获取公众号的所有文章url

此处有次数限制，不可一次获取太多url(获取超过30、40条貌似就会失败)。解决方案多个账号同时爬取

```python
# 实例化爬取对象
# 账号密码自动获取cookie和token
test = OfficialWeChat(username=username, password=password)
# 手动输入账号密码
test = OfficialWeChat(cookie=official_cookie, token=token)

# 输入公众号名称，获取公众号文章总数
articles_sum = test.totalNums(nickname)
# 输入公众号名称，获取公众号部分文章信息, 每次最大返回数为5个
articles_data = test.get_articles(nickname, begin="0", count="5")
# 输入公众号名称，获取公众号的一些信息
officical_info = test.get_official_info(nickname)
# 输入公众号名称，输入关键词，获取公众号相关文章信息, 每次最大返回数为5个
articles_data_query = test.get_articles(nickname, query=query, begin="0", count="5")
# 输入公众号名称，输入关键词，获取公众号相关文章总数
articles_sum_query = test.totalNums(nickname, query=query)

# 保存数据为txt格式
test.save_txt("test.txt", artiacle_data)
# 保存数据为sqlite3
test.save_sqlite("test.db", "test", artiacle_data)
# 保存数据到mongo中
test.save_mongo(data, host=host, port=27017,name=name, password=password, dbname=dbname, collname=collname)
```

#### 步骤二：登录微信PC端获取文章信息

```python
# 支持自动获取appmsg_token和cookie
appmsg_token, cookie = Reader().contral(outfile)

# 实例化爬取对象
# 账号密码自动获取cookie和token
test = LoginWeChat(appmsg_token=appmsg_token, cookie=wechat_cookie)
# 获取微信文章的详细信息（包括文章的阅读数、评论数、点赞数等）
# 这里的articles_url是上面获取到的`articles_data`数组中每一项的"link"
test.GetSpecInfo(article_url=article_url)
# 获取文章所有的评论信息(无需appmsg_token和cookie)
comments = test.get_comments(link)
# 获取文章阅读数点赞数
read_num, like_num = test.get_read_like_num(link)
```

## TO-DO

1. 完善API设计