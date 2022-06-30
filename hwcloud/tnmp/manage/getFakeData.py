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


def Getnetworktraffic(num):
    """
    选取n个随机数据
    获取网络上行下行速率
    :return:
    """
    data = []
    citylist = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江",
                "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "重庆",
                "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆",
                "广东", "广西", "海南"
                ]
    cityname = random.sample(citylist, num)
    ratelist = []
    linklist = []
    value = 1
    for i in range(0, num):
        q = {}
        p = {}
        # print(cityname[i])
        q.update({'name': cityname[i]})
        p.update({'source': str(random.choice(["设备网络速率", "站点网络速率"]))})
        p.update({'target': cityname[i]})
        p.update({'value': round(value)})
        uplinkRate = random.randint(10000, 20000)
        downlinkRate = random.randint(20000, 50000)
        ratelist.append(q)
        linklist.append(p)
        value = (downlinkRate - uplinkRate) / 10000
    ratelist.append({'name': "设备网络速率"})
    ratelist.append({'name': "站点网络速率"})
    linklist.append(
        {
            'source': "设备网络速率",
            'arget': "站点网络速率",
            'value': 5
        })
    # print(ratelist)
    # print(linklist)
    tmp = {}
    tmp.update({"ratelist": ratelist})
    tmp.update({"linklist": linklist})
    data.append(tmp)
    return data

def getFakeDeviceTags():
    return 1

if __name__ == '__main__':
    # data = CreateTopNdata(5)
    # print(data)
    Getnetworktraffic(2)
