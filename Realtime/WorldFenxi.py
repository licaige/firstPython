#导入请求发送模块
import requests
#导入json转换模块
import json
#导入pyecharts中Line
from pyecharts import Line

#创建折线图
line=Line("海外各国疫情发展趋势图",width=1200,height=600)
#参与统计数据的国家列表
countryNameList=["美国","意大利","西班牙","伊朗","法国","德国","韩国","日本本土","加拿大"]
#定义各个国家数据获取链接模板
urlTemplate="https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country={0}&"
#循环遍历各个国家获取数据
for country in countryNameList:
    #替换链接模板
    url=urlTemplate.format(country)
    #发送请求
    baseData=requests.get(url).text
    #print(country+"====================="+baseData)
    #将数据转换成Python中的字典
    data=json.loads(baseData)
    #保存日期列表
    dateList=[]
    #保存每日累计确诊人数
    confirmList=[]
    for item in data["data"]:
        #追加日期
        dateList.append(item["date"])
        #追加确诊人数
        confirmList.append(item["confirm"])
    #添加各国折线图
    line.add(country,dateList,confirmList,mark_point=['max'])
#显示图形参数
line.show_config()
line.render(path="output/海外各国疫情发展趋势图.html")
