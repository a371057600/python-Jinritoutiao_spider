

from scrapy import signals
from selenium import webdriver
from lxml import etree

import time
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Work\python\chromedriver.exe")

    def process_request(self, request, spider):
        url = request.url
        time.sleep(2)
        url2 ='https://www.toutiao.com/ch/news_tech/'
        self.driver.get(url)
        if url == url2:
            try:
                # """ 模拟滚动到底部加载下一页，一共循环6次，每次等待4s，这个时间根据网速调整，如果你需要获取更多，那么把循环的范围加大就行了。
                # """
                for i in range(1, 4):
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    time.sleep(3)
            except:
                pass
        source = self.driver.page_source


        #对啊，我里面也可以爬，外面也可以爬，但是隔离了不知道怎么连贯起来了

        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')

        return response
