import  urllib
from urllib import request
import time
from bs4 import  BeautifulSoup
import re
#获取URL
baseurl = "http://www.yuncaijing.com"
# re_url="http://www.yuncaijing.com/insider/"
def deal_url(url):
    url_list=[]
    for i in range(0,20):
        i=str(i)
        if i==0:
            re_url = url + "simple.html"
            url_list.append(re_url)
        else:
            re_url = url + "page_" + i + ".html"
            url_list.append(re_url)
            url=url
    return url_list

#改变为soup对象

def download_webcontent():
    re_url = "http://www.yuncaijing.com/insider/"
    # time.sleep(2)
    url_list = deal_url(re_url)
    # print(url_list)
    soups = []
    for url in url_list:
        # 设置请求头文件信息
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        req=urllib.request.Request(url,headers=headers)
        resq=urllib.request.urlopen(req,timeout=2)
        if resq.getcode() == 200:
            html_doc = resq.read()
            soup=BeautifulSoup(html_doc,"html.parser")
            soups.append(soup)
    return soups
#处理相关的网页数据
def deal_data(soup):
    print("最新消息相关的股票如下")
    new_stock_list = soup.find_all("div", class_="relate-stock")
    # print(new_stock_list)
    for relate_stock in new_stock_list:
        stock_names = relate_stock.find_all("a", class_="stock-gray")
        for s in stock_names:
            print("【相关股票】：" + s["title"] + ":" + s["data-wscode"] + "【详情】：" + baseurl + s["href"])
def getall_news(soup):
        print("最新消息相关的股票信息:")
        news_list_divs=soup.find_all("div",class_="nc-yc nc-arc-wrap")
        for news_lists in news_list_divs:
            time_lists = news_lists.find_all("kbd")
            news_lists=news_lists.find_all("a",target="_blank")
            for time in time_lists:
                print()
                for news_list in news_lists:
                    print(time.get_text()+"【"+news_list["title"]+"】"+baseurl+news_list["href"])
def write_files():
    with open('C:/Users/srt-k12001/Desktop/医疗.txt', 'w') as f:
        f.write('Hello, world!')
if __name__ == '__main__':
    #write_files()
    # print("新闻")
    soups=download_webcontent()
    for soup in soups:
        links = soup.find_all("a", class_="title", text=re.compile("医疗"))
        for link in links:
            print("【"+link["title"]+"】"+ baseurl + link["href"])
            with open('C:/Users/srt-k12001/Desktop/医疗.txt', 'w') as f:
                f.write("【"+link["title"]+"】"+ baseurl + link["href"])



