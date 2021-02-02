#导入请求发送模块
import requests
#导入json转换模块
import json

#导入pyecharts中Map
from pyecharts import Map
#请求中国疫情数据链接
baseUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34102606731362628003_1585466236229&_=1585466236230"
#请求当前链接返回的数据
chinaData=requests.get(baseUrl).text.replace('"{','{').replace('}"}','}}').replace('\\','')
#处理数据
chinaData=chinaData[chinaData.index("{"):-1]
#print(chinaData)
#将当前的json字符串转成Python的字典
baseData=json.loads(chinaData)


#保存省份名称
provinceNameList=[]
#保存各省份确诊人数
provinceConfirmList=[]
#从数据中提取各个省份的疫情信息
provinceList=baseData["data"]["areaTree"][0]["children"]
for province in provinceList:
    provinceNameList.append(province["name"])
    provinceConfirmList.append(province["total"]["confirm"])

#创建地图
map=Map(title="全国疫情分布图",width=1200,height=600,title_color="red")
#添加中国地图相关参数
map.add("中国地图",provinceNameList,provinceConfirmList,maptype="china",
        visual_range=[1,1000],visual_text_color="#000",is_visualmap=True)
#显示地图配置参数
map.show_config()
#渲染地图
map.render(path="output/全国疫情分布图.html")

