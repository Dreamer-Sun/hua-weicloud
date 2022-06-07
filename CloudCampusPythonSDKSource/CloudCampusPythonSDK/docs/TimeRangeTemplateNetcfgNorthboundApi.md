# swagger_client.TimeRangeTemplateNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig/timetemplate*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_range_template**](TimeRangeTemplateNetcfgNorthboundApi.md#get_time_range_template) | **GET** /controller/campus/v3/networkconfig/timetemplate/ | 查询时间段模板
[**modify_time_range_template**](TimeRangeTemplateNetcfgNorthboundApi.md#modify_time_range_template) | **PUT** /controller/campus/v3/networkconfig/timetemplate/ | 修改时间段模板
[**time_rangetemplate_post**](TimeRangeTemplateNetcfgNorthboundApi.md#time_rangetemplate_post) | **POST** /controller/campus/v3/networkconfig/timetemplate/ | 新增时间段模板


# **get_time_range_template**
> TimeInfo get_time_range_template(name=name)

查询时间段模板

## 典型场景 ##  提供查询时间段模板接口。 ## 接口功能 ##  查询时间段模板。  ## 接口约束 ##  该接口支持北向接口管理访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeRangeTemplateNetcfgNorthboundApi()
name = 'workday template' # str | 模板名称。 (optional)

try: 
    # 查询时间段模板
    api_response = api_instance.get_time_range_template(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRangeTemplateNetcfgNorthboundApi->get_time_range_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| 模板名称。 | [optional] 

### Return type

[**TimeInfo**](TimeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_time_range_template**
> TemplateResultDto modify_time_range_template(modify_dto)

修改时间段模板

## 典型场景 ##  提供修改时间段模板接口。 ## 接口功能 ##  修改时间段模板。  ## 接口约束 ##  该接口支持北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeRangeTemplateNetcfgNorthboundApi()
modify_dto = cloudcampus.TimeTemplateDto() # TimeTemplateDto | 修改时间段模板入参。

try: 
    # 修改时间段模板
    api_response = api_instance.modify_time_range_template(modify_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRangeTemplateNetcfgNorthboundApi->modify_time_range_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_dto** | [**TimeTemplateDto**](TimeTemplateDto.md)| 修改时间段模板入参。 | 

### Return type

[**TemplateResultDto**](TemplateResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_rangetemplate_post**
> TemplateResultDto time_rangetemplate_post(time_template)

新增时间段模板

## 典型场景 ##  提供新增时间段模板接口。 ## 接口功能 ##  新增时间段模板。  ## 接口约束 ##  该接口支持北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeRangeTemplateNetcfgNorthboundApi()
time_template = cloudcampus.AddTemplateDto() # AddTemplateDto | 增加时间段模板入参。

try: 
    # 新增时间段模板
    api_response = api_instance.time_rangetemplate_post(time_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeRangeTemplateNetcfgNorthboundApi->time_rangetemplate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_template** | [**AddTemplateDto**](AddTemplateDto.md)| 增加时间段模板入参。 | 

### Return type

[**TemplateResultDto**](TemplateResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

