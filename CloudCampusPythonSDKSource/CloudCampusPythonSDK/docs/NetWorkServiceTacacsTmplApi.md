# swagger_client.NetWorkServiceTacacsTmplApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/profile*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tacacs_tmpl**](NetWorkServiceTacacsTmplApi.md#create_tacacs_tmpl) | **POST** /controller/campus/v1/networkservice/networkconfig/profile/tacacs/ | 创建TACACS模板
[**delete_tacacs_tmpl**](NetWorkServiceTacacsTmplApi.md#delete_tacacs_tmpl) | **POST** /controller/campus/v1/networkservice/networkconfig/profile/tacacs/batch-delete | 删除TACACS模板
[**edit_tacacs_tmpl**](NetWorkServiceTacacsTmplApi.md#edit_tacacs_tmpl) | **PUT** /controller/campus/v1/networkservice/networkconfig/profile/tacacs/{id} | 修改TACACS模板
[**get_tacacs_tmpl**](NetWorkServiceTacacsTmplApi.md#get_tacacs_tmpl) | **GET** /controller/campus/v1/networkservice/networkconfig/profile/tacacs/ | 查询TACACS模板


# **create_tacacs_tmpl**
> CreateTacacsTmplResponse create_tacacs_tmpl(body)

创建TACACS模板

## 典型场景 ##    创建Tacacs模板。 ## 接口功能 ##   Tacacs模板创建接口（包含Tacacs模板对应的名称、描述、认证服务器地址、端口等）。 ## 接口约束 ##    该接口基于租户下；优先配置主服务器地址/端口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsTmplApi()
body = cloudcampus.CreateTacacsTmplInfoDto() # CreateTacacsTmplInfoDto | tacacs服务器模板信息。

try: 
    # 创建TACACS模板
    api_response = api_instance.create_tacacs_tmpl(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsTmplApi->create_tacacs_tmpl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTacacsTmplInfoDto**](CreateTacacsTmplInfoDto.md)| tacacs服务器模板信息。 | 

### Return type

[**CreateTacacsTmplResponse**](CreateTacacsTmplResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tacacs_tmpl**
> DeleteTacacsTmplResponses delete_tacacs_tmpl(body)

删除TACACS模板

## 典型场景 ##    删除配置模板列表信息。 ## 接口功能 ##   Tacacs模板删除接口（包含Tacacs模板对应的名称、描述、认证服务器地址、端口等）。 ## 接口约束 ##    该接口基于租户下；如果模板被引用不可删除。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsTmplApi()
body = cloudcampus.DeleteTacacsTmplReuest() # DeleteTacacsTmplReuest | tacacs服务器模板id列表。

try: 
    # 删除TACACS模板
    api_response = api_instance.delete_tacacs_tmpl(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsTmplApi->delete_tacacs_tmpl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTacacsTmplReuest**](DeleteTacacsTmplReuest.md)| tacacs服务器模板id列表。 | 

### Return type

[**DeleteTacacsTmplResponses**](DeleteTacacsTmplResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_tacacs_tmpl**
> EditTacacsTmplResponse edit_tacacs_tmpl(id, body)

修改TACACS模板

## 典型场景 ##    修改Tacacs模板。 ## 接口功能 ##   Tacacs模板修改接口（包含Tacacs模板对应的名称、描述、认证服务器地址、端口等）。 ## 接口约束 ##    该接口基于租户下；优先配置主服务器地址/端口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsTmplApi()
id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | tacacs服务器模板Id。
body = cloudcampus.UpdateTacacsTmplInfoDto() # UpdateTacacsTmplInfoDto | tacacs服务器模板body。

try: 
    # 修改TACACS模板
    api_response = api_instance.edit_tacacs_tmpl(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsTmplApi->edit_tacacs_tmpl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| tacacs服务器模板Id。 | 
 **body** | [**UpdateTacacsTmplInfoDto**](UpdateTacacsTmplInfoDto.md)| tacacs服务器模板body。 | 

### Return type

[**EditTacacsTmplResponse**](EditTacacsTmplResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tacacs_tmpl**
> GetTacacsTmplResponse get_tacacs_tmpl()

查询TACACS模板

## 典型场景 ##    查询配置模板列表信息。 ## 接口功能 ##   Tacacs模板查询接口（包含Tacacs模板对应的名称、描述、认证服务器地址、端口等）。 ## 接口约束 ##    该接口基于租户下；优先配置主服务器地址/端口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsTmplApi()

try: 
    # 查询TACACS模板
    api_response = api_instance.get_tacacs_tmpl()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsTmplApi->get_tacacs_tmpl: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTacacsTmplResponse**](GetTacacsTmplResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

