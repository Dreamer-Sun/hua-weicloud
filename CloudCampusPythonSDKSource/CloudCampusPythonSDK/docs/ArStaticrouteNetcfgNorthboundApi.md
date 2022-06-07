# swagger_client.ArStaticrouteNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_ar_staticroute_config**](ArStaticrouteNetcfgNorthboundApi.md#create_device_ar_staticroute_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/arstaticroute/devices/{deviceId}/staticroute | 创建路由器设备静态路由配置
[**delete_device_ar_staticroute_config**](ArStaticrouteNetcfgNorthboundApi.md#delete_device_ar_staticroute_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/arstaticroute/devices/{deviceId}/staticroute/action/batch-delete | 删除路由器设备静态路由配置
[**get_device_ar_staticroute_config**](ArStaticrouteNetcfgNorthboundApi.md#get_device_ar_staticroute_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/arstaticroute/devices/{deviceId}/staticroute | 查询路由器设备静态路由配置
[**update_device_ar_staticroute_config**](ArStaticrouteNetcfgNorthboundApi.md#update_device_ar_staticroute_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/arstaticroute/devices/{deviceId}/staticroute | 修改路由器设备静态路由配置


# **create_device_ar_staticroute_config**
> ArStaticrouteResponseDto create_device_ar_staticroute_config(device_id, device_ar_staticroute_info_dto)

创建路由器设备静态路由配置

## 典型场景 ##    提供创建路由器设备静态路由配置的接口。 ## 接口功能 ##    创建路由器设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ArStaticrouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_ar_staticroute_info_dto = cloudcampus.RouteInfo() # RouteInfo | 创建的路由器设备静态路由配置。

try: 
    # 创建路由器设备静态路由配置
    api_response = api_instance.create_device_ar_staticroute_config(device_id, device_ar_staticroute_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArStaticrouteNetcfgNorthboundApi->create_device_ar_staticroute_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_ar_staticroute_info_dto** | [**RouteInfo**](RouteInfo.md)| 创建的路由器设备静态路由配置。 | 

### Return type

[**ArStaticrouteResponseDto**](ArStaticrouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_ar_staticroute_config**
> ArStaticrouteDeleteResponseDto delete_device_ar_staticroute_config(device_id, id)

删除路由器设备静态路由配置

## 典型场景 ##    提供删除路由器设备静态路由配置的接口。 ## 接口功能 ##    删除路由器设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ArStaticrouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
id = cloudcampus.ArStaticrouteDeleteDto() # ArStaticrouteDeleteDto | 要删除的路由器设备静态路由配置ID列表。

try: 
    # 删除路由器设备静态路由配置
    api_response = api_instance.delete_device_ar_staticroute_config(device_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArStaticrouteNetcfgNorthboundApi->delete_device_ar_staticroute_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **id** | [**ArStaticrouteDeleteDto**](ArStaticrouteDeleteDto.md)| 要删除的路由器设备静态路由配置ID列表。 | 

### Return type

[**ArStaticrouteDeleteResponseDto**](ArStaticrouteDeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_ar_staticroute_config**
> GetArStaticrouteResponseDto get_device_ar_staticroute_config(device_id, page_size, page_index=page_index)

查询路由器设备静态路由配置

## 典型场景 ##    提供查询路由器设备静态路由配置的接口。 ## 接口功能 ##    查询路由器设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ArStaticrouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
page_size = 20 # int | 每页显示记录数。
page_index = 1 # int | 页面索引。 (optional)

try: 
    # 查询路由器设备静态路由配置
    api_response = api_instance.get_device_ar_staticroute_config(device_id, page_size, page_index=page_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArStaticrouteNetcfgNorthboundApi->get_device_ar_staticroute_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **page_size** | **int**| 每页显示记录数。 | 
 **page_index** | **int**| 页面索引。 | [optional] 

### Return type

[**GetArStaticrouteResponseDto**](GetArStaticrouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_ar_staticroute_config**
> ArStaticrouteResponseDto update_device_ar_staticroute_config(device_id, device_ar_staticroute_info_dto)

修改路由器设备静态路由配置

## 典型场景 ##    提供修改路由器设备静态路由配置的接口。 ## 接口功能 ##    修改路由器设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ArStaticrouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_ar_staticroute_info_dto = cloudcampus.DeviceArStaticrouteInfoDto() # DeviceArStaticrouteInfoDto | 修改的路由器设备静态路由配置。

try: 
    # 修改路由器设备静态路由配置
    api_response = api_instance.update_device_ar_staticroute_config(device_id, device_ar_staticroute_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArStaticrouteNetcfgNorthboundApi->update_device_ar_staticroute_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_ar_staticroute_info_dto** | [**DeviceArStaticrouteInfoDto**](DeviceArStaticrouteInfoDto.md)| 修改的路由器设备静态路由配置。 | 

### Return type

[**ArStaticrouteResponseDto**](ArStaticrouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

