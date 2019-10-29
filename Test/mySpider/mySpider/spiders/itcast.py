# conding = utf - 8
import scrapy
from mySpider.mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬取范围
    allowd_domains = ["htto://www.baidu.com"]
    #爬虫起始url
    start_urls = [
        "http://www.baidu.com"
    ]

    def parse(self,response):
        teacher_list = response.xpath("//div[@class='li_txt']")
        #遍历节点集合
        for each in teacher_list:
            # Item对象用来保存数据
            item = MyspiderItem()
