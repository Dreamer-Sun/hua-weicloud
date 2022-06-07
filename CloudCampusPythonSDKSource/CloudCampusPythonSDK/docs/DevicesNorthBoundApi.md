# swagger_client.DevicesNorthBoundApi

All URIs are relative to *https://localhost/controller/campus/v1/indoormapservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_locaton_info**](DevicesNorthBoundApi.md#get_device_locaton_info) | **GET** /controller/campus/v1/indoormapservice/devices/{deviceId}/location-info | 查询楼层已布放设备位置信息


# **get_device_locaton_info**
> QueryDeviceLocationInfoResponse get_device_locaton_info(device_id)

查询楼层已布放设备位置信息

## 典型场景 ##  查询设备位置信息。 ## 接口功能 ##  查询设备位置信息，包含设备所在楼栋，楼层和布放坐标等。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DevicesNorthBoundApi()
device_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | 设备ID，格式UUID。

try: 
    # 查询楼层已布放设备位置信息
    api_response = api_instance.get_device_locaton_info(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesNorthBoundApi->get_device_locaton_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式UUID。 | 

### Return type

[**QueryDeviceLocationInfoResponse**](QueryDeviceLocationInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

