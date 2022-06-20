import json

from django.views.decorators.http import require_http_methods
from django.http.request import QueryDict
from tnmp.api.get_api import Get_Token
from tnmp.manage.querysites import GetSiteId
import requests
from django.http import JsonResponse

from cloudcampus.api_client import ApiClient
from cloudcampus.apis.site_manager_api import SiteManagerApi
from cloudcampus.configuration import Configuration

tenantName = 'c4_usr_034'
tenantPwd = '1qaz@WSX_034'
host = 'cn2.naas.huaweicloud.com'
port = '18002'

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}

UpdateSiteId = {"name": "updateSite", "description": "", "latitude": "", "longtitude": "", "contact": "", "tag": ["abcd"], "isolated": False, "type": ["AR","AR"], "email": "", "phone":
 "", "postcode": "", "address": ""}


def DataFix(list):
    print("-----here is DataFix-------")

    list["type"] = eval(list["type"])
    if list["isolated"] == 'false':
        list["isolated"] = False
    else:
        list["isolated"] = True
    list["tag"] = eval(list["tag"])
    print("after_list", list)
    return list






def UpdateSite(siteId, body):

    body = json.dumps(body)
    print(body)

    req = requests.put(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites/{'+siteId+'}',
                        headers=headers, json=body)

    print("UpdateSite_req", req)
    res = req.json()
    print("UpdateSite", req)
    data = res.get("data", "")

    return data



@require_http_methods(["POST"])
def updateSite(request):
    print("here is updateSite post", request)
    response = {}
    # 获取 json 类型数据:
    a = request.POST.get("siteId", '1')
    b = request.POST.get("form", '2')
    siteId = json.loads(a)
    body = DataFix(json.loads(b))
    print("type(siteId)", type(siteId))
    print(siteId)
    print("type(body)", type(body))
    print(body)
    data = UpdateSite(siteId, body)
    # json_bytes = request.body
    print("-------")

    # req_data = json.loads(json_str)
    # print("req_data", req_data)
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


if __name__ == '__main__':
    UpdateSite('01ebf7bc-0e1d-452c-9b28-34f46a6f80ed', UpdateSiteId)
