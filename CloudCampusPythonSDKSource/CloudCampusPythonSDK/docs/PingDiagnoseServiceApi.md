# swagger_client.PingDiagnoseServiceApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ping_task**](PingDiagnoseServiceApi.md#create_ping_task) | **POST** /controller/campus/v1/oamservice/ping | 创建ping探测任务
[**query_ping_task_by_task_id**](PingDiagnoseServiceApi.md#query_ping_task_by_task_id) | **GET** /controller/campus/v1/oamservice/ping/{taskId} | 查询ping探测结果


# **create_ping_task**
> PingTaskResponse create_ping_task(request)

创建ping探测任务

## 典型场景 ##  创建ping探测任务。 ## 接口功能 ##  1、创建一个ping任务，并返回任务ID。通过任务ID，可得知本次任务的执行结果。  2、ping间隔500ms，超时时间2000ms，默认ping 5次。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PingDiagnoseServiceApi()
request = cloudcampus.PingDiagnoseDto() # PingDiagnoseDto | 请求参数。

try: 
    # 创建ping探测任务
    api_response = api_instance.create_ping_task(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingDiagnoseServiceApi->create_ping_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PingDiagnoseDto**](PingDiagnoseDto.md)| 请求参数。 | 

### Return type

[**PingTaskResponse**](PingTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_ping_task_by_task_id**
> PingReplyResponse query_ping_task_by_task_id(task_id)

查询ping探测结果

## 典型场景 ##  根据任务ID查询ping探测结果。 ## 接口功能 ##  查询ping探测结果。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PingDiagnoseServiceApi()
task_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | ping探测任务ID，格式UUID。

try: 
    # 查询ping探测结果
    api_response = api_instance.query_ping_task_by_task_id(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingDiagnoseServiceApi->query_ping_task_by_task_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ping探测任务ID，格式UUID。 | 

### Return type

[**PingReplyResponse**](PingReplyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

