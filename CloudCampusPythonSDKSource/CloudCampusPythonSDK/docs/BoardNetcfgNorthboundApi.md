# swagger_client.BoardNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_board_config**](BoardNetcfgNorthboundApi.md#create_device_board_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/board/devices/{deviceId}/boards | 添加单板配置
[**delete_device_board_config**](BoardNetcfgNorthboundApi.md#delete_device_board_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/board/devices/{deviceId}/boards/action/batch-delete | 删除单板配置
[**get_device_board_config**](BoardNetcfgNorthboundApi.md#get_device_board_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/board/devices/{deviceId}/boards | 查询单板配置


# **create_device_board_config**
> ConfigResponseDto create_device_board_config(device_id, board_config_dto)

添加单板配置

## 典型场景 ##    提供配置单板参数的接口。 ## 接口功能 ##    配置交换机单板。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.BoardNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
board_config_dto = cloudcampus.BoardConfigDto() # BoardConfigDto | 单板配置信息。

try: 
    # 添加单板配置
    api_response = api_instance.create_device_board_config(device_id, board_config_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BoardNetcfgNorthboundApi->create_device_board_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **board_config_dto** | [**BoardConfigDto**](BoardConfigDto.md)| 单板配置信息。 | 

### Return type

[**ConfigResponseDto**](ConfigResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_board_config**
> BoardDeleteResponseDto delete_device_board_config(device_id, slot)

删除单板配置

## 典型场景 ## 提供删除单板配置的接口。 ## 接口功能 ## 删除站点内该交换机设备指定槽位的单板配置。 ## 接口约束 ## 只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.BoardNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
slot = cloudcampus.BoardDeleteDto() # BoardDeleteDto | 待删除的槽位单板。

try: 
    # 删除单板配置
    api_response = api_instance.delete_device_board_config(device_id, slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BoardNetcfgNorthboundApi->delete_device_board_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **slot** | [**BoardDeleteDto**](BoardDeleteDto.md)| 待删除的槽位单板。 | 

### Return type

[**BoardDeleteResponseDto**](BoardDeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_board_config**
> GetBoardResponseDto get_device_board_config(device_id)

查询单板配置

## 典型场景 ##    提供查询单板配置参数的接口。 ## 接口功能 ##    查询交换机单板配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.BoardNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。

try: 
    # 查询单板配置
    api_response = api_instance.get_device_board_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BoardNetcfgNorthboundApi->get_device_board_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 

### Return type

[**GetBoardResponseDto**](GetBoardResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

