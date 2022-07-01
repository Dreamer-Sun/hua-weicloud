import json

from django.views.decorators.http import require_http_methods
from django.http.request import QueryDict
from tnmp.api.get_api import Get_Token
from tnmp.manage.querysites import GetSiteId
import requests
from django.http import JsonResponse
from tnmp.manage.getFakeData import CreateTopNdata, getFakeDeviceTags, getFakeHistoryflow

tenantName = 'c4_usr_034'
tenantPwd = '1qaz@WSX_034'
host = 'cn2.naas.huaweicloud.com'
port = '18002'

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}

body = {
    "siteId": '',
    "appDimension": '',
    "timeDimension": '',
    "top": 1,
}

body2 = {
    "siteId": '',
    "pageSize": 20,
    "pageIndex": 1
}

body3 = {
    "siteId": '',
    "tagId": '',
    "startTime": 1,
    "endTime": 1
}




def TrafficStatistic(siteId, appDimension, timeDimension, top):
    body["siteId"] = siteId
    body["appDimension"] = appDimension
    body["timeDimension"] = timeDimension
    body["top"] = int(top)
    # req = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/performanceservice/application/apptraffic/topapp',headers=headers, data=body)
    req = CreateTopNdata(int(top))
    print("TrafficStatistic:", req)
    data = req['data']
    # print(data)


    return data



# TopN应用流量
@require_http_methods(["POST"])
def trafficStatistic(request):
    print("here is trafficStatistic post", request)
    response = {}
    # 获取 json 类型数据:
    siteId = request.POST.get("siteId", '1')
    appDimension = request.POST.get("appDimension", '2')
    timeDimension = request.POST.get("timeDimension", '2')
    top = request.POST.get("top", 1)
    print(type(top))
    print(siteId, appDimension, timeDimension, top)
    data = TrafficStatistic(siteId, appDimension, timeDimension, top)
    try:
        response["data"] = data
        response["success"] = "success"
        response["fail"] = "fail"
        response["errcode"] = "errcode"
        response["errmsg"] = "errmsg"
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def QueryTag(siteId, pageSize, pageIndex):

    # req = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/performanceservice/endpointbehavior/tags',headers=headers, data=body2)
    Tags = getFakeDeviceTags()
    print("QueryTag", Tags)
    data = Tags.get("data", "")

    return data



@require_http_methods(["POST"])
def queryTag(request):
    print("here is queryTag post", request)
    response = {}
    # 获取 json 类型数据:
    siteId = request.POST.get("siteId", '1')
    pageSize = request.POST.get("pageSize", 1)
    pageIndex = request.POST.get("pageIndex", 2)
    data = QueryTag(siteId, pageSize, pageIndex)
    print(siteId, pageSize, pageIndex)
    try:
        response["data"] = data
        response["success"] = "success"
        response["fail"] = "fail"
        response["errcode"] = "errcode"
        response["errmsg"] = "errmsg"
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




# 调用函数查询历史接入客户流量

def QueryHistoryflow(siteId, tagId, selectTime):
    Time = selectTime.split(',')
    print("Time分割", Time)
    startTime = int(Time[0])
    endTime = int(Time[1])
    print("Time分割", Time[0], type(startTime))
    fakeHistoryFlowData = getFakeHistoryflow()["data"]
    # req = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/performanceservice/endpointbehavior/historyflow',headers=headers, data=body3)

    return fakeHistoryFlowData






@require_http_methods(["POST"])
def queryHistoryflow(request):
    print("here is queryHistoryflow post", request)
    response = {}
    # 获取 json 类型数据:
    siteId = request.POST.get("siteId", '1')
    tagId = request.POST.get("tagId", 1)
    selectTime = request.POST.get("selectTime", 2)
    data = QueryHistoryflow(siteId, tagId, selectTime)
    print(siteId, tagId, selectTime)
    print(type(selectTime))
    try:
        response["data"] = data
        response["success"] = "success"
        response["fail"] = "fail"
        response["errcode"] = "errcode"
        response["errmsg"] = "errmsg"
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)