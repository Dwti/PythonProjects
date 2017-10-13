from urllib import  request
from bs4 import  BeautifulSoup
import  re
def  download_web_context(re_url):
    req = request.Request(re_url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
    content = request.urlopen(req)
    if content.getcode() == 200:
        html_doc = content.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        return soup

def getall_stocks(re_url):
    req=request.Request(re_url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
    content=request.urlopen(req)
    if content.getcode() == 200:
        html_doc = content.read()
        soup=BeautifulSoup(html_doc,"html.parser")
        # links=soup.find_all("a",href=re.compile("news"))
        baseurl="http://www.yuncaijing.com"
        news_lists=soup.find("ul",id="newslist")#找到这个
        # section_lists=news_lists.find("section",class_="nc-arc-wrap")
        # # print(section_lists.find("time").get_text())
        # span=section_lists.find("span")
        # data=span.find("a")
        new_stock_list=soup.find_all("div",class_="related-stock")
        # print()
        for relate_stock in new_stock_list :
            stock_names=relate_stock.find_all("a",class_=" stock-gray")
            # increase=relate_stock.find("i",class_="ws-zdf")
            # print(increase)
            for s in stock_names:
                increase=s.find_all("i", class_="ws-zdf")
                for ic in increase:
                    print("【相关股票】："+s["title"] + ":" + s["data-wscode"] +"【详情】："+baseurl+s["href"])
                    #+ s["href"]+ "涨幅："+ic.get_text()
        nextpage = soup.find("a", class_="btn btn-default btn-block btn-loading")
        next_url=baseurl+nextpage["href"]
        count=0
        count=count+1
        while(count<=3):
            getall_stocks(next_url)
        print(next_url)
    # <a class="btn btn-default btn-block btn-loading" href="/insider/page_1.html">点击加载更多</a>


if __name__ == '__main__':
    print("最新消息相关的股票如下")
    re_url = "http://www.yuncaijing.com/insider/simple.html"
    getall_stocks(re_url)



