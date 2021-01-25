# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo

class ScrapyStockPipeline:
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = "127.0.0.1"
        port = 27017
        dbname = "stock"

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host, port=port)

        # 指向指定的数据库
        self.mdb = client[dbname]

        self.post = self.mdb["stocks"]

    def process_item(self, item, spider):

        data = dict(item)
        # 向指定的表里添加数据
        self.post.insert(data)
        return item





