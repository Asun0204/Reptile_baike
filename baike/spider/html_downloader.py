#!/usr/bin/env python
# coding=utf-8
# Filename: html_downloader.py
# Created by iFantastic on 2017/6/24
# Description: 下载网页源码
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        """ 下载网页的源码
        :param url: 需要下载的网页的url
        :return: 网页的源码
        """
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()