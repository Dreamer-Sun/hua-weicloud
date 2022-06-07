# swagger_client.ConfigDeployApiNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkconfigservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_all_config**](ConfigDeployApiNorthboundApi.md#deploy_all_config) | **POST** /controller/campus/v1/networkconfigservice/deploy/devices/{deviceId}/alldeploy | 全量下发配置
[**redeploy_fail_config**](ConfigDeployApiNorthboundApi.md#redeploy_fail_config) | **POST** /controller/campus/v1/networkconfigservice/deploy/devices/{deviceId}/redeploy | 重下发失败配置


# **deploy_all_config**
> CommonDto deploy_all_config(device_id)

全量下发配置

## 典型场景 ##    提供配置参数的接口，重新下发设备所有配置。 ## 接口功能 ##    重新下发设备所有配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ConfigDeployApiNorthboundApi()
device_id = 'fbde1c5d-5b94-49e3-a912-18641015e23c' # str | 设备ID，UUID格式。

try: 
    # 全量下发配置
    api_response = api_instance.deploy_all_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigDeployApiNorthboundApi->deploy_all_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**CommonDto**](CommonDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_fail_config**
> CommonDto redeploy_fail_config(device_id)

重下发失败配置

## 典型场景 ##    提供配置参数的接口，重新下发配置结果为失败的配置。 ## 接口功能 ##    重新下发配置结果不为成功的配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ConfigDeployApiNorthboundApi()
device_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 设备ID，UUID格式。

try: 
    # 重下发失败配置
    api_response = api_instance.redeploy_fail_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigDeployApiNorthboundApi->redeploy_fail_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**CommonDto**](CommonDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

