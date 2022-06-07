# swagger_client.ApExtraServiceNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](ApExtraServiceNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/apextraservice/sites/{siteId}/apextraservices | 修改站点内AP增值服务配置
[**get_config**](ApExtraServiceNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/apextraservice/sites/{siteId}/apextraservices | 获取站点内AP增值服务配置


# **config**
> ApExtraServiceResponseDto config(site_id, body)

修改站点内AP增值服务配置

## 典型场景 ##    提供配置参数的接口，修改站点内AP增值服务配置。 ## 接口功能 ##    修改站点内AP增值服务配置。 ## 接口约束 ##    该接口必须在站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApExtraServiceNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.ApExtraServiceInputDto() # ApExtraServiceInputDto | 站点内AP增值服务配置参数体。

try: 
    # 修改站点内AP增值服务配置
    api_response = api_instance.config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApExtraServiceNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**ApExtraServiceInputDto**](ApExtraServiceInputDto.md)| 站点内AP增值服务配置参数体。 | 

### Return type

[**ApExtraServiceResponseDto**](ApExtraServiceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> ApExtraServiceResponseDto get_config(site_id)

获取站点内AP增值服务配置

## 典型场景 ##    提供查询配置参数的接口，查询站点内AP增值服务配置。 ## 接口功能 ##    获取站点内AP增值服务配置。 ## 接口约束 ##    该接口必须在站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApExtraServiceNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。

try: 
    # 获取站点内AP增值服务配置
    api_response = api_instance.get_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApExtraServiceNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**ApExtraServiceResponseDto**](ApExtraServiceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

