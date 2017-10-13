from bs4 import  BeautifulSoup
from urllib import  request
import re
import urllib
html_doc="""
<html>
 <head>
  <script type="text/javascript">
   !window.addEventListener && (location.href = '/help/browser_update.html')
  </script>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0, user-scalable=0" name="viewport"/>
  <title>
   今日股市最新消息_股票市场7*24小时滚动资讯直播_云财经股票内参平台简约版
  </title>
  <meta content="股市最新消息,股票市场,股市直播,股票内参" name="keywords"/>
  <meta content="股市最新消息7x24小时直播！云财经股票内参平台提供今日股市最新消息，最快股市直播，财经资讯、股票市场消息、行业动态、个股公告，股市最新消息快人一步。" name="description"/>
  <link href="http://aliyun.yuncaijing.com/res/pc/assets/css/xui.css?v=201701172326" rel="stylesheet"/>
  <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="shortcut icon" type="image/x-icon">
   <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="icon" type="image/x-icon"/>
   <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="bookmark" type="image/x-icon"/>
   <link href="http://aliyun.yuncaijing.com/res/pc/assets/css/xui_v2.css?v=201701172326" rel="stylesheet"/>
   <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="shortcut icon" type="image/x-icon">
    <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="icon" type="image/x-icon"/>
    <link href="http://aliyun.yuncaijing.com/res/pc/assets/img/favicon.ico?v=201701172326" rel="bookmark" type="image/x-icon"/>
    <link href="http://aliyun.yuncaijing.com/res/pc/assets/css/simple_news.css?v=201701172326" rel="stylesheet"/>
    <script src="/auth/query_login_js.html?v=201701172326" type="text/javascript">
    </script>
   </link>
  </link>
 </head>
 <body>
  <div id="neican-wrap">
   <div class="neican-body">
    <section class="main">
     <aside class="line pa">
     </aside>
     <header class="neican-header tiny-text">
      <i class="iconYCJ icon-news-live-ycj">
      </i>
      <time class="time bold fl big-text">
       7X24小时股票内参快讯
      </time>
      <aside class="fl switch-box">
       <div class="fl">
        <div class="switch-wrap">
         <div class="switch-text">
          <input checked="" id="switch-refresh" type="checkbox"/>
          <label for="switch-refresh">
          </label>
         </div>
         <span>
          自动刷新
         </span>
        </div>
        <i class="icon icon-question" data-placement="bottom" data-title="可以实时自动刷新本页面，当有股市最新消息时，会第一时间显示在本页面" data-toggle="tooltip">
        </i>
       </div>
       <div class="fl">
        <div class="switch-wrap">
         <div class="switch-text">
          <input checked="" id="switch-audio" type="checkbox"/>
          <label for="switch-audio">
          </label>
         </div>
         <span>
          声音提醒
         </span>
        </div>
        <i class="icon icon-question" data-placement="bottom" data-title="当有股市最新消息推送时，电脑会发出声音提示您" data-toggle="tooltip">
        </i>
       </div>
       <div class="fl">
        <div class="switch-wrap">
         <div class="switch-text">
          <input checked="" id="switch-notify" type="checkbox"/>
          <label for="switch-notify">
          </label>
         </div>
         <span>
          桌面通知
         </span>
        </div>
        <a data-remote="/news/modal/5363602" data-target="#simple-modal" data-toggle="modal" href="/news/id_5363602.html">
         <i class="icon icon-question">
         </i>
        </a>
       </div>
       <div class="fl">
        <div class="test-btn">
         <button class="btn btn-primary" id="noti" type="button">
          测试弹窗
         </button>
         <span>
          <a data-remote="/news/modal/5363602" data-target="#simple-modal" data-toggle="modal" href="/news/id_5363602.html">
           如何设置
          </a>
         </span>
        </div>
        <i class="icon icon-question" data-placement="bottom" data-title="请在打开桌面通知开关后，点击该按钮测试是否可以接收桌面通知" data-toggle="tooltip">
        </i>
       </div>
      </aside>
     </header>
     <ul id="newslist">
      <li class="list">
       <i class="widget share-btn iconYCJ icon-sharing-ycj opacity-seven">
       </i>
       <section class="nc-arc-wrap ">
        <time>
         今天 09:33
        </time>
        <span>
         <div class="nc-con">
          <h4>
           <a data-remote="/news/modal/9736483" data-target="#simple-modal" data-toggle="modal" href="/news/id_9736483.html" title="郝鹏赴中国国电调研  强调推进改革重组">
            【郝鹏赴中国国电调研  强调推进改革重组】
           </a>
          </h4>
          10月9日，国资委党委书记郝鹏赴中国国电集团公司检查调研，郝鹏要求，中国国电要把握重组契机，坚定不移深化改革，深入落实好新发展理念，进一步明确公司战略定位、业务布局和发展规划，扎实推进供给侧结构性改革，坚决打好瘦身健体提质增效攻坚战，确保企业平稳健康发展。
          <span class="related-stock-btn">
           <button class="tag" data-toggle="dropdown" data-toggleid="2389" type="button">
            <i class="iconYCJ icon-newstag-ycj">
            </i>
            国电集团
           </button>
          </span>
         </div>
         <ul class="share-wrap">
          <li class="share-weibo" data-share="weibo" data-title="【郝鹏赴中国国电调研  强调推进改革重组】 10月9日，国资委党委书记郝鹏赴中国国电集团公司检查调研，郝鹏要求，中国国电要把握重组契机，坚定不移深化改革，深入落实好新发展理念，进一步明确公司战略定位、业务布局和发展规划，扎实推进供给侧结构性改革，坚决打好瘦身健体提质增效攻坚战，确保企业平稳健康发展。" data-url="/news/id_9736483.html">
           <i class="icon icon-sina">
           </i>
           微博
          </li>
          <li class="share-wechat pr" data-share="wechat">
           <i class="icon icon-wechat-dark">
           </i>
           微信
           <div class="share-wechat-wrap">
            <div class="qrcode">
            </div>
           </div>
          </li>
         </ul>
         <div class="dropdown" data-toggleid="2389">
          <ul class="dropdown-menu new-stock-list">
           <li>
            <a class="" data-showchart-code="000780" data-wscode="000780" href="/quote/sz000780.html" target="_blank" title="ST平能">
             <i>
              ST平能000780
             </i>
             <i class="ws-zdf">
             </i>
            </a>
           </li>
           <li>
            <a class="" data-showchart-code="000966" data-wscode="000966" href="/quote/sz000966.html" target="_blank" title="长源电力">
             <i>
              长源电力000966
             </i>
             <i class="ws-zdf">
             </i>
            </a>
           </li>
           <li>
            <a class="" data-showchart-code="300105" data-wscode="300105" href="/quote/sz300105.html" target="_blank" title="龙源技术">
             <i>
              龙源技术300105
             </i>
             <i class="ws-zdf">
             </i>
            </a>
           </li>
           <li>
            <a class="" data-showchart-code="000635" data-wscode="000635" href="/quote/sz000635.html" target="_blank" title="英力特">
             <i>
              英力特000635
             </i>
             <i class="ws-zdf">
             </i>
            </a>
           </li>
           <li class="more">
            <a href="/story/details/id_2389.html" target="_blank" title="国电集团">
             更多
             <i class="icon icon-triangle-right">
             </i>
            </a>
           </li>
          </ul>
         </div>
        </span>
       </section>
      </li>
      <li class="list">
       <i class="widget share-btn iconYCJ icon-sharing-ycj opacity-seven">
       </i>
       <section class="nc-arc-wrap ">
        <time>
         今天 09:30
        </time>
        <span>
         <div class="nc-con">
          <h4>
           <a data-remote="/news/modal/9736393" data-target="#simple-modal" data-toggle="modal" href="/news/id_9736393.html" title="金莱特今日临停">
            【金莱特今日临停】
           </a>
          </h4>
          云财经讯，金莱特今日临停，拟披露重大事项。
         </div>
         <ul class="share-wrap">
          <li class="share-weibo" data-share="weibo" data-title="【金莱特今日临停】云财经讯，金莱特今日临停，拟披露重大事项。" data-url="/news/id_9736393.html">
           <i class="icon icon-sina">
           </i>
           微博
          </li>
          <li class="share-wechat pr" data-share="wechat">
           <i class="icon icon-wechat-dark">
           </i>
           微信
           <div class="share-wechat-wrap">
            <div class="qrcode">
            </div>
           </div>
          </li>
         </ul>
        </span>
        <div class="related-stock new-stock-list">
         <p>
          相关股票
         </p>
         <a class=" stock-gray" data-showchart-code="002723" data-wscode="002723" href="/quote/sz002723.html" target="_blank" title="金莱特">
          <i>
           金莱特002723
          </i>
          <i class="ws-zdf">
           0%
          </i>
         </a>
        </div>
       </section>
      </li>
      <li class="list">
       <i class="widget share-btn iconYCJ icon-sharing-ycj opacity-seven">
       </i>
       <section class="nc-arc-wrap ">
        <time>
         今天 09:29
        </time>
        <span>
         <div class="nc-con">
          <h4>
           <a data-remote="/news/modal/9736363" data-target="#simple-modal" data-toggle="modal" href="/news/id_9736363.html" title="开盘快报：两市微幅低开 个股涨跌互现">
            【开盘快报：两市微幅低开 个股涨跌互现】
           </a>
          </h4>
          云财经讯，沪深两市微幅低开，沪指报3373.34点，创业板指报1890.66点，个股涨跌互现。盘面上网约车、尾气治理、互联网彩票等板块涨幅居前；西安自贸区、通信设备、5G等板块跌幅居前。
         </div>
         <ul class="share-wrap">
          <li class="share-weibo" data-share="weibo" data-title="【开盘快报：两市微幅低开 个股涨跌互现】云财经讯，沪深两市微幅低开，沪指报3373.34点，创业板指报1890.66点，个股涨跌互现。盘面上网约车、尾气治理、互联网彩票等板块涨幅居前；西安自贸区、通信设备、5G等板块跌幅居前。" data-url="/news/id_9736363.html">
           <i class="icon icon-sina">
           </i>
           微博
          </li>
          <li class="share-wechat pr" data-share="wechat">
           <i class="icon icon-wechat-dark">
           </i>
           微信
           <div class="share-wechat-wrap">
            <div class="qrcode">
            </div>
           </div>
          </li>
         </ul>
        </span>
       </section>
      </li>
      <li class="list">
       <i class="widget share-btn iconYCJ icon-sharing-ycj opacity-seven">
       </i>
       <section class="nc-arc-wrap ">
"""

soup=BeautifulSoup(html_doc,"html.parser")
# links=soup.find_all("a",href=re.compile("news"))
baseurl="http://www.yuncaijing.com"
news_lists=soup.find("ul",id="newslist")#找到这个
section_lists=news_lists.find("section",class_="nc-arc-wrap")
# print(section_lists.find("time").get_text())
span=section_lists.find("span")
data=span.find("a")
p=soup.find_all("div",class_="related-stock new-stock-list")
# print(p)
# url = 'http://example.webscraping.com/view/United-Kingdom-239'
# html = urllib2.urlopen(url).read()
# re.findall('<td class="w2p_fw">(.*?)</td>', html)
print((soup.find("a",text=re.compile("^开盘")))["title"])
