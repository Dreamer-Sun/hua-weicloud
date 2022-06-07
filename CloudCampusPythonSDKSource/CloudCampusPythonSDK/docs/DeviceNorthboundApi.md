# swagger_client.DeviceNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_modify_devices**](DeviceNorthboundApi.md#batch_modify_devices) | **PUT** /controller/campus/v3/devices | 批量修改设备
[**create_devices**](DeviceNorthboundApi.md#create_devices) | **POST** /controller/campus/v3/devices | 创建设备
[**delete_devices**](DeviceNorthboundApi.md#delete_devices) | **DELETE** /controller/campus/v3/devices | 删除设备
[**get_device_models**](DeviceNorthboundApi.md#get_device_models) | **GET** /controller/campus/v3/device-models | 查询设备款型
[**get_site_device**](DeviceNorthboundApi.md#get_site_device) | **GET** /controller/campus/v3/devices | 查询设备
[**modify_devices**](DeviceNorthboundApi.md#modify_devices) | **PUT** /controller/campus/v3/devices/{deviceId} | 修改设备
[**replace_device**](DeviceNorthboundApi.md#replace_device) | **POST** /controller/campus/v3/devices/replace | 替换设备
[**replace_original_device**](DeviceNorthboundApi.md#replace_original_device) | **POST** /controller/campus/v3/devices/replacement | 替换设备款型


# **batch_modify_devices**
> BatchModifyDeviceBean batch_modify_devices(batch_modify_device_dto)

批量修改设备

## 典型场景 ## 批量修改设备的名称、站点等信息。 ## 接口功能 ##   批量修改设备。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
batch_modify_device_dto = cloudcampus.BatchModifyDeviceDto() # BatchModifyDeviceDto | 批量修改设备入参模型。

try: 
    # 批量修改设备
    api_response = api_instance.batch_modify_devices(batch_modify_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->batch_modify_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_modify_device_dto** | [**BatchModifyDeviceDto**](BatchModifyDeviceDto.md)| 批量修改设备入参模型。 | 

### Return type

[**BatchModifyDeviceBean**](BatchModifyDeviceBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_devices**
> CreateDeviceBean create_devices(create_device_dto)

创建设备

## 典型场景 ##  根据设备ESN、设备名称、设备描述、站点ID等进行设备创建。 ## 接口功能 ##  创建设备。 ## 接口约束 ##  该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
create_device_dto = cloudcampus.CreateDeviceDto() # CreateDeviceDto | 创建设备入参信息。

try: 
    # 创建设备
    api_response = api_instance.create_devices(create_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->create_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_device_dto** | [**CreateDeviceDto**](CreateDeviceDto.md)| 创建设备入参信息。 | 

### Return type

[**CreateDeviceBean**](CreateDeviceBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_devices**
> DeleteDeviceBean delete_devices(device_ids)

删除设备

## 典型场景 ##  根据设备ID删除设备。 ## 接口功能 ##  删除设备。 ## 接口约束 ##  该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
device_ids = cloudcampus.DeleteDeviceDto() # DeleteDeviceDto | 设备ID列表。

try: 
    # 删除设备
    api_response = api_instance.delete_devices(device_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->delete_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**DeleteDeviceDto**](DeleteDeviceDto.md)| 设备ID列表。 | 

### Return type

[**DeleteDeviceBean**](DeleteDeviceBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_models**
> DeviceModelEntityList get_device_models()

查询设备款型

## 典型场景 ## 在控制器上查询设备款型信息时使用。 ## 接口功能 ## 查询设备款型信息。 ## 接口约束 ## 该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()

try: 
    # 查询设备款型
    api_response = api_instance.get_device_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->get_device_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceModelEntityList**](DeviceModelEntityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_device**
> DeviceResponseBean get_site_device(page_index=page_index, page_size=page_size, ne_type=ne_type, device_type=device_type, site_id=site_id, sort=sort, name=name)

查询设备

## 典型场景 ##   查询设备信息。 ## 接口功能 ##   查询设备信息（真实设备和虚拟设备），包括所属站点、设备类型、设备名称、设备状态等拓扑信息，支持基于站点查询，支持基于字段排序。 ## 接口约束 ##   1、该接口支持租户下北向接口管理访问，必须在用户会话建立后使用;   2、若pageSize和pageIndex参数不传或者为非法参数，则默认按照pageSize=1000，pageIndex=1返回查询结果。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
page_index = 1 # int | 分页的序号。 (optional) (default to 1)
page_size = 1000 # int | 分页的大小。 (optional) (default to 1000)
ne_type = 'AP,AR' # str | 设备类型，类型可以是'AR'，'AP'，'LSW'，'FW'，如果多个类型用逗号分隔（如：AR，AP）。不推荐使用，请尽量以deviceType为主。 (optional)
device_type = 'AP,AR' # str | 设备类型，类型可以是'AR'，'AP'，'LSW'，'FW'，如果多个类型用逗号分隔（如：AR，AP）。如果跟neType同时出现，以deviceType为主。 (optional)
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID，查询单个站点下设备列表，为空查询所有设备。 (optional)
sort = 'name' # str | 排序字段，支持name，esn，deviceModel，deviceType，status，mac，ip，neType，version，description，createTime，registerTime，modifyTime。 (optional)
name = 'deviceName' # str | 设备名称模糊查询，支持精确和模糊匹配，不支持正则。 (optional)

try: 
    # 查询设备
    api_response = api_instance.get_site_device(page_index=page_index, page_size=page_size, ne_type=ne_type, device_type=device_type, site_id=site_id, sort=sort, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->get_site_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| 分页的序号。 | [optional] [default to 1]
 **page_size** | **int**| 分页的大小。 | [optional] [default to 1000]
 **ne_type** | **str**| 设备类型，类型可以是&#39;AR&#39;，&#39;AP&#39;，&#39;LSW&#39;，&#39;FW&#39;，如果多个类型用逗号分隔（如：AR，AP）。不推荐使用，请尽量以deviceType为主。 | [optional] 
 **device_type** | **str**| 设备类型，类型可以是&#39;AR&#39;，&#39;AP&#39;，&#39;LSW&#39;，&#39;FW&#39;，如果多个类型用逗号分隔（如：AR，AP）。如果跟neType同时出现，以deviceType为主。 | [optional] 
 **site_id** | **str**| 站点ID，查询单个站点下设备列表，为空查询所有设备。 | [optional] 
 **sort** | **str**| 排序字段，支持name，esn，deviceModel，deviceType，status，mac，ip，neType，version，description，createTime，registerTime，modifyTime。 | [optional] 
 **name** | **str**| 设备名称模糊查询，支持精确和模糊匹配，不支持正则。 | [optional] 

### Return type

[**DeviceResponseBean**](DeviceResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_devices**
> ModifyDeviceBean modify_devices(device_id, modify_device_dto)

修改设备

## 典型场景 ##  修改设备基本信息时使用。 ## 接口功能 ##  修改设备基本信息。 ## 接口约束 ##  该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
device_id = '00000000-0000-0000-0000-000000000000' # str | 设备ID。
modify_device_dto = cloudcampus.ModifyDeviceDto() # ModifyDeviceDto | 修改设备入参模型。

try: 
    # 修改设备
    api_response = api_instance.modify_devices(device_id, modify_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->modify_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **modify_device_dto** | [**ModifyDeviceDto**](ModifyDeviceDto.md)| 修改设备入参模型。 | 

### Return type

[**ModifyDeviceBean**](ModifyDeviceBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_device**
> CommonResponseBean replace_device(replace_device_dto)

替换设备

## 操作场景 ##  设备替换。 ## 接口功能 ##  设备替换。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
replace_device_dto = cloudcampus.ReplaceDeviceDto() # ReplaceDeviceDto | 设备替换入参模型。

try: 
    # 替换设备
    api_response = api_instance.replace_device(replace_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->replace_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replace_device_dto** | [**ReplaceDeviceDto**](ReplaceDeviceDto.md)| 设备替换入参模型。 | 

### Return type

[**CommonResponseBean**](CommonResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_original_device**
> CommonResponseBean replace_original_device(replace_original_device_dto)

替换设备款型

## 典型场景 ##  设备款型替换。 ## 接口功能 ##  支持替换款型，支持无ESN替换 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DeviceNorthboundApi()
replace_original_device_dto = cloudcampus.ReplaceOriginalDeviceDto() # ReplaceOriginalDeviceDto | 设备替换入参模型。

try: 
    # 替换设备款型
    api_response = api_instance.replace_original_device(replace_original_device_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceNorthboundApi->replace_original_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replace_original_device_dto** | [**ReplaceOriginalDeviceDto**](ReplaceOriginalDeviceDto.md)| 设备替换入参模型。 | 

### Return type

[**CommonResponseBean**](CommonResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

