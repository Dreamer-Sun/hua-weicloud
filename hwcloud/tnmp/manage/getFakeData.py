# 终端应用流量信息查询假数据
import random
import calendar
import time

# topN应用流量假数据
import string

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


# 获取设备tagId假数据
fakeTags = {

    "errcode": "0.0",
    "errmsg": "",
    "pageIndex": 0,
    "pageSize": 0,
    "totalRecords": 0,
    "data": [
    ]
}

fakeTagNameList = ["huawei", "sanxing", "oppo", "xiaomi", "meizu", "tianyu", "yijiaqi", "jingli", "zhongxing", "vivo", "hello", "admin", "world", "iphone", "hongda", "lenovo", "Blackberry "]



# 获取查询历史接入客户流量假数据

targetName = ["REALTIME_HOUR_FLOW", "REALTIME_DAY_FLOW", "capture_rate", "passersby", "visitors", "connected",
              "within_one_hr", "one_hr_to_six_hrs", "more_than_six_hrs", "average_staytime", "first_time",
              "occasionally", "regularly", "frequently", "repeat_rate", "humanflow"]

fakeHistoryFlow = {
    "errcode": "0.0",
    "errmsg": "",
    "data": [
        {
            "targetName": "humanflow",
            "counts": [
                {
                    "count": "123.0",
                    "stamp": 0
                }
            ]
        }
    ]
}



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


def getRandomTagId():
    tagId = ''
    sample = '0123456789abcdefghijklmnopqrstuvwxyz'
    for i in range(8):
        char = random.choice(sample)#从sample中选择一个字符
        tagId = tagId + char
    tagId = tagId + '-'
    for i in range(4):
        char = random.choice(sample)#从sample中选择一个字符
        tagId = tagId + char
    tagId = tagId + '-'
    for i in range(4):
        char = random.choice(sample)#从sample中选择一个字符
        tagId = tagId + char
    tagId = tagId + '-'
    for i in range(4):
        char = random.choice(sample)#从sample中选择一个字符
        tagId = tagId + char
    tagId = tagId + '-'
    for i in range(12):
        char = random.choice(sample)#从sample中选择一个字符
        tagId = tagId + char
    return tagId


def getFakeDeviceTags():
    num1 = []
    num = random.randint(1, 10)
    print(num)
    tmp = {}
    fakeTags["data"] = []
    for i in range(num):
        a = random.randint(0, len(fakeTagNameList)-1)
        # 防止随机数相同
        while True:
            if a in num1:
                a = random.randint(0, len(fakeTagNameList) - 1)
            else:
                num1.append(a)
                break
        tmp["tagId"] = getRandomTagId()
        tmp["tagName"] = fakeTagNameList[a]
        fakeTags["data"].append(tmp)
        tmp = {}
    # print(fakeTags)
    return fakeTags



def getFakeHistoryflow():
    # 获取时间戳   *1000 代表毫秒为单位
    ts = calendar.timegm(time.gmtime())
    ts = ts * 1000
    fakeHistoryFlow["data"] = []

    # 构造data数据域
    for i in range(len(targetName)):
        tmp = {}
        count = {}
        tmp["targetName"] = targetName[i]
        tmp["counts"] = []
        count["count"] = random.randint(10, 500)
        count["stamp"] = ts
        tmp["counts"].append(count)
        fakeHistoryFlow["data"].append(tmp)

    return fakeHistoryFlow








if __name__ == '__main__':
    # data = CreateTopNdata(5)
    # print(data)
    # getFakeDeviceTags()
    getFakeHistoryflow()
