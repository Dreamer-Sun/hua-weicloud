
import sys

import requests
from cloudcampus.api_client import ApiClient
from cloudcampus.apis.site_manager_api import SiteManagerApi
from cloudcampus.configuration import Configuration
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from tnmp.api.get_api import Get_Token

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}
params = {
        "pageIndex": 1,
        "pageSize": 100
          }
def GetSiteId():
    SiteIdList = []
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers,)
    total = res.json().get('totalRecords')
    num = int((int(total) / 100)) + 1
    for i in range(num):
        params["pageIndex"] = i + 1
        res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                           headers=headers,
                           params=params)
        res_data = res.json()
        data = res_data.get('data')
        for j in range(len(data)):
            SiteIdList.append(data[j]["id"])


    print(len(SiteIdList))
    print(SiteIdList)
    return SiteIdList


def QuerySites():
    SiteDataList = []
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers,)
    total = res.json().get('totalRecords')
    num = int((int(total) / 100)) + 1
    for i in range(num):
        params["pageIndex"] = i + 1
        res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                           headers=headers,
                           params=params)
        res_data = res.json()
        data = res_data.get('data')
        # print("data", data)
        for j in range(len(data)):
            SiteDataList.append(data[j])

    print("len(SiteDataList)", len(SiteDataList))

    after_data = []
    child = {}
    num = 0
    children = {}
    children2 = []
    for i in range(len(SiteDataList)):
        children2.append([])

    for i in range(len(SiteDataList)):
        children["id"] = num
        num = num + 1
        children["label"] = "tenantId：" + str(SiteDataList[i]["tenantId"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "name：" + str(SiteDataList[i]["name"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "description：" + str(SiteDataList[i]["description"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "type：" + str(SiteDataList[i]["type"])
        children2[i].append(children)
        children["id"] = num
        children = {}
        num = num + 1
        children["label"] = "latitude：" + str(SiteDataList[i]["latitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "longtitude：" + str(SiteDataList[i]["longtitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "longitude：" + str(SiteDataList[i]["longitude"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "contact：" + str(SiteDataList[i]["contact"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "tag：" + str(SiteDataList[i]["tag"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "isolated：" + str(SiteDataList[i]["isolated"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "email：" + str(SiteDataList[i]["email"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "phone：" + str(SiteDataList[i]["phone"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "postcode：" + str(SiteDataList[i]["postcode"])
        children2[i].append(children)
        children = {}
        children["id"] = num
        num = num + 1
        children["label"] = "address：" + str(SiteDataList[i]["address"])
        children2[i].append(children)
        children = {}
    print(children2[0])

    for i in range(len(SiteDataList)):
        child["id"] = num
        num = num + 1
        child["label"] = "设备id：" + SiteDataList[i]["id"]
        child["children"] = children2[i]
        after_data.append(child)
        child = {}

    print("---------")
    # print(after_data)
    # 处理数据格式



    return after_data

@require_http_methods(["GET"])
def getSiteData(request):
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


if __name__ == '__main__':
    # QuerySites()
    GetSiteId()
    # testapi()