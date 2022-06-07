# swagger_client.AspfNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aspf_config**](AspfNorthboundApi.md#get_aspf_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/fwaspf/sites/{siteId} | 查询ASPF配置
[**modify_aspf_config**](AspfNorthboundApi.md#modify_aspf_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/fwaspf/sites/{siteId} | 修改ASPF配置


# **get_aspf_config**
> AspfConfigRespDto get_aspf_config(site_id)

查询ASPF配置

## 典型场景 ##    提供查询ASPF配置参数的接口。 ## 接口功能 ##    查询ASPF配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AspfNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。

try: 
    # 查询ASPF配置
    api_response = api_instance.get_aspf_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AspfNorthboundApi->get_aspf_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**AspfConfigRespDto**](AspfConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_aspf_config**
> AspfConfigRespDto modify_aspf_config(site_id, body)

修改ASPF配置

## 典型场景 ##    提供修改ASPF配置参数的接口。 ## 接口功能 ##    修改ASPF配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AspfNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。
body = cloudcampus.AspfConfigDto() # AspfConfigDto | ASPF入参配置结构体。

try: 
    # 修改ASPF配置
    api_response = api_instance.modify_aspf_config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AspfNorthboundApi->modify_aspf_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**AspfConfigDto**](AspfConfigDto.md)| ASPF入参配置结构体。 | 

### Return type

[**AspfConfigRespDto**](AspfConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

