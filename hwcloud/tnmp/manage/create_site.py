import json
import ast
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
        for i in range(len(data)):
                sites = data[i]
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
        print("errmsg", errmsg)
        All_Site["sites"] = []
        return success, fail, errcode, errmsg

# 获取创建成功站点数据格式化送入前端
def treeList(data):
        arr = []
        arr2 = {"label": "", "children": []}
        children = []
        children2 = {"label": ""}
        for i in range(len(data)):
                arr2["label"] = "SiteId:" + data[i]["id"]
                children2["label"] = "name:" + data[i]["name"]
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "description:" + data[i]["description"]
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "type:" + str(data[i]["type"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "pattern:" + str(data[i]["pattern"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "latitude:" + str(data[i]["latitude"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "longtitude:" + str(data[i]["longtitude"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "longitude:" + str(data[i]["longitude"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "contact:" + str(data[i]["contact"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "tag:" + str(data[i]["tag"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "isolated:" + str(data[i]["isolated"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "email:" + str(data[i]["email"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "phone:" + str(data[i]["phone"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "postcode:" + str(data[i]["postcode"])
                children.append(children2)
                children2 = {"label": ""}
                children2["label"] = "address:" + str(data[i]["address"])
                children.append(children2)
                children2 = {"label": ""}
                arr2["children"] = children
                arr.append(arr2)
        print("treeList", arr)
        return arr


def DataFix(list):
        print("-----here is DataFix-------")
        for i in range(len(list)):
                print("type(list[i][type])", type(list[i]["type"]))
                print(list[i]["type"])
                list[i]["type"] = eval(list[i]["type"])
                if list[i]["isolated"] == 'false':
                        list[i]["isolated"] = False
                else:
                        list[i]["isolated"] = True
                if list[i]["cloneDevices"] == 'false':
                        list[i]["cloneDevices"] = False
                else:
                        list[i]["cloneDevices"] = True
                list[i]["tag"] = eval(list[i]["tag"])
                print(type(list[i]["type"]))
        print("after_list", list)
        return list



@require_http_methods(["POST"])
def createsite(request):
        print("here is createsite post", request)
        response = {}
        # 获取 json 类型数据:
        a = request.POST.get("sites", '1')
        sites = json.loads(a)
        print("type(sites)", type(sites))
        print(sites)
        After_fix = DataFix(sites)
        # json_bytes = request.body
        print("-------")

        #req_data = json.loads(json_str)
        # print("req_data", req_data)
        data = {"sites": []}
        data["sites"] = After_fix
        success, fail, errcode, errmsg = CreateSite(data)
        print(success)
        success = treeList(success)
        try:
                response["success"] = success
                response["fail"] = fail
                response["errcode"] = errcode
                response["errmsg"] = errmsg
                response['code'] = 20000
        except Exception as e:
                response['msg'] = str(e)
                response['error_num'] = 1
        return JsonResponse(response)




