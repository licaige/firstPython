#Python内置的访问数据库
import requests
#pyecharts图表库导入(Map地图，Line折线图，Bar柱形图)
from pyecharts import Map,Line,Bar
#将json导入
import json

#生成地图使用的数据--腾讯
mapUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34100282751706540052_1583633749228&_=1583633749229"

#发送请求获取数据--地图数据
mapData=requests.get(mapUrl).text.replace('"{','{').replace('}"})','}})').replace("\\","")
mapData=mapData[mapData.index("(")+1:-1]
#print(type(mapData))
#print(mapData)
#将处理完的数据转换成Python字典
tempMapData=json.loads(mapData)
#各个省份的数据：每个省份的数据也是一个字典对象
chain_provinces=tempMapData["data"]["areaTree"][0]["children"]
print(chain_provinces)
#保存省份名称列表
province_names=[]
#保存各个省份的确诊数据
province_data=[]
for province in chain_provinces:
    province_names.append(province["name"])
    province_data.append(province["total"]["confirm"])
map=Map("全国疫情分布图",width=1200,height=600)
#第一参数：标题#第二参数：省份列表（list）#第三参数：数据列表(list)#visual_range：左侧颜色柱范围
# #is_visualmap：是否显示颜色柱范围#visual_text_color：颜色柱初始颜色#is_label_show：文本颜色
map.add("",province_names,province_data,maptype='china',visual_range=[0,1000],
        is_visualmap=True,
        visual_text_color='#000',is_label_show=True)
#地图的配置参数
map.show_config()
#渲染地图
map.render(path="output/全国疫情分布图.html")






