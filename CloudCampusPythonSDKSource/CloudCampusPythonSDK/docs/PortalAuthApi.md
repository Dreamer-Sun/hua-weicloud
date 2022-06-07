# swagger_client.PortalAuthApi

All URIs are relative to *https://localhost/controller/campus/v1/portalauth*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorization_result**](PortalAuthApi.md#get_authorization_result) | **GET** /controller/campus/v1/portalauth/loginstatus/{psessionid} | 查询认证结果
[**portal_auth_login**](PortalAuthApi.md#portal_auth_login) | **POST** /controller/campus/v1/portalauth/login | 认证终端用户
[**portal_auth_logout**](PortalAuthApi.md#portal_auth_logout) | **POST** /controller/campus/v1/portalauth/logout | 注销终端用户


# **get_authorization_result**
> AuthorizationOutputDto get_authorization_result(psessionid)

查询认证结果

## 典型场景 ##  提供认证结果查询接口。 ## 接口功能 ##  根据认证会话ID，查询认证结果。 ## 接口约束 ##  接口不需要认证。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalAuthApi()
psessionid = '5ea660be98a84618fa3d6d03f65f47ab578ba3b4216790186a932f9e8c8c880d' # str | 会话ID。

try: 
    # 查询认证结果
    api_response = api_instance.get_authorization_result(psessionid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalAuthApi->get_authorization_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psessionid** | **str**| 会话ID。 | 

### Return type

[**AuthorizationOutputDto**](AuthorizationOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_auth_login**
> UserAuthOutputDto portal_auth_login(body)

认证终端用户

## 典型场景 ##  用户认证接口。 ## 接口功能 ##  用户输入认证用户名密码后，控制器对认证信息进行校验，校验通过后通知设备对终端用户进行授权，用户可以接入网络。 ## 接口约束 ##  接口不需要认证，该接口返回认证结果，授权结果需要调用接口查询。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalAuthApi()
body = cloudcampus.UserAuthInputDto() # UserAuthInputDto | 认证信息。

try: 
    # 认证终端用户
    api_response = api_instance.portal_auth_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalAuthApi->portal_auth_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAuthInputDto**](UserAuthInputDto.md)| 认证信息。 | 

### Return type

[**UserAuthOutputDto**](UserAuthOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_auth_logout**
> CommonOutputDto portal_auth_logout(body)

注销终端用户

## 典型场景 ##  用户注销接口。 ## 接口功能 ##  根据用户认证ID，注销用户，注销后，用户将无法继续访问网络。 ## 接口约束 ##  接口不需要认证。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalAuthApi()
body = cloudcampus.UserLogoutInputDto() # UserLogoutInputDto | 注销信息。

try: 
    # 注销终端用户
    api_response = api_instance.portal_auth_logout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalAuthApi->portal_auth_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLogoutInputDto**](UserLogoutInputDto.md)| 注销信息。 | 

### Return type

[**CommonOutputDto**](CommonOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

