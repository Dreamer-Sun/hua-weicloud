# swagger_client.NetWorkServiceTacacsApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tacacs_config**](NetWorkServiceTacacsApi.md#get_tacacs_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/tacacs/sites/{siteId}/tacacs | 查询TACACS信息
[**update_tacacs_config**](NetWorkServiceTacacsApi.md#update_tacacs_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/tacacs/sites/{siteId}/tacacs | 修改TACACS信息


# **get_tacacs_config**
> GetTacacsConfigResponse get_tacacs_config(site_id)

查询TACACS信息

## 典型场景 ##    TACACS查询接口，查询TACACS配置。 ## 接口功能 ##    获取TACACS配置（包含TACACS模板对应的配置信息和逃生策略）。 ## 接口约束 ##    该接口操作范围仅限当前租户下的指定站点。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。格式为UUID格式

try: 
    # 查询TACACS信息
    api_response = api_instance.get_tacacs_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsApi->get_tacacs_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。格式为UUID格式 | 

### Return type

[**GetTacacsConfigResponse**](GetTacacsConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tacacs_config**
> EditTacacsConfigResponse update_tacacs_config(site_id, body)

修改TACACS信息

## 典型场景 ##    修改TACACS接口。 ## 接口功能 ##    进行TACACS修改（包含TACACS模板对应的配置信息和逃生策略）。 ## 接口约束 ##    该接口操作范围仅限当前租户下的指定站点。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NetWorkServiceTacacsApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。格式是UUID格式
body = cloudcampus.TacacsServerInfo() # TacacsServerInfo | 配置参数。

try: 
    # 修改TACACS信息
    api_response = api_instance.update_tacacs_config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetWorkServiceTacacsApi->update_tacacs_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。格式是UUID格式 | 
 **body** | [**TacacsServerInfo**](TacacsServerInfo.md)| 配置参数。 | 

### Return type

[**EditTacacsConfigResponse**](EditTacacsConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

