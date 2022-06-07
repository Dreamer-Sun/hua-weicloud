# swagger_client.LSWMgmtVlanNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](LSWMgmtVlanNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswmgmtvlan/devices/{deviceId}/mgmtvlan | 修改站点内交换机的管理VLAN配置
[**get_config**](LSWMgmtVlanNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/lswmgmtvlan/devices/{deviceId}/mgmtvlan | 获取站点内交换机的管理VLAN配置


# **config**
> MgmtVlanResponseDto config(device_id, body)

修改站点内交换机的管理VLAN配置

## 典型场景 ##    提供配置参数的接口，修改交换机的管理VLAN配置。 ## 接口功能 ##    修改交换机管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。<br>    如果当前交换机设备的上行口为Access类型，则直接将defaultVLAN设置为当前管理VLAN。<br>    如果当前交换机设备的上行口为Trunk类型，则用户配置管理VLAN前需要同时放行旧管理VLAN和新管理VLAN。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWMgmtVlanNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID，格式为uuid格式。
body = cloudcampus.MgmtVlanDto() # MgmtVlanDto | 站点内交换机的管理VLAN配置参数体。

try: 
    # 修改站点内交换机的管理VLAN配置
    api_response = api_instance.config(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWMgmtVlanNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式为uuid格式。 | 
 **body** | [**MgmtVlanDto**](MgmtVlanDto.md)| 站点内交换机的管理VLAN配置参数体。 | 

### Return type

[**MgmtVlanResponseDto**](MgmtVlanResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> MgmtVlanResponseDto get_config(device_id)

获取站点内交换机的管理VLAN配置

## 典型场景 ##    提供查询配置参数的接口，查询LSW的管理VLAN配置信息。 ## 接口功能 ##    获取管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWMgmtVlanNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。

try: 
    # 获取站点内交换机的管理VLAN配置
    api_response = api_instance.get_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWMgmtVlanNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 

### Return type

[**MgmtVlanResponseDto**](MgmtVlanResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

