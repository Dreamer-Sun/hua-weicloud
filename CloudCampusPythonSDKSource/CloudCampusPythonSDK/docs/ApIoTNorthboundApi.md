# swagger_client.ApIoTNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](ApIoTNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/apiot/sites/{siteId}/apiot | 配置站点内AP的IOT配置
[**get_config**](ApIoTNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/apiot/sites/{siteId}/apiot | 查询站点内AP的IOT配置


# **config**
> IoTConfigResponseDto config(site_id, body)

配置站点内AP的IOT配置

## 典型场景 ##    提供配置参数的接口，配置AP的IOT信息。 ## 接口功能 ##    配置AP的IOT信息。 ## 接口约束 ##    该接口必须在租户内，存在AP设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIoTNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。
body = cloudcampus.IoTDto() # IoTDto | 站点内AP的IOT配置参数体。

try: 
    # 配置站点内AP的IOT配置
    api_response = api_instance.config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIoTNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**IoTDto**](IoTDto.md)| 站点内AP的IOT配置参数体。 | 

### Return type

[**IoTConfigResponseDto**](IoTConfigResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> IoTResponseDto get_config(site_id)

查询站点内AP的IOT配置

## 典型场景 ##    提供查询AP的IOT配置信息接口。 ## 接口功能 ##    查询IOT配置。 ## 接口约束 ##    该接口必须在租户内，存在AP设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIoTNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。

try: 
    # 查询站点内AP的IOT配置
    api_response = api_instance.get_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIoTNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**IoTResponseDto**](IoTResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

