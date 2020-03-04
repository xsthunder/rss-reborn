# 订阅自动发送邮件

好处：被动地接受信息源，减少app安装

## 需要在项目根目录配置：

all using utf-8, Unix newline
```
personal_info.json 
//用于获取接口的相关，看下面的说明
bili_curl.txt 
anichar_url_with_token.txt
```

### personal_info.json 结构

```json
{
    "sender":"example_render@qq.com",
    "password":"example_auth_code",
    "recipient":"example_recipient@qq.com",
    "smtp":{
        "address":"smtp.qq.com",
        "port":465
    }
}
```

## 运行

```
cd nb
python main
```

### 代码

./nb/*.ipynb

### 生成代码

./nb/*.py

### 缓存

缓存为空则发送所有

./nb/*.json

### curl代码

*_curl.txt

## 邮箱配置

qq邮箱请password请使用鉴权码:

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256%27)

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=371



## 已有订阅源，配置curl.txt

copy cURL(POSIX) on firefox webconsle/network filter by XHR，保存成`*_curl.txt`

### bilibili

web: https://t.bilibili.com/pages/nav/index_new#/video

url: https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new

method: get

保存成`bili_curl.txt`

### anichart

> steal your auth token from anichart to avoid trouble and save my life

web: https://anichart.net/settings click login and it'd redirect to` https://anichart.net/auth#access_token=*` copy that url save as `anichar_url_with_token.txt`

method: get

`ani_curl.txt` is curl cmd using [Implicit Grant - AniList APIv2 Docs](https://anilist.gitbook.io/anilist-apiv2-docs/overview/oauth/implicit-grant#making-authenticated-requests) 'js code on web console replacing query data found at [Notifications · AniList](https://anilist.co/notifications) and token stolen at anichart. token is said to be valid for a year.

## 数据说明

每一个card是一个字典，由card和它的key构成cards

`cvt_cards`是convert card的缩写，用于转换成下面格式的统一格式，缓存文件格式

### 样例
```json
{
    "93211769": {
        "content": {
            "title": "【精彩回顾】李玲：中国人究竟需要什么样的医疗制度？",
            "desc": "一勺思想·李玲：关于中国医疗体系的讨论",
            "pic": "https://i1.hdslb.com/bfs/archive/39ebde04b813e5e2c804749938495b265860526d.jpg@64w_36h_1c.jpg"
        },
        "url": "https://www.bilibili.com/video/av93211769",
        "time": "2020-03-02T21:26:31"
    }
}
```


## 参考

1. https://github.com/waynecrasta/siteWatcher/blob/master/siteWatcher.py
2. https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
3. https://stackoverflow.com/questions/5952344/how-do-i-format-a-string-using-a-dictionary-in-python-3-x
4. https://stackoverflow.com/questions/882712/sending-html-email-using-python
5. https://avilpage.com/2018/03/convert-browser-requests-to-python-requests.html
6. https://docs.python.org/3/library/smtplib.html
7. https://github.com/fastai/course-v3/blob/master/nbs/dl2/00_exports.ipynb
8. https://docs.python.org/3/library/traceback.html

## depend

pip install uncurl fire requests


## 使用时间

初步:7个小时。
第一次修缮:2小时

## TODO

5. 增加#clear_output_when_commit，#clear_when_commit，两种类型，方便jupyter notebook commit
