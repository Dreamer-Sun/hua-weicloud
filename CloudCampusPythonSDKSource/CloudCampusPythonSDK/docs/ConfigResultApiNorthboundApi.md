# swagger_client.ConfigResultApiNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkconfigservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_results**](ConfigResultApiNorthboundApi.md#get_config_results) | **POST** /controller/campus/v1/networkconfigservice/configresult | 获取配置结果


# **get_config_results**
> StateResponseDto get_config_results(batch_get_dto)

获取配置结果

## 典型场景 ##    提供配置参数的接口，获取配置结果。获取的配置结果为所传siteIds和deviceIds的并集。 ## 接口功能 ##    获取配置结果。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ConfigResultApiNorthboundApi()
batch_get_dto = cloudcampus.BatchGetDto() # BatchGetDto | 服务信息。

try: 
    # 获取配置结果
    api_response = api_instance.get_config_results(batch_get_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigResultApiNorthboundApi->get_config_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_get_dto** | [**BatchGetDto**](BatchGetDto.md)| 服务信息。 | 

### Return type

[**StateResponseDto**](StateResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

