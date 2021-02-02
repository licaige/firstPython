# -*- coding: utf-8 -*-
import scrapy
import os
import urllib.request


class JishudaniuSpider(scrapy.Spider):
    #爬虫的名字
    name = 'jishudaniu'
    #allowed_domains = ['example.com']
    #爬虫爬取数据的起点
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        #保存服务器的地址
        host_name="https://pvp.qq.com/web201605/"
        #获取英雄详细页的地址(a标签) extract()表示提取数据
        hero_a_links=response.xpath('//div[@class="herolist-box"]/div[@class="herolist-content"]/ul/li/a')
        for link in hero_a_links:
            #提取英雄详细页地址
            href=link.xpath('./@href').extract()[0]
            detial_url=host_name+href
            #繁殖多个请求, 请求具体的英雄页
            yield scrapy.Request(detial_url,self.detial_parse)

    #详细英雄页数据处理函数
    def detial_parse(self, response):
        #从网页中提取英雄的名称和编号
        message=response.xpath('/html/body/script[10]/text()').extract()[0]
        #通过拆分字符串实现英雄名称和编号的获取
        heroName=message.split(",")[0].replace("'","").split(" = ")[1]
        heroNo=message.split(",")[1].replace("'","").replace(";","").split(" = ")[1].strip()
        #定义英雄皮肤链接地址模板
        heroSkinLinksTemplate=f"https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{heroNo}/{heroNo}-bigskin-"

        #指定英雄皮肤存放路径
        filePath="F:\\wzry\\"
        #判断路径是否存在
        if not os.path.exists(filePath+heroName):
            #创建文件夹
            os.makedirs(filePath+heroName)
        #提取当前英雄所有的皮肤名称
        skins=response.xpath('//div[@class="pic-pf"]/ul/@data-imgname').extract()[0]
        skin_list=skins.split("|")
        tempSkinList=[]
        for skin in skin_list:
            tempSkinList.append(skin.split("&")[0])
        #根据英雄皮肤的数量生成数字序列
        for index in range(0,len(tempSkinList)):
            #获取皮肤名称
            skinName=tempSkinList[index]
            #拼接皮肤链接地址
            fileName='{}{}{}{}'.format(filePath+heroName,os.sep,skinName,".jpg")
            #下载图片， 并保存本地
            urllib.request.urlretrieve(heroSkinLinksTemplate+"{0}.jpg".format(index+1),filename=fileName)




