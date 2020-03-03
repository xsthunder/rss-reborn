# 订阅自动发送邮件

好处：被动地接受信息源，减少app安装

## 配置

all using utf-8, Unix newline
```
personal_info.json
bili_curl.txt
ani_curl.txt
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

## 邮箱配置

qq邮箱请password请使用鉴权码:

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256%27)

https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=371

## depend

pip install uncurl fire requests

## TODO

1. 等待鉴权失效后，独立鉴权文件。
2. 增加用于更新鉴权后，增加单个python文件测试，加入subname=subname+"测试"，需要绕过main，直接运行get_cards, get_msg, sendMail
3. 上传github，需要避开敏感信息
4. 修改缓存为空时，发送所有
5. 增加#clear_output_when_commit，#clear_when_commit，两种类型，方便jupyter notebook commit

## 使用时间

初步：使用7个小时。

## 已有订阅源

copy cURL(POSIX) on firefox webconsle/network filter by XHR

### bilibili

web: https://t.bilibili.com/pages/nav/index_new#/video

url: https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new

method: get

### anichart

web: https://anilist.co/notifications goto airing

url: https://anilist.co/graphql

method: get



## 参考

1. https://github.com/waynecrasta/siteWatcher/blob/master/siteWatcher.py
2. https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
3. https://stackoverflow.com/questions/5952344/how-do-i-format-a-string-using-a-dictionary-in-python-3-x
4. https://stackoverflow.com/questions/882712/sending-html-email-using-python
5. https://avilpage.com/2018/03/convert-browser-requests-to-python-requests.html
6. https://docs.python.org/3/library/smtplib.html
7. https://github.com/fastai/course-v3/blob/master/nbs/dl2/00_exports.ipynb
8. https://docs.python.org/3/library/traceback.html