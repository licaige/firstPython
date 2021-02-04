#导入菜单模块
import MessageManager as mm
#导入sys模块
import sys
#实现菜单输出
def outputMainMenu():
    print("疫情实时数据管理系统")
    print("********************************************")
    print("1. 查看当前实时疫情信息")
    print("2. 新增疫情信息")
    print("3. 更新疫情信息")
    print("4. 查看目标城市疫情信息")
    print("5. 退   出")
    print("********************************************")
    number = int(input("请选择："))
    if number == 1:
        # 查看当前实时疫情信息
        print("************查看当前实时疫情信息*************")
        print("省份\t\t确诊\t\t治愈\t\t死亡")
        #调用查看当前实时疫情信息
        data=mm.showCurrentESMessage()
        for key in data:
            print(f"{key}\t\t", end="")
            for item in data[key]:
                print(f"{item}\t\t", end="")
            print("")
        print("********************************************")
    elif number == 2:
        # 新增疫情信息
        print("***************新增疫情信息*****************")
        province = input("请输入省份：")
        confirm = int(input("请输入累计确诊人数："))
        health = int(input("请输入治愈人数："))
        dead = int(input("请输入死亡人数:"))
        isOK=mm.addESMessage(province,confirm,health,dead)
        if isOK :
            print("添加成功！")
        else:
            print("添加失败, 当前省份已经存在！")
    elif number == 3:
        # 更新疫情信息
        print("***************更新疫情信息****************")
        province = input("请输入要更新的省份：")
        if mm.existsProvince(province):
            # 1. 初始化循环变量
            flag = "y"
            while flag == "y":
                num = int(input("请选择更新的具体信息：0. 确诊人数   1. 治愈人数   2. 死亡人数:"))
                if num == 0:
                    confirm = int(input("请输入确诊人数："))
                    if mm.updateESMessage(province,confirm=confirm):
                        print("更新成功！")
                    else:
                        print("更新失败！")
                elif num == 1:
                    health = int(input("请输入治愈人数："))
                    if mm.updateESMessage(province, health=health):
                        print("更新成功！")
                    else:
                        print("更新失败！")
                elif num == 2:
                    dead = int(input("请输入死亡人数："))
                    if mm.updateESMessage(province, dead=dead):
                        print("更新成功！")
                    else:
                        print("更新失败！")
                flag = input("是否继续？（y/n）:")
        else:
            print("当前输入的省份不存在， 请选择新增功能！")
        print("********************************************")
    elif number == 4:
        #查看目标省份的疫情信息
        print("** ** ** ** ** ** 查看目标省份疫情信息 ** ** ** ** ** ** *")
        answer="y"
        while answer=="y":
            province = input("请输入要查询的省份：")
            #执行查询功能
            provinceDict=mm.searchESMessageByProvince(province)
            if "湖北" in provinceDict:
                print(f"您输入的{province}不存在， 为您提供湖北实时数据")
                print("湖北", end="\t\t")
                for item in provinceDict["湖北"]:
                    print(item,end="\t\t")
            else:
                print(province,end="\t\t")
                for item in provinceDict[province]:
                    print(item, end="\t\t")
            answer=input("\n是否继续？（y / n）:")
    elif number == 5:
        print("谢谢使用")
        #退出程序
        sys.exit(1)

#返回上一级菜单
def returnMainMenu():
    # 1. 初始化循环变量
    answer = "0"
    while answer == "0":
        #在本部模块中调用函数--输出主菜单
        outputMainMenu()
        answer = input("输入0返回主菜单:")
    else:
        print("输入错误，程序终止！")