import requests
import getAudio


def getUrl(url, Referer, page):
    User_Agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    header = {
        "Referer": Referer,
        "User-Agent": User_Agent
    }

    response = requests.get(url=url, headers=header)
    json_data = response.json()

    titles = []
    bvids = []
    for item in json_data['data']['list']['vlist']:
        title = item['title']
        bvid = item['bvid']
        titles.append(title)
        bvids.append(bvid)
        getAudio.get(title, bvid, page)



#1 url = "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=d43894a0fe07adaa1210d4c7ea8beb9b&wts=1699535179"
Referer = "https://space.bilibili.com/1367537276/video"

urls = [
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=2&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=467d44f0a30711ec6b63e1b3a24eaea5&wts=1699753294",  #2
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=3&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=12ad32fc63d8826136c06acf4035e830&wts=1699753403",
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=4&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=1471041ee895041346237d63cbc99213&wts=1699753439",
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=5&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=e4224959b9974d39cf9f0df8beaea7c0&wts=1699753471",
    "https://api.bilibili.com/x/space/wbi/arc/search?mid=1367537276&ps=30&tid=0&pn=6&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEFNRCwgUkVOT0lSIChyZW5vaXIgTExWTSAxNS4wLjYpLCBPcGVuR0wgNC42KUdvb2dsZSBJbmMuIChBTU&w_rid=ba299f23e915f76a6ae0c952c53210c1&wts=1699753514"   #6
]


def main():
    for i in range(len(urls)):
        url = urls[i]
        page = i + 2
        print(page, "start!")
        getUrl(url, Referer, page)
        print(page, "finished!")


main()