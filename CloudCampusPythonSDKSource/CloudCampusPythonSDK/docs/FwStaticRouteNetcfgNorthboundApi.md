# swagger_client.FwStaticRouteNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_fw_static_route_config**](FwStaticRouteNetcfgNorthboundApi.md#create_device_fw_static_route_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/fwstaticroute/devices/{deviceId}/staticroute | 创建防火墙设备静态路由配置
[**delete_device_fw_static_route_config**](FwStaticRouteNetcfgNorthboundApi.md#delete_device_fw_static_route_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/fwstaticroute/devices/{deviceId}/staticroute/action/batch-delete | 删除防火墙设备静态路由配置
[**get_device_fw_static_route_config**](FwStaticRouteNetcfgNorthboundApi.md#get_device_fw_static_route_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/fwstaticroute/devices/{deviceId}/staticroute | 查询防火墙设备静态路由配置
[**update_device_fw_static_route_config**](FwStaticRouteNetcfgNorthboundApi.md#update_device_fw_static_route_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/fwstaticroute/devices/{deviceId}/staticroute | 修改防火墙设备静态路由配置


# **create_device_fw_static_route_config**
> FwStaticRouteResponseDto create_device_fw_static_route_config(device_id, device_fw_static_route_info_dto)

创建防火墙设备静态路由配置

## 典型场景 ##    提供创建防火墙设备静态路由配置的接口。 ## 接口功能 ##    创建防火墙设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwStaticRouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_fw_static_route_info_dto = cloudcampus.FwRouteInfo() # FwRouteInfo | 创建的防火墙设备静态路由配置。

try: 
    # 创建防火墙设备静态路由配置
    api_response = api_instance.create_device_fw_static_route_config(device_id, device_fw_static_route_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwStaticRouteNetcfgNorthboundApi->create_device_fw_static_route_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_fw_static_route_info_dto** | [**FwRouteInfo**](FwRouteInfo.md)| 创建的防火墙设备静态路由配置。 | 

### Return type

[**FwStaticRouteResponseDto**](FwStaticRouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_fw_static_route_config**
> FwStaticRouteDeleteResponseDto delete_device_fw_static_route_config(device_id, id)

删除防火墙设备静态路由配置

## 典型场景 ##    提供删除防火墙设备静态路由配置的接口。 ## 接口功能 ##    删除防火墙设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwStaticRouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
id = cloudcampus.FwStaticRouteDeleteDto() # FwStaticRouteDeleteDto | 要删除的防火墙设备静态路由配置ID列表。

try: 
    # 删除防火墙设备静态路由配置
    api_response = api_instance.delete_device_fw_static_route_config(device_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwStaticRouteNetcfgNorthboundApi->delete_device_fw_static_route_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **id** | [**FwStaticRouteDeleteDto**](FwStaticRouteDeleteDto.md)| 要删除的防火墙设备静态路由配置ID列表。 | 

### Return type

[**FwStaticRouteDeleteResponseDto**](FwStaticRouteDeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_fw_static_route_config**
> GetFwStaticRouteResponseDto get_device_fw_static_route_config(device_id, page_index, page_size)

查询防火墙设备静态路由配置

## 典型场景 ##    提供查询防火墙设备静态路由配置的接口。 ## 接口功能 ##    查询防火墙设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwStaticRouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
page_index = 1 # int | 页面索引。
page_size = 20 # int | 每页显示记录数。

try: 
    # 查询防火墙设备静态路由配置
    api_response = api_instance.get_device_fw_static_route_config(device_id, page_index, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwStaticRouteNetcfgNorthboundApi->get_device_fw_static_route_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **page_index** | **int**| 页面索引。 | 
 **page_size** | **int**| 每页显示记录数。 | 

### Return type

[**GetFwStaticRouteResponseDto**](GetFwStaticRouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_fw_static_route_config**
> FwStaticRouteResponseDto update_device_fw_static_route_config(device_id, device_fw_static_route_info_dto)

修改防火墙设备静态路由配置

## 典型场景 ##    提供修改防火墙设备静态路由配置的接口。 ## 接口功能 ##    修改防火墙设备静态路由配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwStaticRouteNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_fw_static_route_info_dto = cloudcampus.DeviceFwStaticRouteInfoDto() # DeviceFwStaticRouteInfoDto | 修改的防火墙设备静态路由配置。

try: 
    # 修改防火墙设备静态路由配置
    api_response = api_instance.update_device_fw_static_route_config(device_id, device_fw_static_route_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwStaticRouteNetcfgNorthboundApi->update_device_fw_static_route_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_fw_static_route_info_dto** | [**DeviceFwStaticRouteInfoDto**](DeviceFwStaticRouteInfoDto.md)| 修改的防火墙设备静态路由配置。 | 

### Return type

[**FwStaticRouteResponseDto**](FwStaticRouteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

