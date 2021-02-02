#导入请求发送模块
import requests
#导入json转换模块
import json
#导入xlrd解析Excel表格
import xlrd
#导入pyecharts中Map
from pyecharts import Map
#请求海外各国疫情数据链接
baseUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=jQuery34102606731362628003_1585466236233&_=1585466236234"
#请求当前链接返回的数据
worldData=requests.get(baseUrl).text.replace('"{','{').replace('}"}','}}').replace('\\','')
#处理数据
worldData=worldData[worldData.index("{"):-1]
#将当前的json字符串转成Python的字典
baseData=json.loads(worldData)
#打开Excel文件读取数据
excelData=xlrd.open_workbook("世界各国中英文对照表.xlsx")
#通过索引顺序获取当前sheet表格
table=excelData.sheet_by_index(0)
#获取行数
rows=table.nrows
#创建国家中英文对照字典
countryDict={}
#循环获取中英文国家名称的键值对（字典）
for i in range(rows):
    countryDict[table.row_values(i)[1]]=table.row_values(i)[0]
#保存英文国家名称列表
englishCountryNameList=[]
#保存各个国家的确诊数据
countryConfirmDataList=[]
# 获取每个国家的名称和当前累计确诊人数
for country in baseData["data"]["foreignList"]:
    if country["name"] in countryDict:
        englishCountryNameList.append(countryDict[country["name"]])
        countryConfirmDataList.append(country["confirm"])
#创建地图
map=Map(title="世界疫情分布图",width=1200,height=600,title_color="red")
#添加世界地图相关参数
map.add("世界地图",englishCountryNameList,countryConfirmDataList,maptype="world",
        visual_range=[1,10000],visual_text_color="#000",is_visualmap=True)
#显示地图配置参数
map.show_config()
#渲染地图
map.render(path="output/世界疫情分布图.html")