
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


def QuerySites():
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/sites',
                       headers=headers)
    res_data = res.json()
    # data = res_data.get('totalRecords')

    # print(res_data)
    return res_data

@require_http_methods(["GET"])
def getSiteData(request):
    response = {}
    tmp_data = QuerySites()
    try:
        response['totalRecords'] = tmp_data.get('totalRecords')
        response["data"] = tmp_data.get('data')
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)