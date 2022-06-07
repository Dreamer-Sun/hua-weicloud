# swagger_client.GetPoePowerStateApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_poe_power_state**](GetPoePowerStateApi.md#get_poe_power_state) | **GET** /controller/campus/v1/oamservice/poe/{deviceId} | 查询PoE电源状态


# **get_poe_power_state**
> GetPoePowerStateResp get_poe_power_state(device_id)

查询PoE电源状态

## 典型场景 ##    查询PoE电源状态。 ## 接口功能 ##    查询PoE电源状态。 ## 接口约束 ##    北向接口管理员可以访问。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.GetPoePowerStateApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID，UUID格式。

try: 
    # 查询PoE电源状态
    api_response = api_instance.get_poe_power_state(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPoePowerStateApi->get_poe_power_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**GetPoePowerStateResp**](GetPoePowerStateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

