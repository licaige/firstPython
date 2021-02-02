#Python内置的访问数据库
import requests
#pyecharts图表库导入(Map地图，Line折线图，Bar柱形图)
from pyecharts import Map,Line,Bar
#将json导入
import json

# 创建折线图
line = Line("海外各国疫情趋势图", "人数", width=1200, height=600)
#参与调查的国家列表
countryNames=["美国","意大利","西班牙","伊朗","法国","德国","韩国","日本本土","加拿大"]
urlTemplate="https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country={0}&"
for country in countryNames:
    url=urlTemplate.format(country)
    baseData=requests.get(url).text
    #print(country+"======================="+baseData)
    data=json.loads(baseData)
    datelist=[]
    confirmlist=[]
    for item in data["data"]:
        datelist.append(item["date"])
        confirmlist.append(item["confirm"])
    line.add(country, datelist, confirmlist, mark_point=['max'])
line.show_config()
line.render(path="./output/海外各国疫情趋势图.html")


