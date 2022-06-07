# swagger_client.TenantServiceApi

All URIs are relative to *https://localhost/controller/campus/v1/baseservice/tenants*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_softcom_tenant**](TenantServiceApi.md#create_softcom_tenant) | **POST** /controller/campus/v1/baseservice/tenants/ | 创建租户
[**delete_softcom_tenant**](TenantServiceApi.md#delete_softcom_tenant) | **DELETE** /controller/campus/v1/baseservice/tenants/{tenantId} | 删除租户
[**query_softcom_tenants**](TenantServiceApi.md#query_softcom_tenants) | **GET** /controller/campus/v1/baseservice/tenants/ | 查询租户


# **create_softcom_tenant**
> CreateTenantResponseDto create_softcom_tenant(create_tenant_dto)

创建租户

## 典型场景 ##  创建租户。 ## 接口功能 ##  创建租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TenantServiceApi()
create_tenant_dto = cloudcampus.CreateTenantDto() # CreateTenantDto | 创建租户基本信息。

try: 
    # 创建租户
    api_response = api_instance.create_softcom_tenant(create_tenant_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantServiceApi->create_softcom_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_dto** | [**CreateTenantDto**](CreateTenantDto.md)| 创建租户基本信息。 | 

### Return type

[**CreateTenantResponseDto**](CreateTenantResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_softcom_tenant**
> DeleteResponseDto delete_softcom_tenant(tenant_id)

删除租户

## 典型场景 ##  删除租户。 ## 接口功能 ##  通过租户标识删除租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TenantServiceApi()
tenant_id = '00000000-0000-0000-0000-000000000000' # str | 删除租户ID。

try: 
    # 删除租户
    api_response = api_instance.delete_softcom_tenant(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantServiceApi->delete_softcom_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| 删除租户ID。 | 

### Return type

[**DeleteResponseDto**](DeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_softcom_tenants**
> TenantListDto query_softcom_tenants(page_index=page_index, page_size=page_size)

查询租户

## 典型场景 ##  查询租户。 ## 接口功能 ##  提供分页查询租户列表功能。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用，推荐使用分页查询，如果没有使用分页查询，可能会由于数据量多导致响应时间较长。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TenantServiceApi()
page_index = 0 # int | 分页的序号。 (optional) (default to 0)
page_size = 20 # int | 分页的大小。 (optional)

try: 
    # 查询租户
    api_response = api_instance.query_softcom_tenants(page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantServiceApi->query_softcom_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| 分页的序号。 | [optional] [default to 0]
 **page_size** | **int**| 分页的大小。 | [optional] 

### Return type

[**TenantListDto**](TenantListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

