# rss-reborn

I hate to have too many apps in my phone for notification. so i build a system to send me email when there's updates. It's no longer needed to check updates across websites, so it'd help concentration. 

## feature

1. modulized development in jupyter introduced by [course-v3/nbs/dl2 at master · fastai/course-v3](https://github.com/fastai/course-v3/tree/master/nbs/dl2)
2. webcrawler

## now supports

1. bilibili notification
2. anilist notification

## run

```
pip install uncurl fire requests
cd nb
# firt to confiure 
python main
```

## first to configure：

all using utf-8, Unix newline
```
personal_info.json 
// webcrawler related see bellow for clarication
bili_curl.txt 
anichar_url_with_token.txt
```

### personal_info.json

smtp server which sends email and email desitination.

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



## code structure

`./nb/*.ipynb`

### generated code

`./nb/*.py`

### data cache

if its empty all notification will be sent

`./nb/*.json`

### `notification api` in `curl fomart`
```
*_curl.txt //  parsing to `requests` using `uncurl`
```


## setting up qq mail

qq邮箱请password请使用鉴权码:

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256%27)

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=371



## setting up `.txt*`


### bilibili

goto: https://t.bilibili.com/pages/nav/index_new#/video

api url: https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new

method: get

copy cURL(POSIX) on firefox webconsle/network filter by XHR saved as `bili_curl.txt`.

### anichart

> steal your auth token from anichart to avoid trouble and save my life.

web: https://anichart.net/settings click login and it'd redirect to` https://anichart.net/auth#access_token=*` copy that url save as `anichar_url_with_token.txt`.

method: get

`ani_curl.txt` is curl cmd using [Implicit Grant - AniList APIv2 Docs](https://anilist.gitbook.io/anilist-apiv2-docs/overview/oauth/implicit-grant#making-authenticated-requests) 'js code on web console replacing query data found at [Notifications · AniList](https://anilist.co/notifications) and token stolen at anichart. token is said to be valid for a year. DONT modify.

## cache structure

`./nb/*.json` contains notification data which I call cards. cards is a dict which key is `card_id` and `card`. each `card` is in unified notification structure. `card_id` is used to index card.

`cvt_cards` means convert card for tranforms api data to cards.

### cards

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


## ref

1. https://github.com/waynecrasta/siteWatcher/blob/master/siteWatcher.py
2. https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
3. https://stackoverflow.com/questions/5952344/how-do-i-format-a-string-using-a-dictionary-in-python-3-x
4. https://stackoverflow.com/questions/882712/sending-html-email-using-python
5. https://avilpage.com/2018/03/convert-browser-requests-to-python-requests.html
6. https://docs.python.org/3/library/smtplib.html
7. https://github.com/fastai/course-v3/blob/master/nbs/dl2/00_exports.ipynb
8. https://docs.python.org/3/library/traceback.html


## 使用时间

初步:7个小时。
第一次修缮:2小时

## TODO

5. 增加#clear_output_when_commit，#clear_when_commit，两种类型，方便jupyter notebook commit
