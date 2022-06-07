# swagger_client.ApRadioConfigNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_radio_config**](ApRadioConfigNorthboundApi.md#get_device_radio_config) | **GET** /controller/campus/v3/networkconfig/device/{deviceId}/apradio/radios | 查询AP设备射频配置信息
[**update_device_radio_config**](ApRadioConfigNorthboundApi.md#update_device_radio_config) | **PUT** /controller/campus/v3/networkconfig/device/{deviceId}/apradio/radios | 修改AP设备射频配置信息


# **get_device_radio_config**
> ApDeviceRadioResponsesDto get_device_radio_config(device_id)

查询AP设备射频配置信息

## 典型场景 ##  提供查询AP设备射频配置信息接口。<br> ## 接口功能 ##  查询AP设备射频配置信息。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>        

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApRadioConfigNorthboundApi()
device_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 设备ID，UUID格式。

try: 
    # 查询AP设备射频配置信息
    api_response = api_instance.get_device_radio_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApRadioConfigNorthboundApi->get_device_radio_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**ApDeviceRadioResponsesDto**](ApDeviceRadioResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_radio_config**
> ApDeviceRadioResponsesDto update_device_radio_config(device_id, ap_device_radio_api_dto)

修改AP设备射频配置信息

## 典型场景 ##  提供修改AP设备射频配置信息接口。<br>  ## 接口功能 ##  修改AP设备射频配置信息。<br>  ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApRadioConfigNorthboundApi()
device_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 设备ID，UUID格式。
ap_device_radio_api_dto = cloudcampus.ApDeviceRadioApiDto() # ApDeviceRadioApiDto | 修改AP设备射频配置入参。

try: 
    # 修改AP设备射频配置信息
    api_response = api_instance.update_device_radio_config(device_id, ap_device_radio_api_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApRadioConfigNorthboundApi->update_device_radio_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 
 **ap_device_radio_api_dto** | [**ApDeviceRadioApiDto**](ApDeviceRadioApiDto.md)| 修改AP设备射频配置入参。 | 

### Return type

[**ApDeviceRadioResponsesDto**](ApDeviceRadioResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

