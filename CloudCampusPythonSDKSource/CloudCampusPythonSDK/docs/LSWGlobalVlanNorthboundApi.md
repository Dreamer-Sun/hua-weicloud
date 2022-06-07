# swagger_client.LSWGlobalVlanNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lsw_global_vlan_info**](LSWGlobalVlanNorthboundApi.md#create_lsw_global_vlan_info) | **POST** /controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan | 创建交换机的全局VLAN配置
[**delete_lsw_global_vlan_info**](LSWGlobalVlanNorthboundApi.md#delete_lsw_global_vlan_info) | **DELETE** /controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan/{recordId} | 删除交换机的全局VLAN配置
[**get_lsw_global_vlan_infos**](LSWGlobalVlanNorthboundApi.md#get_lsw_global_vlan_infos) | **GET** /controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan | 查询交换机的全局VLAN配置
[**update_lsw_global_vlan_info**](LSWGlobalVlanNorthboundApi.md#update_lsw_global_vlan_info) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswglobalvlan/devices/{deviceId}/globalvlan | 修改交换机的全局VLAN配置


# **create_lsw_global_vlan_info**
> LswGlobalVlanResponseDto create_lsw_global_vlan_info(device_id, body)

创建交换机的全局VLAN配置

## 典型场景 ##    提供配置参数的接口，创建交换机的全局VLAN配置。 ## 接口功能 ##    创建交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWGlobalVlanNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d515abcd' # str | 设备ID，格式为uuid格式。
body = cloudcampus.LswGlobalVlanDto() # LswGlobalVlanDto | 全局VLAN配置。

try: 
    # 创建交换机的全局VLAN配置
    api_response = api_instance.create_lsw_global_vlan_info(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWGlobalVlanNorthboundApi->create_lsw_global_vlan_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式为uuid格式。 | 
 **body** | [**LswGlobalVlanDto**](LswGlobalVlanDto.md)| 全局VLAN配置。 | 

### Return type

[**LswGlobalVlanResponseDto**](LswGlobalVlanResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lsw_global_vlan_info**
> LswGlobalVlanDelRespDto delete_lsw_global_vlan_info(device_id, record_id)

删除交换机的全局VLAN配置

## 典型场景 ##    提供配置参数的接口，删除交换机的全局VLAN配置。 ## 接口功能 ##    删除交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWGlobalVlanNorthboundApi()
device_id = 'ffce359c-cf08-4717-bc26-c6e6af8f0ec3' # str | 设备ID，格式为uuid格式。
record_id = '813a76d4-6eec-4264-ae45-a6f261482b60' # str | VLAN ID，UUID格式。

try: 
    # 删除交换机的全局VLAN配置
    api_response = api_instance.delete_lsw_global_vlan_info(device_id, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWGlobalVlanNorthboundApi->delete_lsw_global_vlan_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式为uuid格式。 | 
 **record_id** | **str**| VLAN ID，UUID格式。 | 

### Return type

[**LswGlobalVlanDelRespDto**](LswGlobalVlanDelRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lsw_global_vlan_infos**
> LswGlobalVlanAllRespDto get_lsw_global_vlan_infos(device_id)

查询交换机的全局VLAN配置

## 典型场景 ##    提供查询配置参数的接口，查询LSW的全局VLAN配置信息。 ## 接口功能 ##    查询全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWGlobalVlanNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID，格式为uuid格式

try: 
    # 查询交换机的全局VLAN配置
    api_response = api_instance.get_lsw_global_vlan_infos(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWGlobalVlanNorthboundApi->get_lsw_global_vlan_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式为uuid格式 | 

### Return type

[**LswGlobalVlanAllRespDto**](LswGlobalVlanAllRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lsw_global_vlan_info**
> LswGlobalVlanResponseDto update_lsw_global_vlan_info(device_id, body)

修改交换机的全局VLAN配置

## 典型场景 ##    提供配置参数的接口，修改交换机的全局VLAN配置。 ## 接口功能 ##    修改交换机全局VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWGlobalVlanNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID，格式为uuid格式。
body = cloudcampus.LswGlobalVlanUpdateDto() # LswGlobalVlanUpdateDto | 交换机的全局VLAN配置。

try: 
    # 修改交换机的全局VLAN配置
    api_response = api_instance.update_lsw_global_vlan_info(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWGlobalVlanNorthboundApi->update_lsw_global_vlan_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，格式为uuid格式。 | 
 **body** | [**LswGlobalVlanUpdateDto**](LswGlobalVlanUpdateDto.md)| 交换机的全局VLAN配置。 | 

### Return type

[**LswGlobalVlanResponseDto**](LswGlobalVlanResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

