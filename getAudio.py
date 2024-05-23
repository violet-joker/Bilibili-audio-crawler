import requests
import json
import re
import os

def get(title, bvid, page):
    url = "https://www.bilibili.com/video/"
    # bvid = "/BV1Yg4y1c7qZ/" 
    url = url + bvid + '/'
    title = title.replace(" ", "") + ".mp3"
    PATH = "/home/xf/PY/file/"
    paths = ["audio1/", "audio2/", "audio3/", "audio4/", "audio5/", "audio6/"] 
    
    
    # PATH = PATH + paths[page-1]
    # old = title + title
    # new = title 

    # if (os.path.exists(PATH + old)):
    #     os.chdir(PATH)
    #     os.rename(old, new)
    #     print(title)
    
    # return

    for i in paths:
        item = PATH + i + title
        path = PATH + paths[page-1] + title
        if (os.path.exists(item)):   #去重
            print(title, 'has been downloaded')
            return


    User_Agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    Referer = url

    headers = {
        "user-agent": User_Agent,
        "Referer": Referer
    }

    res=requests.get(url=url,headers=headers)

    obj=re.compile(r'window.__playinfo__=(.*?)</script>',re.S)
    html_data=obj.findall(res.text)[0] #从列表转换为字符串
    json_data=json.loads(html_data)

    audios=json_data['data']['dash']['audio']
    audio_url=audios[0]['baseUrl']


    resp2=requests.get(url=audio_url,headers=headers)
    path = PATH + paths[page-1] + title
    with open(path, mode='wb') as f:
        f.write(resp2.content)
    print(title, 'has been downloaded successfully!')