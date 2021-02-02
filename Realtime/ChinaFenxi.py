#导入请求发送模块
import requests
#导入json转换模块
import json
#导入pyecharts中Map
from pyecharts import Line
#请求中国疫情数据链接
baseUrl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery34102606731362628003_1585466236231&_=1585466236232"
#请求当前链接返回的数据
chinaData=requests.get(baseUrl).text.replace('"{','{').replace('}"}','}}').replace('\\','')
#处理数据
chinaData=chinaData[chinaData.index("{"):-1]
#print(chinaData)
#将当前的json字符串转成Python的字典
baseData=json.loads(chinaData)

#保存疫情属性列表
attrList=["累计确诊","现有疑似","现有确诊","现有重症","境外输入"]

#日期列表
dateList=[]
#累计确诊列表
confirmList=[]
#现有疑似列表
suspectList=[]
#现有确诊列表
nowConfirmList=[]
#现有重症列表
nowSevereList=[]
#境外输入列表
importedCaseList=[]

#解析数据
for item in baseData["data"]["chinaDayList"]:
    #追加日期
    dateList.append(item["date"])
    #追加累计确诊列表
    confirmList.append(item["confirm"])
    #追加现有疑似列表
    suspectList.append(item["suspect"])
    #追加现有确诊列表
    nowConfirmList.append(item["nowConfirm"])
    #追加现有重症列表
    nowSevereList.append(item["nowSevere"])
    #追加境外输入列表
    importedCaseList.append(item["importedCase"])
#创建折线图
line=Line("全国疫情发展趋势图",width=1200,height=600)
#添加各国折线图
line.add("累计确诊",dateList,confirmList,mark_point=['max'])
line.add("现有疑似",dateList,suspectList,mark_point=['max'])
line.add("现有确诊",dateList,nowConfirmList,mark_point=['max'])
line.add("现有重症",dateList,nowSevereList,mark_point=['max'])
line.add("境外输入",dateList,importedCaseList,mark_point=['max'])
#显示图形参数
line.show_config()
line.render(path="output/全国疫情发展趋势图.html")
