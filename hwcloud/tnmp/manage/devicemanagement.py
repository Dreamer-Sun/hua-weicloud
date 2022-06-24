# 设备管理
import json

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from tnmp.api.get_api import Get_Token

tokenid = Get_Token()

headers = {
    "X-ACCESS-TOKEN": tokenid
}


def GetDeviceInfo(pageIndex, pageSize):
    """
    获取所有设备信息
    :return:
    """
    para = {
        'pageIndex': pageIndex,
        'pageSize': pageSize
    }
    q = {}
    data = []
    res = requests.get(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/devices',
                       params=para,
                       headers=headers, )
    # print(res)
    tm_data = res.json().get('data')
    totalRecords = res.json().get('totalRecords')
    q.update({'totalRecords': totalRecords})
    q.update({'datainfo': tm_data})
    data.append(q)
    # print(data)
    return data


@require_http_methods(["GET"])
def getdeviceinfo(request):
    """
        前端接口请求数据
        获取站点所有的信息，返回到前端
        :param request:
        :return:
        """
    pageIndex = request.GET.get('pageIndex')
    pageSize = request.GET.get('pageSize')
    response = {}
    tmp_data = GetDeviceInfo(pageIndex=pageIndex, pageSize=pageSize)
    try:
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def CreateDevice(body_params):
    """
    创建设备
    :return:
    """
    body = body_params
    body_params = eval(body)
    # print("sssssssssssssssssssssssssbody_params", body_params, type(body_params))
    print(body_params.get('devices')[0])
    res = requests.post(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/devices',
                        json=body_params,
                        headers=headers, )
    tm_data = res.json()
    print(tm_data)
    return tm_data


@require_http_methods(["POST"])
def createdevice(request):
    """
        前端接口请求数据
        创建设备信息
        :param request:
        :return:
        """
    body_params = request.GET.get('data')
    # print("这里是body_params", body_params)
    response = {}
    tmp_data = CreateDevice(body_params=body_params)
    try:
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def DeleteDevice(data):
    body = data
    body_params = eval(body)
    # print("sssssssssssssssssssssssssbody_params", body_params, type(body_params))
    # print(body_params.get('devices')[0])
    res = requests.delete(url='https://cn2.naas.huaweicloud.com:18002/controller/campus/v3/devices',
                          json=body_params,
                          headers=headers, )
    tm_data = res.json()
    print(tm_data)
    return tm_data


@require_http_methods(["DELETE"])
def delete_device(request):
    """
    前端接口请求数据
    删除设备信息
    :param request:
    :return:
    """
    body_params = request.GET.get('data')
    # print("这里是body_params", body_params)
    response = {}
    tmp_data = DeleteDevice(body_params)
    try:
        response["data"] = tmp_data
        response['code'] = 20000
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
