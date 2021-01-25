# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import *
import time

class StocksSpider(scrapy.Spider):
    name = "stocks"

    page_num = 1
    url = 'http://4.push2.eastmoney.com/api/qt/clist/get?pn={0}&pz=100&po=1&np=1&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f20,f8,f184,f62,f3,f17,f16,f15,f10,f18,f23,f2,f7,f12,f14'
    start_urls = [url.format(page_num)]

    def parse(self, response):
        data = json.loads(response.text)


        data = data["data"]

        # 总条数
        total = data["total"]

        # 总页数
        if total%100 != 0:
            page_sum = int(total/100 + 1)
        else:
            page_sum = int(total /100)


        stocks = data["diff"]

        for stock in stocks:
            item = ScrapyStockItem()

            item["name"] = stock["f14"]
            item["code"] = stock["f12"]
            item["amplitude"] = stock["f7"]
            item["new_price"] = stock["f2"]
            item["price_to_book_rate"] = stock["f23"]
            item["yesterday_price"] = stock["f18"]
            item["volume_ratio"] = stock["f10"]
            item["top"] = stock["f15"]
            item["low"] = stock["f16"]
            item["today_price"] = stock["f17"]
            item["up_and_down"] = stock["f3"]
            item["net_share"] = stock["f184"]
            item["turnover_rate"] = stock["f8"]
            item["total_market_value"] = stock["f20"]


            # 当前时间
            item["spider_time"] = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())

            yield item

        if self.page_num < page_sum:
            self.page_num += 1
            yield scrapy.Request(self.url.format(self.page_num),callback=self.parse)










