# swagger_client.AuthenProfileNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig/openprofile*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authen_profile**](AuthenProfileNorthboundApi.md#create_authen_profile) | **POST** /controller/campus/v3/networkconfig/openprofile/authenprofile | 创建认证模板
[**delete_authen_profile**](AuthenProfileNorthboundApi.md#delete_authen_profile) | **POST** /controller/campus/v3/networkconfig/openprofile/authenprofile/batch-delete | 删除认证模板
[**get_authen_profile**](AuthenProfileNorthboundApi.md#get_authen_profile) | **GET** /controller/campus/v3/networkconfig/openprofile/authenprofile | 查询认证模板
[**get_authen_profile_by_id**](AuthenProfileNorthboundApi.md#get_authen_profile_by_id) | **GET** /controller/campus/v3/networkconfig/openprofile/authenprofile/{id} | 根据ID查询认证模板
[**update_authen_profile**](AuthenProfileNorthboundApi.md#update_authen_profile) | **PUT** /controller/campus/v3/networkconfig/openprofile/authenprofile/{id} | 更新认证模板


# **create_authen_profile**
> AuthenRespDto create_authen_profile(authen_profile_dto)

创建认证模板

## 典型场景 ##  提供创建认证模板的接口。<br> ## 接口功能 ##  提供创建认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenProfileNorthboundApi()
authen_profile_dto = cloudcampus.AuthenProfileDto() # AuthenProfileDto | 创建认证模板北向入参。

try: 
    # 创建认证模板
    api_response = api_instance.create_authen_profile(authen_profile_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenProfileNorthboundApi->create_authen_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authen_profile_dto** | [**AuthenProfileDto**](AuthenProfileDto.md)| 创建认证模板北向入参。 | 

### Return type

[**AuthenRespDto**](AuthenRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authen_profile**
> AuthenProfileDeleteRespDto delete_authen_profile(authen_profile_delete_dto)

删除认证模板

## 典型场景 ##  提供批量删除认证模板的接口。<br> ## 接口功能 ##  提供批量删除认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenProfileNorthboundApi()
authen_profile_delete_dto = cloudcampus.AuthenProfileDeleteDto() # AuthenProfileDeleteDto | 删除认证模板北向入参。

try: 
    # 删除认证模板
    api_response = api_instance.delete_authen_profile(authen_profile_delete_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenProfileNorthboundApi->delete_authen_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authen_profile_delete_dto** | [**AuthenProfileDeleteDto**](AuthenProfileDeleteDto.md)| 删除认证模板北向入参。 | 

### Return type

[**AuthenProfileDeleteRespDto**](AuthenProfileDeleteRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authen_profile**
> AuthenProfileQueryResultDto get_authen_profile(page_num=page_num, page_size=page_size, query_value=query_value)

查询认证模板

## 典型场景 ##  提供查询认证模板的接口。<br> ## 接口功能 ##  提供查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenProfileNorthboundApi()
page_num = 56 # int | 页码。 (optional)
page_size = 56 # int | 分页尺寸。 (optional)
query_value = 'query_value_example' # str | 认证模板名称模糊查询，支持精确和模糊匹配，不支持正则。 (optional)

try: 
    # 查询认证模板
    api_response = api_instance.get_authen_profile(page_num=page_num, page_size=page_size, query_value=query_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenProfileNorthboundApi->get_authen_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_num** | **int**| 页码。 | [optional] 
 **page_size** | **int**| 分页尺寸。 | [optional] 
 **query_value** | **str**| 认证模板名称模糊查询，支持精确和模糊匹配，不支持正则。 | [optional] 

### Return type

[**AuthenProfileQueryResultDto**](AuthenProfileQueryResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authen_profile_by_id**
> AuthenRespDto get_authen_profile_by_id(id)

根据ID查询认证模板

## 典型场景 ##  提供根据ID查询认证模板的接口。<br> ## 接口功能 ##  提供根据ID查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenProfileNorthboundApi()
id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 认证模板ID。

try: 
    # 根据ID查询认证模板
    api_response = api_instance.get_authen_profile_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenProfileNorthboundApi->get_authen_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 认证模板ID。 | 

### Return type

[**AuthenRespDto**](AuthenRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authen_profile**
> AuthenRespDto update_authen_profile(id, authen_profile_dto)

更新认证模板

## 典型场景 ##  提供更新认证模板的接口。<br> ## 接口功能 ##  提供更新认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenProfileNorthboundApi()
id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 认证模板ID。
authen_profile_dto = cloudcampus.AuthenProfileDto() # AuthenProfileDto | 更新认证模板北向入参。

try: 
    # 更新认证模板
    api_response = api_instance.update_authen_profile(id, authen_profile_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenProfileNorthboundApi->update_authen_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 认证模板ID。 | 
 **authen_profile_dto** | [**AuthenProfileDto**](AuthenProfileDto.md)| 更新认证模板北向入参。 | 

### Return type

[**AuthenRespDto**](AuthenRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

