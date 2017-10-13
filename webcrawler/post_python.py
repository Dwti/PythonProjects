from bs4 import BeautifulSoup
# import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
so = BeautifulSoup(html_doc,"html.parser")#使用python的标准的解释器
# print(so.prettify())
#获取文字
# print(so.get_text("Tillie"))
# for link in so.find_all('a'):
#     print(link.get("href"))
print(so.title)
print(so.find_all('a'))

