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

# 返回数据类型示例
# {
#     "errcode": "0",
#     "errmsg": "",
#     "success": [
#         {
#             "id": "b0a874e5-fc19-4743-8fd1-def2567ab026",
#             "name": "test11",
#             "description": "站点测试11",
#             "type": [
#                 "AP"
#             ],
#             "pattern": 1,
#             "latitude": "50",
#             "longtitude": "111",
#             "longitude": "111",
#             "contact": "shadougan",
#             "tag": [
#                 "aabb"
#             ],
#             "isolated": false,
#             "email": "tenant@huawei.com",
#             "phone": "123456789",
#             "postcode": "215000",
#             "address": "beijing road"
#         },
#         {
#             "id": "481ab649-9501-459e-8b99-d9ae5e7111cb",
#             "name": "test22",
#             "description": "站点测试22",
#             "type": [
#                 "AP"
#             ],
#             "pattern": 1,
#             "latitude": "50",
#             "longtitude": "111",
#             "longitude": "111",
#             "contact": "shadougan",
#             "tag": [
#                 "aabb"
#             ],
#             "isolated": false,
#             "email": "tenant@huawei.com",
#             "phone": "123456789",
#             "postcode": "215000",
#             "address": "beijing road"
#         }
#     ],
#     "fail": []
# }


sites = {
        "name": "test",
        "description": "站点测试1",
        "type": ["AP", "AR"],
        "pattern": 1,
        "latitude": "",
        "longtitude": "",
        "contact": "",
        "tag": [""],
        "isolated": False,
        "email": "",
        "phone": "",
        "postcode": "",
        "address": "",
        "cfgOriginId": "",
        "cfgOriginType": "",
        "cloneDevices": False
        }

All_Site = {
        "sites": []
}

def CreateSite(req_data):
        data = req_data["sites"]
        print("CreateSitedata", data)
        print(len(data))
        print(data[1])
        for i in range(len(data)):
                sites = data[i]
                # sites["name"] = data[i]["name"]
                # sites["description"] = data[i]["description"]
                # sites["type"] = data[i]["type"]
                # sites["pattern"] = data[i]["pattern"]
                # sites["latitude"] = data[i]["latitude"]
                # sites["longtitude"] = data[i]["longtitude"]
                # sites["contact"] = data[i]["contact"]
                # sites["tag"] = data[i]["tag"]
                # sites["isolated"] = data[i]["isolated"]
                # sites["email"] = data[i]["email"]
                # sites["phone"] = data[i]["phone"]
                # sites["postcode"] = data[i]["postcode"]
                # sites["address"] = data[i]["address"]
                # sites["cfgOriginId"] = data[i]["cfgOriginId"]
                # sites["cfgOriginType"] = data[i]["cfgOriginType"]
                # sites["cloneDevices"] = data[i]["cloneDevices"]

                All_Site["sites"].append(sites)


        print("ALL_SITE", All_Site)
        req = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                                    headers=headers, json=All_Site)
        res = req.json()
        success = res.get("success", "")
        fail = res.get("fail", "")
        errcode = res.get("errcode", "")
        errmsg = res.get("errmsg", "")
        print("CreateSite", res)
        All_Site["sites"] = []
        return success, fail, errcode, errmsg




@require_http_methods(["POST"])
def createsite(request):
        print("here is createsite post", request)
        response = {}
        tmp_data = "QuerySites()"
        # 获取 json 类型数据:
        a = request.POST
        print("a", a)
        json_bytes = request.body
        # json_bytes = request.query_params.get("nickname")
        print("-------")

        # 将 bytes 类型转为 str
        # json_str = json_bytes.decode()
        print(json_bytes)
        # python3.6 及以上版本中, json.loads() 方法可以接收 str 和 bytes 类型
        # 但是 python3.5 以及以下版本中, json.loads() 方法只能接收 str,
        # 3.5 需要有上面的编码步骤.
        #req_data = json.loads(json_str)
        # print("req_data", req_data)
        success, fail, errcode, errmsg = CreateSite("req_data")
        print(success)
        try:
                response['totalRecords'] = len(tmp_data)
                response["data"] = tmp_data
                response["success"] = success
                response["fail"] = fail
                response["errcode"] = errcode
                response["errmsg"] = errmsg
                response['code'] = 20000
        except Exception as e:
                response['msg'] = str(e)
                response['error_num'] = 1
        return JsonResponse(response)




