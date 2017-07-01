#!/usr/bin/env python
# coding=utf-8
# Filename: spider_main.py
# Created by iFantastic on 2017/6/24
# Description: 爬虫主程序
import urllib2

from baike.spider import html_downloader
from baike.spider import url_manager
from baike.spider import html_parser
from baike.spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                print '第%d次:' % count, urllib2.unquote(new_url).encode('utf-8')

                if count == 30:
                    break

                count = count+1
            except Exception as e:
                print '第%d次:craw failed, %s' % (count, e)

        self.outputer.output_html()


if __name__ == '__main__':
    url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(url)