# swagger_client.NetWorkServiceLocalUserApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_localuser_info**](NetWorkServiceLocalUserApi.md#create_localuser_info) | **POST** /controller/campus/v1/networkservice/networkconfig/net/localuser/sites/{siteId}/users | 创建本地用户
[**create_template_localuser_info**](NetWorkServiceLocalUserApi.md#create_template_localuser_info) | **POST** /controller/campus/v1/networkservice/networkconfig/net/localuser/site-templates/{siteTemplateId}/users | 创建站点模板的本地用户
[**delete_localuser_info**](NetWorkServiceLocalUserApi.md#delete_localuser_info) | **DELETE** /controller/campus/v1/networkservice/networkconfig/net/localuser/sites/{siteId}/users/{username} | 删除本地用户
[**delete_template_localuser_info**](NetWorkServiceLocalUserApi.md#delete_template_localuser_info) | **DELETE** /controller/campus/v1/networkservice/networkconfig/net/localuser/site-templates/{siteTemplateId}/users/{username} | 删除本地用户
[**get_localuser_info**](NetWorkServiceLocalUserApi.md#get_localuser_info) | **GET** /controller/campus/v1/networkservice/networkconfig/net/localuser/sites/{siteId}/users | 查询本地用户
[**get_template_localuser_info**](NetWorkServiceLocalUserApi.md#get_template_localuser_info) | **GET** /controller/campus/v1/networkservice/networkconfig/net/localuser/site-templates/{siteTemplateId}/users | 查询站点模板的本地用户
[**init_loginuser_info**](NetWorkServiceLocalUserApi.md#init_loginuser_info) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/localuser/users/admin | 配置租户下设备admin账号的默认密码
[**update_localuser_info**](NetWorkServiceLocalUserApi.md#update_localuser_info) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/localuser/sites/{siteId}/users/{username} | 修改本地用户
[**update_template_localuser_info**](NetWorkServiceLocalUserApi.md#update_template_localuser_info) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/localuser/site-templates/{siteTemplateId}/users/{username} | 修改站点模板的本地用户


# **create_localuser_info**
> CreateLocalUserInfoResponse create_localuser_info(site_id, body)

创建本地用户

## 典型场景 ##    提供创建配置参数的接口，创建本地用户接口。 ## 接口功能 ##    提供创建配置参数的接口，创建本地用户密码，接入方式（包括monitor和manager设备本地用户）等。 ## 接口约束 ##    该接口功能基于站点发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.CreateLocalUserInfoRequst() # CreateLocalUserInfoRequst | 本地用户信息。

try: 
    # 创建本地用户
    api_response = api_instance.create_localuser_info(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->create_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**CreateLocalUserInfoRequst**](CreateLocalUserInfoRequst.md)| 本地用户信息。 | 

### Return type

[**CreateLocalUserInfoResponse**](CreateLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_localuser_info**
> CreateLocalUserInfoResponse create_template_localuser_info(site_template_id, body)

创建站点模板的本地用户

## 典型场景 ##    提供创建配置参数的接口，创建站点模板的本地用户接口。 ## 接口功能 ##    提供创建配置参数的接口，创建站点模板的本地用户密码，接入方式（包括monitor和manager设备本地用户）等。 ## 接口约束 ##    该接口功能基于站点发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点模板ID。
body = cloudcampus.CreateLocalUserInfoRequst() # CreateLocalUserInfoRequst | 本地用户信息。

try: 
    # 创建站点模板的本地用户
    api_response = api_instance.create_template_localuser_info(site_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->create_template_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID。 | 
 **body** | [**CreateLocalUserInfoRequst**](CreateLocalUserInfoRequst.md)| 本地用户信息。 | 

### Return type

[**CreateLocalUserInfoResponse**](CreateLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_localuser_info**
> DeleteLocalUserInfoResponse delete_localuser_info(site_id, username)

删除本地用户

## 典型场景 ##    提供删除配置参数的接口，删除本地用户接口。 ## 接口功能 ##    提供删除配置参数的接口，删除本地用户。 ## 接口约束 ##    该接口基于站点发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
username = 'test' # str | 本地用户名，在URL中拼接用户名时，要对特殊字符转义。

try: 
    # 删除本地用户
    api_response = api_instance.delete_localuser_info(site_id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->delete_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **username** | **str**| 本地用户名，在URL中拼接用户名时，要对特殊字符转义。 | 

### Return type

[**DeleteLocalUserInfoResponse**](DeleteLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_localuser_info**
> DeleteLocalUserInfoResponse delete_template_localuser_info(site_template_id, username)

删除本地用户

## 典型场景 ##    提供删除配置参数的接口，删除本地用户接口。 ## 接口功能 ##    提供删除配置参数的接口，删除本地用户。 ## 接口约束 ##    该接口基于站点发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点模板ID。
username = 'test' # str | 本地用户名，在URL中拼接用户名时，要对特殊字符转义。

try: 
    # 删除本地用户
    api_response = api_instance.delete_template_localuser_info(site_template_id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->delete_template_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID。 | 
 **username** | **str**| 本地用户名，在URL中拼接用户名时，要对特殊字符转义。 | 

### Return type

[**DeleteLocalUserInfoResponse**](DeleteLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localuser_info**
> GetLocalUserInfosResponse get_localuser_info(site_id)

查询本地用户

## 典型场景 ##    提供查询配置参数的接口，查询本地用户接口。 ## 接口功能 ##    提供查询配置参数的接口，查询本地用户接口(包括monitor和manager设备本地用户)。 ## 接口约束 ##    该接口基于站点。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。

try: 
    # 查询本地用户
    api_response = api_instance.get_localuser_info(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->get_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**GetLocalUserInfosResponse**](GetLocalUserInfosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_localuser_info**
> GetLocalUserInfosResponse get_template_localuser_info(site_template_id)

查询站点模板的本地用户

## 典型场景 ##    提供查询配置参数的接口，查询站点模板的本地用户接口。 ## 接口功能 ##    提供查询配置参数的接口，查询站点模板的本地用户接口(包括monitor和manager设备本地用户)。 ## 接口约束 ##    该接口基于站点。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点模板ID。

try: 
    # 查询站点模板的本地用户
    api_response = api_instance.get_template_localuser_info(site_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->get_template_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID。 | 

### Return type

[**GetLocalUserInfosResponse**](GetLocalUserInfosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_loginuser_info**
> InitLocalUserInfoResponse init_loginuser_info(body)

配置租户下设备admin账号的默认密码

## 典型场景 ##    提供配置租户下设备admin账号的默认密码的接口。 ## 接口功能 ##    提供配置租户下设备admin账号的默认密码的接口。 ## 接口约束 ##    该接口基于租户发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
body = cloudcampus.InitLocalUserInfoRequst() # InitLocalUserInfoRequst | 租户下设备admin账号的默认密码配置信息。

try: 
    # 配置租户下设备admin账号的默认密码
    api_response = api_instance.init_loginuser_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->init_loginuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InitLocalUserInfoRequst**](InitLocalUserInfoRequst.md)| 租户下设备admin账号的默认密码配置信息。 | 

### Return type

[**InitLocalUserInfoResponse**](InitLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_localuser_info**
> UpdateLocalUserInfoResponse update_localuser_info(site_id, username, body)

修改本地用户

## 典型场景 ##    提供修改配置参数的接口，修改本地用户接口。 ## 接口功能 ##    提供修改配置参数的接口，修改本地用户密码，接入方式（包括monitor和manager设备本地用户）等。 ## 接口约束 ##    该接口基于租户发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
username = 'test' # str | 本地用户名，在URL中拼接用户名时，要对特殊字符转义。
body = cloudcampus.UpdateLocalUserInfoRequst() # UpdateLocalUserInfoRequst | 本地用户配置信息。

try: 
    # 修改本地用户
    api_response = api_instance.update_localuser_info(site_id, username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->update_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **username** | **str**| 本地用户名，在URL中拼接用户名时，要对特殊字符转义。 | 
 **body** | [**UpdateLocalUserInfoRequst**](UpdateLocalUserInfoRequst.md)| 本地用户配置信息。 | 

### Return type

[**UpdateLocalUserInfoResponse**](UpdateLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_localuser_info**
> UpdateLocalUserInfoResponse update_template_localuser_info(site_template_id, username, body)

修改站点模板的本地用户

## 典型场景 ##    提供修改配置参数的接口，修改站点模板的本地用户接口。 ## 接口功能 ##    提供修改配置参数的接口，修改站点模板的本地用户密码，接入方式（包括monitor和manager设备本地用户）等。 ## 接口约束 ##    该接口基于租户发布和管理。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceLocalUserApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点模板ID。
username = 'test' # str | 本地用户名，在URL中拼接用户名时，要对特殊字符转义。
body = cloudcampus.UpdateLocalUserInfoRequst() # UpdateLocalUserInfoRequst | 本地用户配置信息。

try: 
    # 修改站点模板的本地用户
    api_response = api_instance.update_template_localuser_info(site_template_id, username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceLocalUserApi->update_template_localuser_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID。 | 
 **username** | **str**| 本地用户名，在URL中拼接用户名时，要对特殊字符转义。 | 
 **body** | [**UpdateLocalUserInfoRequst**](UpdateLocalUserInfoRequst.md)| 本地用户配置信息。 | 

### Return type

[**UpdateLocalUserInfoResponse**](UpdateLocalUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

