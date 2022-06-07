# swagger_client.RadiusTemplateNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/profile*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_radius_template**](RadiusTemplateNorthboundApi.md#create_radius_template) | **POST** /controller/campus/v1/networkservice/networkconfig/profile/radius | 创建RADIUS模板
[**delete_radius_template**](RadiusTemplateNorthboundApi.md#delete_radius_template) | **POST** /controller/campus/v1/networkservice/networkconfig/profile/radius/batch-delete | 删除RADIUS模板
[**get_radius_template**](RadiusTemplateNorthboundApi.md#get_radius_template) | **GET** /controller/campus/v1/networkservice/networkconfig/profile/radius | 查询RADIUS模板
[**update_radius_template**](RadiusTemplateNorthboundApi.md#update_radius_template) | **PUT** /controller/campus/v1/networkservice/networkconfig/profile/radius/{id} | 修改RADIUS模板


# **create_radius_template**
> CreateRadiusTempResponseDto create_radius_template(body)

创建RADIUS模板

## 典型场景 ##    创建RADIUS模板。 ## 接口功能 ##    RADIUS模板创建接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.RadiusTemplateNorthboundApi()
body = cloudcampus.CreateRadiusTempDto() # CreateRadiusTempDto | RADIUS服务器模板信息。

try: 
    # 创建RADIUS模板
    api_response = api_instance.create_radius_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusTemplateNorthboundApi->create_radius_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRadiusTempDto**](CreateRadiusTempDto.md)| RADIUS服务器模板信息。 | 

### Return type

[**CreateRadiusTempResponseDto**](CreateRadiusTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_radius_template**
> DeleteRadiusTempResponseDto delete_radius_template(body)

删除RADIUS模板

## 典型场景 ##    删除RADIUS模板信息。 ## 接口功能 ##    RADIUS模板删除接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.RadiusTemplateNorthboundApi()
body = cloudcampus.DeleteRadiusTempDto() # DeleteRadiusTempDto | RADIUS服务器模板ID列表。

try: 
    # 删除RADIUS模板
    api_response = api_instance.delete_radius_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusTemplateNorthboundApi->delete_radius_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRadiusTempDto**](DeleteRadiusTempDto.md)| RADIUS服务器模板ID列表。 | 

### Return type

[**DeleteRadiusTempResponseDto**](DeleteRadiusTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_radius_template**
> GetRadiusTempResponseDto get_radius_template(page_size=page_size, page_index=page_index)

查询RADIUS模板

## 典型场景 ##    查询RADIUS模板列表信息。 ## 接口功能 ##    RADIUS模板查询接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.RadiusTemplateNorthboundApi()
page_size = 20 # int | 每页大小。 (optional)
page_index = 1 # int | 页码。 (optional)

try: 
    # 查询RADIUS模板
    api_response = api_instance.get_radius_template(page_size=page_size, page_index=page_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusTemplateNorthboundApi->get_radius_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| 每页大小。 | [optional] 
 **page_index** | **int**| 页码。 | [optional] 

### Return type

[**GetRadiusTempResponseDto**](GetRadiusTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_radius_template**
> UpdateRadiusTempResponseDto update_radius_template(id, body)

修改RADIUS模板

## 典型场景 ##    修改RADIUS模板。 ## 接口功能 ##    RADIUS模板修改接口。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.RadiusTemplateNorthboundApi()
id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | RADIUS服务器模板ID，UUID格式。
body = cloudcampus.UpdateRadiusTempDto() # UpdateRadiusTempDto | RADIUS服务器模板信息。

try: 
    # 修改RADIUS模板
    api_response = api_instance.update_radius_template(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusTemplateNorthboundApi->update_radius_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| RADIUS服务器模板ID，UUID格式。 | 
 **body** | [**UpdateRadiusTempDto**](UpdateRadiusTempDto.md)| RADIUS服务器模板信息。 | 

### Return type

[**UpdateRadiusTempResponseDto**](UpdateRadiusTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

