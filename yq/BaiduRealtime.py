from selenium import webdriver
from pyecharts import Map  # 地图

mobileEmulation={'deviceName':'iPhone X'}
options=webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',mobileEmulation)
#选择浏览器，可以是Firefox 、Ie 或Chrome，使用前需安装浏览器插件；
#driver是一个变量，可随便起
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3")
top=driver.find_element_by_class_name("VirusTable_1-1-209_MdE8uT").click()

flag=driver.find_element_by_class_name("VirusTable_1-1-209_38pQEh")
#获取所有省份
province=flag.find_elements_by_class_name("VirusTable_1-1-209_AcDK7v")
#获取确诊人数
quezhen=flag.find_elements_by_class_name("VirusTable_1-1-209_3x1sDV")
#获取治愈和死亡人数
other=flag.find_elements_by_class_name("VirusTable_1-1-209_EjGi8c")
zhiyu=[]
siwang=[]
for i in range(0,len(other)):
    if other[i].text=="-":
        if i % 2 == 0:
            zhiyu.append("0")
        else:
            siwang.append("0")
    else:
        if i % 2 == 0:
            zhiyu.append(other[i].text)
        else:
            siwang.append(other[i].text)

#写入数据到csv文件中
#currTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
# f = open("info/shishiyiqing.csv", "w+", encoding="utf_8_sig", newline="")
# writer = csv.writer(f)
# writer.writerow(['省市', '确诊', '治愈', '死亡'])
# for i in range(0,len(zhiyu)):
#     writer.writerow([province[i].text,quezhen[i].text,zhiyu[i],siwang[i]])
# # pandas读数据
# df = pd.read_csv(open("info/shishiyiqing.csv", encoding="utf_8_sig"))
provinces=[]
quezhens=[]
for i in range(0,len(quezhen)):
    if i%2!=0:
        quezhens.append(quezhen[i].text)
for i in range(0,len(zhiyu)):
    provinces.append(province[i].text)
    print(provinces[i]+"======"+quezhens[i]+"========="+zhiyu[i]+"======="+siwang[i])
map = Map(u'全国疫情分布图', width=1200, height=600)
map.add("", provinces, quezhens, maptype='china',visual_range=[0, 800],
        is_visualmap=True, visual_text_color='#000',is_label_show=True)
map.show_config()
map.render(path="output/map.html")
