from urllib import request
from bs4 import  BeautifulSoup
import re
#百度百科的
# resUrl="https://baike.baidu.com/item/Python/407313?fr=aladdin"
#东方财富网站的
resUrl="http://tianqi.2345.com/heyuan/59293.htm"
#response=request.urlopen(resUrl)
req=request.Request(resUrl)
#模拟浏览器去请求
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
response=request.urlopen(req)
if response.getcode() == 200:
    html_doc=response.read()
    soup=BeautifulSoup(html_doc,"html.parser",from_encoding="gbk")
    # links=soup.find_all('a',target="_blank",text=re.compile(r"人民日报"))
    links = soup.find_all('a')
    # print(soup.find_all('a'))
    base_url="https://baike.baidu.com/item"

    for link in links:
        # print(link.get_text()+":"+base_url+link["href"])
        # if link.get_text()== "华为":
        #     print(link.get_text() + ":" + base_url + link["href"])
        print(link.get_text() + ":" + link["href"])
    # print(response.read().decode("utf8"))