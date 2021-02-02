#Python内置的访问数据库
import requests
#pyecharts图表库导入(Map地图，Line折线图，Bar柱形图)
from pyecharts import Map,Line,Bar
#将json导入
import json

import xlrd
#生成数据分析图表使用的数据--腾讯
baseUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=jQuery341003516239794227838_1585408020609&_=1585408020610"
#发送请求获取数据--数据分析数据
baseData=requests.get(baseUrl).text.replace('"{','{').replace('}"})','}})').replace("\\","")
baseData=baseData[baseData.index("(")+1:-1]
#print(baseData)
#将处理完的数据转换成Python字典
data=json.loads(baseData)
tempBaseData=data["data"]["foreignList"]

#打开Excel文件读取数据
data = xlrd.open_workbook('世界各国中英文对照表.xlsx')
#通过索引顺序获取
table = data.sheet_by_index(0)
#获取行数
nrows = table.nrows
#将国家名称定义成字典
countryDict={}
for i in range(nrows):
    countryDict[table.row_values(i)[1]]=table.row_values(i)[0]

#保存国家名称列表
country_names=[]
#保存各个国家的确诊数据
country_data=[]
for country in tempBaseData:
    if country["name"] in countryDict:
        country_names.append(countryDict[country["name"]])
        country_data.append(country["confirm"])

map=Map("世界疫情分布图",width=1200,height=600)
#第一参数：标题#第二参数：省份列表（list）#第三参数：数据列表(list)#visual_range：左侧颜色柱范围
# #is_visualmap：是否显示颜色柱范围#visual_text_color：颜色柱初始颜色#is_label_show：文本颜色
map.add("世界地图",country_names,country_data,maptype='world',visual_range=[0,10000],
        is_visualmap=True,
        visual_text_color='#000')
#地图的配置参数
map.show_config()
#渲染地图
map.render(path="output/世界疫情分布图.html")