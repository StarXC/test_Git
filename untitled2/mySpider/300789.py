#!/usr/bin/env python3
#__*__coding = utf-8 __*__
import requests
from bs4 import BeautifulSoup as Bs4

head_url = "http://www.300789.com"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
def get_first_url():
    list_href = []
    responses = requests.get(head_url)
    # print(responses.text)
    soup = Bs4(responses.text, "lxml")
    # print(soup)
    urls_li = soup.find_all(["a","br","tr"])
    # urls_li = soup["href"]
    # print(urls_li)
    # urls_li = soup.select(selector  = ".a")
    # print(urls_li)
    for url_li in urls_li:
        urls = url_li.select("a")
        # print(urls)
        for url in urls:
            url_href = url.get("href")
            a = list_href.append(head_url + url_href)
            # print(a)
            out_url = list(set(list_href))
            # print(out_url)
    # print(out_url)
    return out_url




def get_next_url(urllist):
    url_list = []
    for url in urllist:
        response = requests.get(url,headers=headers)
        soup = Bs4(response.text,"lxml")
        urls = soup.find_all("a")
        if urls:
            for url2 in urls:
                url2_1 = url2.get("href")
                if url2_1:
                    if url2_1[0] == "/":
                        url2_1 = head_url + url2_1
                        url_list.append(url2_1)
                        if url2_1[0:24] == "http://www.300789.com":
                            url2_1 = url2_1
                            url_list.append(url2_1)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        else:
            pass
    url_list2 = set(url_list)
    for url_ in url_list2:
        res = requests.get(url_)
        if res.status_code ==200:
            print(url_)
    print(len(url_list2))
    get_next_url(url_list2)


if __name__ == "__main__":
    urllist = get_first_url()
    # print(urllist)
    get_next_url(urllist)

