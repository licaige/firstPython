#Python内置的访问数据库
import requests
#pyecharts图表库导入(Map地图，Line折线图，Bar柱形图)
from pyecharts import Map,Line,Bar
#将json导入
import json
#导入pandas
import pandas as pd
#生成数据分析图表使用的数据--腾讯
baseUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery34100282751706540052_1583633749230&_=1583633749231"
#发送请求获取数据--数据分析数据
baseData=requests.get(baseUrl).text.replace('"{','{').replace('}"})','}})').replace("\\","")
baseData=baseData[baseData.index("(")+1:-1]
print(type(baseData))
#将处理完的数据转换成Python字典
data=json.loads(baseData)
#初始化pandas
chinaDayColumnList=["date","confirm","suspect","dead","heal","nowConfirm","nowSevere"]#列
chinaDaySeriesList=[]#多行
#提取中国从疫情开始每一疫情具体数据
tempBaseData=data["data"]["chinaDayList"]
#遍历每天具体数据编程pandas
for item in tempBaseData:
    line=[item["date"],item["confirm"],item["suspect"],item["dead"],
          item["heal"],item["nowConfirm"],item["nowSevere"]]
    #创建pandas中的行
    series=pd.Series(line,chinaDayColumnList)
    chinaDaySeriesList.append(series)
#创建表格
chainDayDateFrame=pd.DataFrame(chinaDaySeriesList)
print(chainDayDateFrame)

#生成全国实时疫情趋势图
#创建折线图
line=Line("全国实时疫情趋势图","人数",width=1200,height=600)
#从表格中拿到所以日期
dateAttr=list(chainDayDateFrame.loc[chainDayDateFrame.index,"date"])
confirm=list(chainDayDateFrame.loc[chainDayDateFrame.index,"confirm"])
suspect=list(chainDayDateFrame.loc[chainDayDateFrame.index,"suspect"])
nowConfirm=list(chainDayDateFrame.loc[chainDayDateFrame.index,"nowConfirm"])
nowSevere=list(chainDayDateFrame.loc[chainDayDateFrame.index,"nowSevere"])
line.add("累计确诊",dateAttr,confirm,mark_point=['max'])
line.add("现有疑似",dateAttr,suspect,mark_point=['max'])
line.add("现有确诊",dateAttr,nowConfirm,mark_point=['max'])
line.add("现有重症",dateAttr,nowSevere,mark_point=['max'])
line.show_config()
line.render(path="./output/全国实时疫情趋势图.html")



