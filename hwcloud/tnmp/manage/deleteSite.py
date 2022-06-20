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

deleteBody = {
    "ids": []
}

def DeleteSite(siteList):
    deleteBody["ids"] = siteList
    req = requests.delete(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                        headers=headers, json=deleteBody)
    res = req.json()
    print("DeleteSite", req)
    success = res.get("success", "")

    return success







@require_http_methods(["POST"])
def deleteSite(request):
    print("here is deleteSite post", request)
    response = {}
    # 获取 json 类型数据:
    a = request.POST.get("sites", '1')
    sites = json.loads(a)
    print("type(sites)", type(sites))
    print(sites)
    success = DeleteSite(sites)
    # json_bytes = request.body
    print("-------")

    # req_data = json.loads(json_str)
    # print("req_data", req_data)
    try:
        response["data"] = "here is DeleteSite"
        response["success"] = success
        response["fail"] = "fail"
        response["errcode"] = "errcode"
        response["errmsg"] = "errmsg"
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


