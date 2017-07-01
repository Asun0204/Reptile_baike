#!/usr/bin/env python
# coding=utf-8
# Filename: url_manager.py
# Created by iFantastic on 2017/6/24
# Description: 管理URL集合


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """ 添加一个url到URL集合中
        :param url: 需要添加的url
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """ 添加一组url到URL集合中
        :param urls: 需要添加的一组url
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """ URL集合中是否还有未抓取过的url
        :return: 还有未抓取过的url就返回True，否则为False
        """
        return len(self.new_urls) != 0

    def get_new_url(self):
        """ 获取一个未抓取过的url
        :return: 一个url
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
