import requests
import sys
from django.http import HttpResponse, JsonResponse
from cloudcampus.api_client import ApiClient
from cloudcampus.apis.radius_template_northbound_api import RadiusTemplateNorthboundApi
from cloudcampus.configuration import Configuration
from django.views.decorators.http import require_http_methods

information = {
    "userName": "c4_usr_034",
    "password": "1qaz@WSX_034"
}


def testapi():
    tenantName = 'c4_usr_034'
    tenantPwd = '1qaz@WSX_034'
    host = 'cn2.naas.huaweicloud.com'
    port = '18002'
    config = Configuration(host, port, tenantName, tenantPwd)
    api_client = ApiClient(config)
    api = RadiusTemplateNorthboundApi(api_client)
    pageIndex = 1
    pageSize = 100
    model = api.get_radius_template(page_index=pageIndex, page_size=pageSize)
    print(model)


def Get_Token():
    res = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/v2/tokens',
                        json=information)
    # print(HttpResponse)
    # print(res.json())
    res_data = res.json()
    # print(res_data)
    tokenid = res_data.get('data').get('token_id')
    print(tokenid)
    return tokenid

@require_http_methods(["GET"])
def show_token(request):
    response = {}
    tokeninfo = Get_Token()
    try:
        response['token'] = tokeninfo
        response['code'] = 20000
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
