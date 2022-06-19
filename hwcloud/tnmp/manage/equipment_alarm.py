import json

from django.views.decorators.http import require_http_methods
from django.http.request import QueryDict
from tnmp.api.get_api import Get_Token
from tnmp.manage.querysites import GetSiteId
import requests

from django.http import JsonResponse

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}

body = {
    "siteId": "8d53e11c-2808-4319-8a0d-8e4d60c76e76",
    "deviceCategory": "ALL"
}

def getequipmentalarm(index):
    SiteList = GetSiteId()
    print("equipment_site", SiteList[index])
    body["siteId"] = SiteList[index]
    res = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/oamservice/device/alarm', headers=headers, json=body)
    data = res.json()["data"]
    print("equipment_data", data)


    # 设备告警信息  格式为站点id，站点所有设备
    #Alarm_message = []
    # temp tamp为中间变量
    temp = {}

    # print("站点总数", len(SiteList))
    # for i in range(len(SiteList)):
    #     body["siteId"] = SiteList[i]
    #     res = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/oamservice/device/alarm', headers=headers, json=body)
    #     temp["siteId"] = SiteList[i]
    #     temp["data"] = res.json()["data"]
    #     Alarm_message.append(temp)
    #     temp = {}
    #     # Alarm_message[i]["siteId"] = SiteList[i]
    #     # Alarm_message[i]["data"] = res.json()["data"]
    #
    # # print(SiteList)
    # print("Alarm_message", Alarm_message)
    # print("Alarm_message[0]", Alarm_message[0])
    # print("Alarm_message[40]", Alarm_message[40])
    # print(body)
    # print(res.json())
    return data





@require_http_methods(["POST"])
def getEquipmentAlarm(request):
    # 获取 json 类型数据:
    # json_bytes = request.body
    # print("json_bytes", type(json_bytes))
    # print("json_bytes", json_bytes)
    # # 将 bytes 类型转为 str
    # json_str = json_bytes.decode()
    # # python3.6 及以上版本中, json.loads() 方法可以接收 str 和 bytes 类型
    # #但是 python3.5 以及以下版本中, json.loads() 方法只能接收 str,
    # # 3.5 需要有上面的编码步骤.
    # req_data = json.loads(json_str)
    # id = req_data["id"]
    # print(type(id))
    id = request.GET.get('id')
    print(int(id))
    response = {}
    tmp_data = getequipmentalarm(int(id))
    test1 = {'deviceTotalCount': 1, 'normalDeviceCount': 1, 'warningDeviceCount': 1, 'faultyDeviceCount': 0, 'offlineDeviceCount': 0, 'unregistedDeviceCount': 0, 'alarmCriticalCount': 0, 'alarmMajorCount': 0, 'alarmMinorCount': 0, 'alarmWarningCount': 0}
    # test2 = {'deviceTotalCount': 2, 'normalDeviceCount': 2, 'warningDeviceCount': 2, 'faultyDeviceCount': 0, 'offlineDeviceCount': 0, 'unregistedDeviceCount': 0, 'alarmCriticalCount': 0, 'alarmMajorCount': 0, 'alarmMinorCount': 0, 'alarmWarningCount': 0}
    # if int(id) == 2:
    #     tmp_data = test1
    # elif int(id) == 2:
    #     tmp_data = test2

    try:
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)





@require_http_methods(["GET"])
def getSiteId(request):
    response = {}
    tmp_data = GetSiteId()
    # print(tmp_data)
    try:
        response['totalRecords'] = len(tmp_data)
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


if __name__=="__main__":
    getequipmentalarm(5)


