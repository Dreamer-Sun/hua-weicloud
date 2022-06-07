# swagger_client.FwNatNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_fw_nat_config**](FwNatNetcfgNorthboundApi.md#create_device_fw_nat_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/fwnat/devices/{deviceId}/fwnat | 创建防火墙设备NAT配置
[**delete_device_fw_nat_config**](FwNatNetcfgNorthboundApi.md#delete_device_fw_nat_config) | **POST** /controller/campus/v1/networkservice/networkconfig/net/fwnat/devices/{deviceId}/fwnat/action/batch-delete | 删除防火墙设备NAT配置
[**get_device_fw_nat_config**](FwNatNetcfgNorthboundApi.md#get_device_fw_nat_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/fwnat/devices/{deviceId}/fwnat | 查询防火墙设备NAT配置
[**update_device_fw_nat_config**](FwNatNetcfgNorthboundApi.md#update_device_fw_nat_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/fwnat/devices/{deviceId}/fwnat | 修改防火墙设备NAT配置


# **create_device_fw_nat_config**
> FwNatResponseDto create_device_fw_nat_config(device_id, device_fw_nat_info_dto)

创建防火墙设备NAT配置

## 典型场景 ##    提供创建防火墙设备NAT配置的接口。 ## 接口功能 ##    创建防火墙设备NAT配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwNatNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_fw_nat_info_dto = cloudcampus.DeviceFwNatInfoDto() # DeviceFwNatInfoDto | 创建的防火墙设备NAT配置。

try: 
    # 创建防火墙设备NAT配置
    api_response = api_instance.create_device_fw_nat_config(device_id, device_fw_nat_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwNatNetcfgNorthboundApi->create_device_fw_nat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_fw_nat_info_dto** | [**DeviceFwNatInfoDto**](DeviceFwNatInfoDto.md)| 创建的防火墙设备NAT配置。 | 

### Return type

[**FwNatResponseDto**](FwNatResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_fw_nat_config**
> FwNatDeleteResponseDto delete_device_fw_nat_config(device_id, id)

删除防火墙设备NAT配置

## 典型场景 ##    提供删除防火墙设备NAT配置的接口。 ## 接口功能 ##    删除防火墙设备NAT配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwNatNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
id = cloudcampus.FwNatDeleteDto() # FwNatDeleteDto | 要删除的防火墙设备NAT配置ID列表。

try: 
    # 删除防火墙设备NAT配置
    api_response = api_instance.delete_device_fw_nat_config(device_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwNatNetcfgNorthboundApi->delete_device_fw_nat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **id** | [**FwNatDeleteDto**](FwNatDeleteDto.md)| 要删除的防火墙设备NAT配置ID列表。 | 

### Return type

[**FwNatDeleteResponseDto**](FwNatDeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_fw_nat_config**
> GetFwNatResponseDto get_device_fw_nat_config(device_id, page_index=page_index, page_size=page_size)

查询防火墙设备NAT配置

## 典型场景 ##    提供查询防火墙设备NAT配置的接口。 ## 接口功能 ##    查询防火墙设备NAT配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwNatNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
page_index = 1 # int | 页面索引。 (optional)
page_size = 20 # int | 每页显示记录数。 (optional)

try: 
    # 查询防火墙设备NAT配置
    api_response = api_instance.get_device_fw_nat_config(device_id, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwNatNetcfgNorthboundApi->get_device_fw_nat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **page_index** | **int**| 页面索引。 | [optional] 
 **page_size** | **int**| 每页显示记录数。 | [optional] 

### Return type

[**GetFwNatResponseDto**](GetFwNatResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_fw_nat_config**
> FwNatResponseDto update_device_fw_nat_config(device_id, device_fw_nat_info_dto)

修改防火墙设备NAT配置

## 典型场景 ##    提供修改防火墙设备NAT配置的接口。 ## 接口功能 ##    修改防火墙设备NAT配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwNatNetcfgNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备标识，UUID格式。
device_fw_nat_info_dto = cloudcampus.DeviceFwNatInfoDto() # DeviceFwNatInfoDto | 修改的防火墙设备NAT配置。

try: 
    # 修改防火墙设备NAT配置
    api_response = api_instance.update_device_fw_nat_config(device_id, device_fw_nat_info_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwNatNetcfgNorthboundApi->update_device_fw_nat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备标识，UUID格式。 | 
 **device_fw_nat_info_dto** | [**DeviceFwNatInfoDto**](DeviceFwNatInfoDto.md)| 修改的防火墙设备NAT配置。 | 

### Return type

[**FwNatResponseDto**](FwNatResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

