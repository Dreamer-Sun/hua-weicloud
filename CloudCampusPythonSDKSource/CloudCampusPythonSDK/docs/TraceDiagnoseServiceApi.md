# swagger_client.TraceDiagnoseServiceApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trace_task**](TraceDiagnoseServiceApi.md#create_trace_task) | **POST** /controller/campus/v1/oamservice/trace | 创建Trace探测任务
[**query_trace_task_by_task_id**](TraceDiagnoseServiceApi.md#query_trace_task_by_task_id) | **GET** /controller/campus/v1/oamservice/trace/{taskId} | 查询Trace探测结果


# **create_trace_task**
> TraceTaskResponse create_trace_task(request)

创建Trace探测任务

## 典型场景 ##  创建Trace探测任务。 ## 接口功能 ##  创建Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TraceDiagnoseServiceApi()
request = cloudcampus.TraceDiagnoseDto() # TraceDiagnoseDto | 请求参数。

try: 
    # 创建Trace探测任务
    api_response = api_instance.create_trace_task(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TraceDiagnoseServiceApi->create_trace_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TraceDiagnoseDto**](TraceDiagnoseDto.md)| 请求参数。 | 

### Return type

[**TraceTaskResponse**](TraceTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_trace_task_by_task_id**
> TraceReplyResponse query_trace_task_by_task_id(task_id)

查询Trace探测结果

## 典型场景 ##  根据taskId查询trace任务。 ## 接口功能 ##  查询Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TraceDiagnoseServiceApi()
task_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | Trace探测任务ID，格式UUID。

try: 
    # 查询Trace探测结果
    api_response = api_instance.query_trace_task_by_task_id(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TraceDiagnoseServiceApi->query_trace_task_by_task_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Trace探测任务ID，格式UUID。 | 

### Return type

[**TraceReplyResponse**](TraceReplyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

