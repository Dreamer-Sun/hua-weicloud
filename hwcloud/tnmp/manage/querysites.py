
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

def GetSiteId():
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers)
    res_data = res.json()
    data = res_data.get('data')
    SiteIdList = []
    for i in range(len(data)):
        SiteIdList.append(data[i]["id"])

    # print(SiteIdList)
    return SiteIdList


def QuerySites():
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