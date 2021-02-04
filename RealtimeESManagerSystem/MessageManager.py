import RealtimeMessageData as rmd
#查看当前实时疫情信息
def showCurrentESMessage():
    #从腾讯新闻网站中使用爬虫实现疫情信息的抓取
    return rmd.ESData

#添加疫情信息
def addESMessage(province,confirm,health,dead):
    # 检查当前输入的省份在字典中是否存在
    if province not in rmd.ESData:
        rmd.ESData[province] = [confirm, health, dead]
        return True
    else:
        return False

#实现目标省份疫情信息查询功能
def searchESMessageByProvince(province="湖北"):
    #保存查询结果
    provinceDict={}
    #判断province参数是否存在
    if province not in rmd.ESData:
        provinceDict["湖北"]=rmd.ESData["湖北"]
    else:
        provinceDict[province] = rmd.ESData[province]
    #返回结果
    return provinceDict

#更新疫情信息
def updateESMessage(province,**dictData):
    #判断省份是否存在
    if province in rmd.ESData:
        for item in dictData:
            if item=="confirm":#更新确诊人数
                rmd.ESData[province][0]=dictData["confirm"]
            elif item=="health":#更新治愈人数
                rmd.ESData[province][1] = dictData["health"]
            elif item=="dead":#更死亡诊人数
                rmd.ESData[province][2] = dictData["dead"]
        #更新成功
        return True
    else:
        #更新失败
        return False


#判断省份是否存在
def existsProvince(province):
    if province in rmd.ESData:
        return True
    else:
        return False



