#!/usr/bin/env python
# coding=utf-8
# Filename: html_outputer.py
# Created by iFantastic on 2017/6/24
# Description: 收集所需数据和显示
import urllib2


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """用列表把数据收集起来
        :param data: 需要收集的数据
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """把数据存储到本地
        """
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<head><meta charset=utf-8></head>')
        fout.write('<body>')

        fout.write('<table>')

        fout.write('<tr>')

        fout.write('<td>url</td>')
        fout.write('<td>title</td>')
        fout.write('<td>summary</td>')

        fout.write('</tr>')

        # 默认编码模式ascii
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % urllib2.unquote(data['url'].encode('utf-8')))
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')

        fout.write('</body>')
        fout.write('</html>')

        fout.close()