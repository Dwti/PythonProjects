from bs4 import  BeautifulSoup
from urllib import  request
import re
html_doc="""
"""
count=0
re_url="http://www.yuncaijing.com/insider/simple.html"
req=request.Request(re_url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
content=request.urlopen(req)
if content.getcode() == 200:
    html_doc=content.read()
    soup=BeautifulSoup(html_doc,"html.parser")
    # links=soup.find_all("a",href=re.compile("news"))
    baseurl="http://www.yuncaijing.com"
    news_lists=soup.find_all("ul",id="newslist")#找到这个
    for news_list in news_lists:
        section_lists=news_list.find_all("section",class_="nc-arc-wrap")
        # stocks_list = news_list.find_all("div", class_="related-stock new-stock-list")
        # for stocks in stocks_list:
        #     stocks = stocks_list.find_all("a", class_=" stock-gray")
        #     print(stocks["title"] + ":" + stocks["data-wscode"] + ">>>>" + "详情地址:" + baseurl + stocks["href"])
        for section_list in section_lists:
            print(section_list.find("time").get_text())
            li_lists=section_list.find_all("li",class_="share-weibo" )
            for data in li_lists:
                count=count+1
                context=data["data-title"]+baseurl+data["data-url"]
                print(context.strip())
                print("--------------------------------------------------------------------------------------------------")
            #print(li_lists)
print(count)