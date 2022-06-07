# swagger_client.ResetNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_device**](ResetNorthboundApi.md#reset_device) | **POST** /controller/campus/v1/oamservice/reset/device-configurations | 批量恢复设备出厂设置


# **reset_device**
> ResetDeviceResponse reset_device(request)

批量恢复设备出厂设置

## 典型场景 ## 批量恢复设备出厂设置。 ## 接口功能 ## 批量恢复设备出厂设置，设备恢复出厂设置后，会从站点中移除。 ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。该接口为同步接口，接口耗时与设备网络状态有关，超时时间为1分钟。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ResetNorthboundApi()
request = cloudcampus.ResetDeviceRequest() # ResetDeviceRequest | 批量恢复设备出厂设置请求。

try: 
    # 批量恢复设备出厂设置
    api_response = api_instance.reset_device(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResetNorthboundApi->reset_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ResetDeviceRequest**](ResetDeviceRequest.md)| 批量恢复设备出厂设置请求。 | 

### Return type

[**ResetDeviceResponse**](ResetDeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

