# swagger_client.AclTemplateNBNorthBoundApi

All URIs are relative to *https://localhost/controller/campus/v3/profile/acl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_acl_template**](AclTemplateNBNorthBoundApi.md#add_acl_template) | **POST** /controller/campus/v3/profile/acl/ | 创建ACL模板
[**delete_acl_template**](AclTemplateNBNorthBoundApi.md#delete_acl_template) | **DELETE** /controller/campus/v3/profile/acl/ | 删除ACL模板
[**get_acl_template**](AclTemplateNBNorthBoundApi.md#get_acl_template) | **GET** /controller/campus/v3/profile/acl/ | 查询ACL模板
[**update_acl_template**](AclTemplateNBNorthBoundApi.md#update_acl_template) | **PUT** /controller/campus/v3/profile/acl/{id} | 更新ACL模板


# **add_acl_template**
> UpdateAclRet add_acl_template(body)

创建ACL模板

## 典型场景 ##  提供创建ACL模板接口。<br> ## 接口功能 ##  创建ACL模板。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AclTemplateNBNorthBoundApi()
body = cloudcampus.AclDtoDetail() # AclDtoDetail | 待创建的ACL模板信息。

try: 
    # 创建ACL模板
    api_response = api_instance.add_acl_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclTemplateNBNorthBoundApi->add_acl_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AclDtoDetail**](AclDtoDetail.md)| 待创建的ACL模板信息。 | 

### Return type

[**UpdateAclRet**](UpdateAclRet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acl_template**
> DeleteAclRet delete_acl_template(body)

删除ACL模板

## 典型场景 ##  提供删除ACL模板接口。<br> ## 接口功能 ##  删除ACL模板。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AclTemplateNBNorthBoundApi()
body = cloudcampus.DeleteTemplateDto() # DeleteTemplateDto | 待删除的ACL模板标识。

try: 
    # 删除ACL模板
    api_response = api_instance.delete_acl_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclTemplateNBNorthBoundApi->delete_acl_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteTemplateDto**](DeleteTemplateDto.md)| 待删除的ACL模板标识。 | 

### Return type

[**DeleteAclRet**](DeleteAclRet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl_template**
> QueryAclRet get_acl_template()

查询ACL模板

## 典型场景 ##  提供查询ACL模板接口。<br> ## 接口功能 ##  查询ACL模板。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AclTemplateNBNorthBoundApi()

try: 
    # 查询ACL模板
    api_response = api_instance.get_acl_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclTemplateNBNorthBoundApi->get_acl_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryAclRet**](QueryAclRet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_acl_template**
> UpdateAclRet update_acl_template(id, body)

更新ACL模板

## 典型场景 ##  提供更新ACL模板接口。<br> ## 接口功能 ##  更新ACL模板。<br> ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AclTemplateNBNorthBoundApi()
id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 待更新的ACL模板标识。
body = cloudcampus.UpadateAclDto() # UpadateAclDto | 待更新的ACL模板信息。

try: 
    # 更新ACL模板
    api_response = api_instance.update_acl_template(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclTemplateNBNorthBoundApi->update_acl_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 待更新的ACL模板标识。 | 
 **body** | [**UpadateAclDto**](UpadateAclDto.md)| 待更新的ACL模板信息。 | 

### Return type

[**UpdateAclRet**](UpdateAclRet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

