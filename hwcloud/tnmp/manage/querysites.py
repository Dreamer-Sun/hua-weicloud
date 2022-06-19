import ctypes
import sys
import threading
import time
from collections import Counter
import ctypes
import requests
from cloudcampus.api_client import ApiClient
from cloudcampus.apis.site_manager_api import SiteManagerApi
from cloudcampus.configuration import Configuration
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from geopy.geocoders import Nominatim
from tnmp.api.get_api import Get_Token

global isEnd
tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}


def QuerySites():
    """
    获取站点所有的数据
    :param
    :return 返回所有的站点数据
    """
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers)
    res_data = res.json()
    data = res_data.get('data')
    print(data[0]["id"])
    print(len(data))
    after_data = []
    child = {}
    num = 0
    children = {}
    children2 = []
    for i in range(len(data)):
        children2.append([])

    for i in range(len(data)):
        children["id"] = num
        num = num + 1
        children["label"] = "tenantId：" + str(data[i]["tenantId"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "name：" + str(data[i]["name"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "description：" + str(data[i]["description"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "type：" + str(data[i]["type"])
        children2[i].append(children)
        children["id"] = num
        children = {}
        num = num + 1
        children["label"] = "latitude：" + str(data[i]["latitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "longtitude：" + str(data[i]["longtitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "longitude：" + str(data[i]["longitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "contact：" + str(data[i]["contact"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "tag：" + str(data[i]["tag"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "isolated：" + str(data[i]["isolated"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "email：" + str(data[i]["email"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "phone：" + str(data[i]["phone"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "postcode：" + str(data[i]["postcode"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "address：" + str(data[i]["address"])
        children2[i].append(children)
        children = {}
    print(children2[0])

    for i in range(len(data)):
        child["id"] = num
        num = num + 1
        child["label"] = "设备id：" + data[i]["id"]
        child["children"] = children2[i]
        after_data.append(child)
        child = {}

    print("---------")
    # print(after_data)
    # 处理数据格式

    return after_data


@require_http_methods(["GET"])
def getSiteData(request):
    """
    前端接口请求数据
    获取站点所有的信息，返回到前端
    :param request:
    :return:
    """
    response = {}
    tmp_data = QuerySites()
    try:
        response['totalRecords'] = len(tmp_data)
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def QueryMapSites():
    """
    获取站点的数据
    :param
    :return 站点的经纬度，和颜色
    """
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers)
    res_data = res.json()
    tmp_data = res_data.get('data')
    data = []
    for i in tmp_data:
        xsite = i.get('latitude')
        ysite = i.get('longitude')
        # data.append({'value': [xsite, ysite], 'itemStyle': {'color': '#d26309'}})
        data.append({'value': [ysite, xsite], 'itemStyle': {'color': '#d26309'}})
    # print(data)
    return data


@require_http_methods(["GET"])
def getsitesmap(request):
    """
    前端接口
    获取站点的地图的经纬度数据
    :param request:
    :return:
    """
    response = {}
    tmp_data = QueryMapSites()
    try:
        response['points'] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


class MyThread(threading.Thread):
    """
    定义一个线程类
    """

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        # threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

    # def kill(self):
    #     ctypes.pythonapi.PyThreadState_SetAstncExc(
    #         ctypes.c_long(self.ident), ctypes.py_object(SystemExit)
    #     )

def check_contain_chinese(check_str):
    """
    判断函数 判断字符串是否是中文
    :param check_str:
    :return:
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        else:
            return False


def QuerySitesdData():
    """
    获取站点的数据
    :return: 返回站点的站点类型
    返回站点的位于各大洲的哪个位置
    """
    global isEnd
    isEnd = 0
    print("Now is Threading1")

    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers)
    res_data = res.json()
    tmp_data = res_data.get('data')
    data = []
    for i in tmp_data:
        # “纬度”【 Latitude】
        xsite = i.get('latitude')
        # “经度”【longitude】、
        ysite = i.get('longitude')
        type = i.get('type')
        # data.append({'value': [xsite, ysite], 'itemStyle': {'color': '#d26309'}})
        data.append({'value': [ysite, xsite], 'type': type})
    # print(data)
    # 根据经纬度判断站点在哪个国家
    # geolocator = Nominatim()
    countrydata = []
    geolocator = Nominatim(user_agent='BuyiXiao')
    for i in data:
        latitu = i.get('value')[0]
        longitu = i.get('value')[1]
        point = "%s, %s" % (longitu, latitu)
        # 位置坐标
        # print(point)
        # 假数据
        # point = ("38.9122, 121.602")
        location = geolocator.reverse(point)
        # 位置信息，识别的时间随着数据的增加而增加
        # print(location.address.split(',')[-1].replace(' ', ''))
        # 这是国家名称
        countryname = location.address.split(',')[-1].replace(' ', '')
        # 因为所有站点中中国居多，这里判断一下，如果是中国，那么再细化分省份，否则使用国家名称
        if countryname == '中国':
            # 是不是中文
            flag = check_contain_chinese(location.address.split(',')[-2].replace(' ', ''))
            # print(flag)
            if flag:
                countryname = location.address.split(',')[-2].replace(' ', '')
            else:
                countryname = location.address.split(',')[-3].replace(' ', '')
            # print(countryname)
        else:
            countryname = countryname
        countrydata.append(countryname)
        # print(len(location.address))
    # location = geolocator.reverse("38.9122, 121.602")
    # print((location.latitude, location.longitude))
    # print(location.raw)
    # 显示所有的国家名字列表
    # print(countrydata)
    tempcon = set(countrydata)
    xaxisdata = []
    histigramsitenum = []
    for i in tempcon:
        if countrydata.count(i) > 1:
            print("元素{}, 重复{}次".format(i, countrydata.count(i)))
            xaxisdata.append(i)
            histigramsitenum.append(countrydata.count(i))
            # q = {"%s" % i: countrydata.count(i)}
    print(xaxisdata)
    print(xaxisdata[0])
    q = {'xaxisdata': xaxisdata, 'sitenum': histigramsitenum}
    # q = {'xaxisdata': '河北省', '北京市', '天津市', 'histigramsitenum': 37, 51, 12}
    # print(q)
    typedata = []
    sitetype = []
    sitetypenum = []
    for i in data:
        typedata.append(str(i.get('type')).replace('[', '').replace(']', ''))
    # print(typedata)
    typeda = set(typedata)
    for i in typeda:
        if typedata.count(i) >= 1:
            print("元素{}, 重复{}次".format(i, typedata.count(i)))

            sitetype.append(i)
            sitetypenum.append(typedata.count(i))

    q.update({'sitetype': sitetype, 'sitetypenum': sitetypenum})
    print(q)
    isEnd = 1
    return q


def QueryResultByQuerySitesdData():
    """
    查询上面函数的结果
    :return:
    """
    global isEnd
    flag = False
    # flag = True
    print("Now is Threading2")
    while 1:
        if isEnd == 1:
            flag = True
            print("Thread is done")
            break
        else:
            print("Thread is running")
            time.sleep(8)
    return flag

# 创建两个线程
# for i in range(5):
#     locals()['t' + str(i)] = MyThread(func=QuerySitesdData)
#     locals()['t' + str(i + 1)] = MyThread(func=QueryResultByQuerySitesdData)
t1 = MyThread(func=QuerySitesdData)
t2 = MyThread(func=QueryResultByQuerySitesdData)

@require_http_methods(["GET"])
def queryresultbyquerysitesdata(request):
    """
    前端请求接口
    请求线程2，判断线程1是否执行完毕,如果1执行完毕，直接
    :param
    request:
    :return:
    """
    print(t1.get_result())
    print(t2.get_result())
    # while 1:
    #     time.sleep(5)
    #     print("t1 result", t1.get_result())
    #     print("t2 result", t2.get_result())
    #     if t2.get_result():
    #         break
    # t1.join()
    # t2.join()
    response = {}
    # tmp_data = QueryResultByQuerySitesdData()
    try:
        response['flag'] = t2.get_result()
        # response['flag'] = True
        response['data'] = t1.get_result()
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def querysitesdata(request):
    """
    前端请求接口
    是获取站点的位置和站点类型的
    :param
    request:
    :return:
    """
    # 开启线程
    t1.start()
    t2.start()
    response = {}
    # tmp_data = QuerySitesdData()
    try:
        response['data'] = "线程开启成功!"
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# if __name__ == '__main__':
#     isEnd = 0
#     t1 = MyThread(func=QuerySitesdData)
#     t2 = MyThread(func=QueryResultByQuerySitesdData)
#
#     t1.start()
#     t2.start()
#
#     while 1:
#         time.sleep(5)
#         print("t1 result", t1.get_result())
#         print("t2 result", t2.get_result())
#         if t2.get_result():
#             break
#     # t1.join()
#     # t2.join()
