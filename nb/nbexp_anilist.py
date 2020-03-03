
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./anilist.ipynb

from nbexp_personal import sendEmail
from nbexp_bilibili import get_main, partial, fetch_code, operator, itemgetter, render_msg, get_time, write_json, exists, read_json
from nbexp_bilibili import render_html
get_time(0)

# 复制为cCURL（posix）
with open('../ani_curl.txt', 'r', encoding='UTF-8') as f:
    code = f.read()

fetch = partial(fetch_code, code)

def goto_hell(d):
    if isinstance(d, dict):
        values = list(d.values())
        if __name__ == "main":
            assert len(values) == 1, values
        return goto_hell(values[0])
    return d
goto_hell({1:{2:3}})

def cvt_link(name):
    tempate = 'https://nyaa.si/?f=0&c=1_4&q=%5BOhys-Raws%5D+'
    name = name.replace(' ', '+')
    return tempate + name

# 变成和 bilibili.json相同格式
def cvt_card(content):
#     content = contents[0]
    media = content['media']
    obj = {
        "content":{
            "title":goto_hell(media['title']),
            "desc":str(content['episode']) + ' AIRED',
            "pic":goto_hell(media['coverImage']),
        },
        "url":cvt_link(goto_hell(media['title'])),
        "time":get_time(content['createdAt'])
    }
    return obj

def cvt_cards(j):

    notifications = j['data']["Page"]["notifications"]
    content_ids = map(operator.itemgetter('id'), notifications)
    content_ids = map(str, content_ids)
    contents = map(itemgetter('episode', 'media', 'createdAt'), notifications)
    content_ids, contents  = map(list, (content_ids, contents))
    contents = map(cvt_card, contents)

    return dict(zip(content_ids, contents ))

def get_cards():
    j = fetch()
    return cvt_cards(j)
json_path = "./anilist.json"
main = get_main(json_path, get_cards, "ani")