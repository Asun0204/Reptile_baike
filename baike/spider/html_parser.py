#!/usr/bin/env python
# coding=utf-8
# Filename: html_parser.py
# Created by iFantastic on 2017/6/24
# Description: 解析网页源码，获取URL和数据
import urlparse
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        """ 获取一个网页上的我们需要的url和数据
        :param page_url: 网页的url
        :param html_cont: 网页的源码
        :return: new_urls: 该网页上需要抓取的url
        :return new_data: 该网页上我们需要的内容数据
        """
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        return new_urls, new_data

    def __get_new_urls(self, page_url, soup):
        """ 抓取该网页上所需的链接url
        :param page_url: 网页的url
        :param soup: 网页的bs对象
        :return: 该网页上需要抓取的全部url
        """
        new_urls = set()
        # /item/Python
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def __get_new_data(self, page_url, soup):
        """ 获取该网页上我们需要的内容数据
        :param page_url: 该网页的url
        :param soup: 该网页的bs对象
        :return: 该网页上我们需要的内容数据
        """
        res_data = {'url': page_url}

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data