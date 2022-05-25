import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['cs.58.com']
    start_urls = ['http://cs.58.com/']

    def parse(self, response):
        # 字符串
        # content = response.text
        # print(content)
        # 二进制数据
        # content = response.body
        # print(content)
        # 获取长沙58热门岗位
        print('=======================')
        job_list = response.xpath("//div[@class='col4']//a").extract()

        print(job_list)

