# swagger_client.GroupradioCfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_device_radio_config**](GroupradioCfgNorthboundApi.md#get_all_device_radio_config) | **GET** /controller/campus/v3/networkconfig/site/{siteId}/apradio/radios | 查询站点下所有AP设备射频配置信息
[**get_group_radio_config**](GroupradioCfgNorthboundApi.md#get_group_radio_config) | **GET** /controller/campus/v3/networkconfig/site/{siteId}/apradio | 查询AP站点射频配置信息
[**update_group_radio_config**](GroupradioCfgNorthboundApi.md#update_group_radio_config) | **PUT** /controller/campus/v3/networkconfig/site/{siteId}/apradio | 修改AP站点射频配置信息


# **get_all_device_radio_config**
> DeviceRadioConfigResponsesDto get_all_device_radio_config(site_id)

查询站点下所有AP设备射频配置信息

## 典型场景 ##  提供查询站点下所有AP设备射频配置信息接口。<br> ## 接口功能 ##  查询站点下所有AP设备射频信息。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.GroupradioCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点ID，UUID格式。

try: 
    # 查询站点下所有AP设备射频配置信息
    api_response = api_instance.get_all_device_radio_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupradioCfgNorthboundApi->get_all_device_radio_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 

### Return type

[**DeviceRadioConfigResponsesDto**](DeviceRadioConfigResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_radio_config**
> GroupRadioConfigResponsesDto get_group_radio_config(site_id)

查询AP站点射频配置信息

## 典型场景 ##  提供查询AP站点射频配置信息接口。<br> ## 接口功能 ##  查询AP站点射频配置信息。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>          

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.GroupradioCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点ID，UUID格式。

try: 
    # 查询AP站点射频配置信息
    api_response = api_instance.get_group_radio_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupradioCfgNorthboundApi->get_group_radio_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 

### Return type

[**GroupRadioConfigResponsesDto**](GroupRadioConfigResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_radio_config**
> GroupRadioConfigResponsesDto update_group_radio_config(site_id, group_radio_config_api_dto)

修改AP站点射频配置信息

## 典型场景 ##  提供修改AP射频配置信息接口。<br>  ## 接口功能 ##  修改AP站点射频配置信息。<br>  ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br>          

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.GroupradioCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点ID，UUID格式。
group_radio_config_api_dto = cloudcampus.GroupRadioConfigApiDto() # GroupRadioConfigApiDto | 修改AP站点射频配置入参。

try: 
    # 修改AP站点射频配置信息
    api_response = api_instance.update_group_radio_config(site_id, group_radio_config_api_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupradioCfgNorthboundApi->update_group_radio_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **group_radio_config_api_dto** | [**GroupRadioConfigApiDto**](GroupRadioConfigApiDto.md)| 修改AP站点射频配置入参。 | 

### Return type

[**GroupRadioConfigResponsesDto**](GroupRadioConfigResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

