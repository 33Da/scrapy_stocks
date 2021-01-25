# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyStockItem(scrapy.Item):
    # define the fields for your item here like:
    # 股票名称
    name = scrapy.Field()

    # 股票代码
    code = scrapy.Field()

    # 振幅
    amplitude = scrapy.Field()

    # 最新价
    new_price = scrapy.Field()

    # 市净率
    price_to_book_rate = scrapy.Field()

    # 昨收
    yesterday_price = scrapy.Field()

    # 量比
    volume_ratio = scrapy.Field()

    # 最高
    top = scrapy.Field()

    # 最低
    low = scrapy.Field()

    # 今日开
    today_price = scrapy.Field()

    # 涨跌幅
    up_and_down = scrapy.Field()

    # 净占比
    net_share = scrapy.Field()

    # 换手率
    turnover_rate = scrapy.Field()

    # 总市值
    total_market_value = scrapy.Field()

    # 爬取时间
    spider_time = scrapy.Field()

