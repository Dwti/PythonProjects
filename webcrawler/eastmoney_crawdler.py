from bs4 import  BeautifulSoup
from urllib import  request
import re
# re_url="http://www.yuncaijing.com/insider/simple.html"
re_url="https://www.cailianpress.com"
req=request.Request(re_url)

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0")
content=request.urlopen(req)
if content.getcode() == 200:
    html_doc=content.read()
    soup=BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
    links=soup.find_all("a",href=re.compile("news"))
    baseurl="http://www.yuncaijing.com"
    #print(soup.find_all("h4"))
    # print(soup.get_text())
    # print(soup.prettify())
    links=soup.find_all("a", class_="title",text=re.compile("雄安"))
    # print(soup.find_all("a", text=re.compile("雄安")))
    for link in links:
        print(link["title"]+baseurl+link["href"])


    # for link in links:
    #   print(link.get_text()+":"+baseurl+link["href"])