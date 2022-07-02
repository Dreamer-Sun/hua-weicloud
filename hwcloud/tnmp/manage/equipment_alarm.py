import json

from django.views.decorators.http import require_http_methods
from django.http.request import QueryDict
from tnmp.api.get_api import Get_Token
from tnmp.manage.querysites import GetSiteId
import requests

from django.http import JsonResponse

from tnmp.manage.getFakeData import getFakePic_1_data, getFakePic_2_data, getFakePic_3_data, getFakePic_4_data

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}

body = {
    "siteId": "8d53e11c-2808-4319-8a0d-8e4d60c76e76",
    "deviceCategory": "ALL"
}

def getequipmentalarm(siteId, deviceCategory):
    # print("equipment_site", SiteList[index])
    body["siteId"] = siteId
    body["deviceCategory"] = deviceCategory
    res = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v1/oamservice/device/alarm', headers=headers, json=body)
    data = res.json()["data"]
    print("body", body)
    print("equipment_data", data)

    req_data = []
    req_data.append(data["deviceTotalCount"])
    req_data.append(data["normalDeviceCount"])
    req_data.append(data["warningDeviceCount"])
    req_data.append(data["faultyDeviceCount"])
    req_data.append(data["offlineDeviceCount"])
    req_data.append(data["unregistedDeviceCount"])
    req_data.append(data["alarmCriticalCount"])
    req_data.append(data["alarmMajorCount"])
    req_data.append(data["alarmMinorCount"])
    req_data.append(data["alarmWarningCount"])

    for i in range(len(req_data)):
        req_data[i] = req_data[i] + 1
    print(req_data)

    # 设备告警信息  格式为站点id，站点所有设备
    #Alarm_message = []
    # temp tamp为中间变量


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
    return req_data





@require_http_methods(["POST"])
def getEquipmentAlarm(request):


    # print(id)
    # print(int(id))
    response = {}
    siteId = request.POST.get("siteId", '1')
    deviceCategory = request.POST.get("deviceCategory", '1')
    print("here getEquipmentAlarm", siteId, deviceCategory)
    picture_1_data = getFakePic_1_data()
    picture_2_data = getFakePic_2_data()
    picture_3_date, picture_3_data = getFakePic_3_data()
    picture_4_data_1, picture_4_data_2 = getFakePic_4_data()
    # if(isUpdate == "true" ):
    # now_device = getequipmentalarm(siteId, deviceCategory)


    try:
        response["data"] = "tmp_data"
        response["now_device"] = "now_device"
        response["picture_1_data"] = picture_1_data
        response["picture_2_data"] = picture_2_data
        response["picture_3_date"] = picture_3_date
        response["picture_3_data"] = picture_3_data
        response["picture_4_data_1"] = picture_4_data_1
        response["picture_4_data_2"] = picture_4_data_2
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




@require_http_methods(["POST"])
def getEquipmentAlarm2(request):


    # print(id)
    # print(int(id))
    response = {}
    siteId = request.POST.get("siteId", '1')
    deviceCategory = request.POST.get("deviceCategory", '1')
    now_device = getequipmentalarm(siteId, deviceCategory)
    try:
        response["data"] = "tmp_data"
        response["now_device"] = now_device
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


