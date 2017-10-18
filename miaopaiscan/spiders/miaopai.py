# -*- coding: utf-8 -*-
import re
import scrapy
import json
from bs4 import BeautifulSoup
from scrapy.http import Request
from miaopaiscan.mysqlpipelines.sql import Sql
from miaopaiscan.items import MiaopaiscanItem


class MiaopaiSpider(scrapy.Spider):
    name = 'miaopaiscan'
    allowed_domains = ['www.miaopai.com']
    start_urls = ['http://www.miaopai.com/']



    def start_requests(self):
        startint=6000001
        endint=7000000
        startid = Sql.selectmaxid(self, startint, endint)['id']
        if  startid!=None:
            startint=startid
        maxLimit = Sql.select_count(self,startint,endint)
        maxLimit=maxLimit['count(*)']
        # maxLimit=100
        # print(maxLimit)
        for end in range(1,int(int(maxLimit)/50)+1):
            endLimit=end*50
            startLimit=(end-1)*50
            result=Sql.select_countLimit(self,startLimit,endLimit,startint,endint)
            for result1 in result:
                # print(result1['href'])
                yield Request(result1['href'], self.parse_user,meta={'suid':result1['suid']})

        # print(maxLimit)
        pass
    def parse_user(self,response):
        result=BeautifulSoup(response.text, 'lxml').find_all("div", class_="videoIntr")
        for resu in result:
            suid=response.meta['suid']
            item = MiaopaiscanItem()

            item['videohref']=resu.find("ul",class_="commentLike").find("a").get('href')

            lookstr=resu.find("span",class_="red").get_text()
            # pattern = re.compile(r'maxnum=\d+')
            item['look'] = re.sub("\D", "", lookstr)
            item['suid']=suid
            item['videoabout']=resu.find("div",class_="viedoAbout").get_text().strip()

            item['like']=resu.find("ul",class_="commentLike").find_all("a")[0].get_text()

            item['commen']=resu.find("ul",class_="commentLike").find_all("a")[1].get_text()

            item['date']=resu.find("p",class_="personalDataT").find_all("span")[0].get_text()
            yield item

        print('--------------')

        pass


