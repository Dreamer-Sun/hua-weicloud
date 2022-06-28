



# 终端应用流量信息查询假数据
import random

topNdata = {
     "errcode": "0",
     "errmsg": "",
     "data": [
     ]
}
ApplicationList = ["抖音", "今日头条", "微信", "腾讯QQ", "抖音", "虎牙直播",
                   "斗鱼", "百度网盘", "钉钉", "淘宝", "京东", "高德地图",
                   "美团", "QQ浏览器", "哔哩哔哩", "爱奇艺", "携程旅行"]

ApplicationPercent = [20.5, 18.56, 17.43, 16.36, 15.43, 14.89, 13.62, 14.58, 13.49, 11.46, 10.64, 9.45, 8.43]
ApplicationTraffic = [602.2, 530.3, 450.5, 410.7, 370.4, 330.5, 299.6, 234.4, 200.8, 155.2, 131.5, 99.4, 65.9]
# 随机种子列表

def CreateTopNdata(num):
    topNdata["data"] = []
    arr = {}
    num1 = []
    num2 = []
    for i in range(num):
        a = random.randint(0, len(ApplicationList) - 1)
        b = random.randint(0, len(ApplicationPercent) - 1)
        # 防止随机数重复
        while True:
            if a in num1:
                a = random.randint(0, len(ApplicationList) - 1)
            else:
                num1.append(a)
                break
        while True:
            if b in num2:
                b = random.randint(0, len(ApplicationPercent) - 1)
            else:
                num2.append(b)
                break

        arr["name"] = ApplicationList[a]
        arr["percent"] = ApplicationPercent[b]
        arr["traffic"] = ApplicationTraffic[b]
        arr["unit"] = "MB"
        topNdata["data"].append(arr)
        arr = {}
    # print(topNdata)
    # print('')
    return topNdata



if __name__ == '__main__':
    data = CreateTopNdata(5)
    print(data)
