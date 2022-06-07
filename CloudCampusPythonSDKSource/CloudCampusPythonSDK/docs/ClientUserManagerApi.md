# swagger_client.ClientUserManagerApi

All URIs are relative to *https://localhost/controller/cloud/v2/northbound/accessuser/haca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cut_user**](ClientUserManagerApi.md#cut_user) | **POST** /controller/cloud/v2/northbound/accessuser/haca/cutuser | 强制用户下线
[**get_authorizationresult**](ClientUserManagerApi.md#get_authorizationresult) | **GET** /controller/cloud/v2/northbound/accessuser/haca/authorizationresult/{psessionid} | 查询授权结果
[**user_authorization**](ClientUserManagerApi.md#user_authorization) | **POST** /controller/cloud/v2/northbound/accessuser/haca/authorization | 授权终端用户


# **cut_user**
> CutUserOutputDto cut_user(body)

强制用户下线

## 典型场景 ##  提供强制用户下线北向接口。 ## 接口功能 ##  强制用户下线 ## 接口约束 ##  该接口支持北向操作管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ClientUserManagerApi()
body = cloudcampus.CutUserInputDto() # CutUserInputDto | 用户信息。

try: 
    # 强制用户下线
    api_response = api_instance.cut_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserManagerApi->cut_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CutUserInputDto**](CutUserInputDto.md)| 用户信息。 | 

### Return type

[**CutUserOutputDto**](CutUserOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorizationresult**
> CommonAuthorizationOutputDto get_authorizationresult(psessionid, node_ip)

查询授权结果

## 典型场景 ##  提供授权结果查询北向接口。 ## 接口功能 ##  根据授权回话ID，查询授权结果 ## 接口约束 ##  该接口支持北向操作管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ClientUserManagerApi()
psessionid = '5ea660be98a84618fa3d6d03f65f47ab578ba3b4216790186a932f9e8c8c880d' # str | 会话ID。
node_ip = '192.168.211.236' # str | 授权节点地址。

try: 
    # 查询授权结果
    api_response = api_instance.get_authorizationresult(psessionid, node_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserManagerApi->get_authorizationresult: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **psessionid** | **str**| 会话ID。 | 
 **node_ip** | **str**| 授权节点地址。 | 

### Return type

[**CommonAuthorizationOutputDto**](CommonAuthorizationOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_authorization**
> CommonAuthorizationOutputDto user_authorization(body)

授权终端用户

## 典型场景 ##  用户授权接口。 ## 接口功能 ##  根据认证用户信息，授予用户对应权限。 ## 接口约束 ##  该接口支持北向操作管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ClientUserManagerApi()
body = cloudcampus.UserAuthorizationInputDto() # UserAuthorizationInputDto | 授权信息。

try: 
    # 授权终端用户
    api_response = api_instance.user_authorization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserManagerApi->user_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAuthorizationInputDto**](UserAuthorizationInputDto.md)| 授权信息。 | 

### Return type

[**CommonAuthorizationOutputDto**](CommonAuthorizationOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

