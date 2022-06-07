# swagger_client.PeriodRebootDeviceApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reboot_task_status**](PeriodRebootDeviceApi.md#get_reboot_task_status) | **GET** /controller/campus/v1/oamservice/device-reboot/{deviceId} | 查询设备定时重启任务
[**period_reboot_device**](PeriodRebootDeviceApi.md#period_reboot_device) | **PUT** /controller/campus/v1/oamservice/device-reboot/{deviceId} | 设置设备定时重启任务


# **get_reboot_task_status**
> GetRebootStatusResp get_reboot_task_status(device_id)

查询设备定时重启任务

## 典型场景 ##    查询重启任务状态。 ## 接口功能 ##    基于设备维度查询重启任务状态。 ## 接口约束 ##    北向接口管理员可以访问。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenAuth
cloudcampus.configuration.api_key['X-ACCESS-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
cloudcampus

# create an instance of the API class
api_instance = cloudcampus.PeriodRebootDeviceApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID，UUID格式。

try: 
    # 查询设备定时重启任务
    api_response = api_instance.get_reboot_task_status(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodRebootDeviceApi->get_reboot_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**GetRebootStatusResp**](GetRebootStatusResp.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **period_reboot_device**
> PeriodRebootDeviceResp period_reboot_device(device_id, task_param)

设置设备定时重启任务

## 典型场景 ##    提供创建或更新定时重启设备任务接口。 ## 接口功能 ##    基于设备维度创建或更新定时重启设备任务。 ## 接口约束 ##    北向接口管理员可以访问。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenAuth
cloudcampus.configuration.api_key['X-ACCESS-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
cloudcampus

# create an instance of the API class
api_instance = cloudcampus.PeriodRebootDeviceApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID，UUID格式。
task_param = cloudcampus.ReriodRebootDeviceParam() # ReriodRebootDeviceParam | 参数。

try: 
    # 设置设备定时重启任务
    api_response = api_instance.period_reboot_device(device_id, task_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeriodRebootDeviceApi->period_reboot_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 
 **task_param** | [**ReriodRebootDeviceParam**](ReriodRebootDeviceParam.md)| 参数。 | 

### Return type

[**PeriodRebootDeviceResp**](PeriodRebootDeviceResp.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

