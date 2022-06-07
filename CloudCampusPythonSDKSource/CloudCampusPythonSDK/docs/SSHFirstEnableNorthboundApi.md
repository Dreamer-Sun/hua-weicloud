# swagger_client.SSHFirstEnableNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ssh_first_enable_config**](SSHFirstEnableNorthboundApi.md#get_ssh_first_enable_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/ssh/sites/{siteId}/sshfirstenable | 查询SSH客户端首次认证免公钥配置
[**update_ssh_first_enable_config**](SSHFirstEnableNorthboundApi.md#update_ssh_first_enable_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/ssh/sites/{siteId}/sshfirstenable | 修改SSH客户端首次认证免公钥配置


# **get_ssh_first_enable_config**
> SSHFirstEnableResponseDto get_ssh_first_enable_config(site_id)

查询SSH客户端首次认证免公钥配置

## 典型场景 ##    提供查询配置参数的接口，查询SSH客户端首次认证免公钥开关是否打开。 ## 接口功能 ##    在某个站点下，查询SSH客户端首次认证免公钥开关是否打开。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SSHFirstEnableNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。

try: 
    # 查询SSH客户端首次认证免公钥配置
    api_response = api_instance.get_ssh_first_enable_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHFirstEnableNorthboundApi->get_ssh_first_enable_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**SSHFirstEnableResponseDto**](SSHFirstEnableResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_first_enable_config**
> SSHFirstEnableResponseDto update_ssh_first_enable_config(site_id, body)

修改SSH客户端首次认证免公钥配置

## 典型场景 ##    提供修改配置参数的接口，修改SSH客户端首次认证免公钥开关。 ## 接口功能 ##    在某个站点下，修改SSH客户端首次认证免公钥开关。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SSHFirstEnableNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.SSHFirstEnableDto() # SSHFirstEnableDto | SSH客户端首次认证免公钥开关参数体。

try: 
    # 修改SSH客户端首次认证免公钥配置
    api_response = api_instance.update_ssh_first_enable_config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSHFirstEnableNorthboundApi->update_ssh_first_enable_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**SSHFirstEnableDto**](SSHFirstEnableDto.md)| SSH客户端首次认证免公钥开关参数体。 | 

### Return type

[**SSHFirstEnableResponseDto**](SSHFirstEnableResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

