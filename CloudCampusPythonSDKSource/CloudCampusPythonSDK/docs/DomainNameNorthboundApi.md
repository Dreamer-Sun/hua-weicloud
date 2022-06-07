# swagger_client.DomainNameNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](DomainNameNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/domainname/sites/{siteId}/domainnames | 修改站点内设备域名配置
[**get_config**](DomainNameNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/domainname/sites/{siteId}/domainnames | 获取站点内设备域名配置


# **config**
> DomainNameResponseDto config(site_id, body)

修改站点内设备域名配置

## 典型场景 ##    提供配置参数的接口，修改站点内设备域名配置。 ## 接口功能 ##    修改站点内设备域名配置。 ## 接口约束 ##    该接口必须在站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DomainNameNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式
body = cloudcampus.DomainNameDto() # DomainNameDto | 站点内设备域名配置参数体。

try: 
    # 修改站点内设备域名配置
    api_response = api_instance.config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainNameNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式 | 
 **body** | [**DomainNameDto**](DomainNameDto.md)| 站点内设备域名配置参数体。 | 

### Return type

[**DomainNameResponseDto**](DomainNameResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> DomainNameResponseDto get_config(site_id)

获取站点内设备域名配置

## 典型场景 ##    提供查询配置参数的接口，查询站点内设备域名配置。 ## 接口功能 ##    获取站点内设备域名配置。 ## 接口约束 ##    该接口必须在站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.DomainNameNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式。

try: 
    # 获取站点内设备域名配置
    api_response = api_instance.get_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainNameNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 

### Return type

[**DomainNameResponseDto**](DomainNameResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

