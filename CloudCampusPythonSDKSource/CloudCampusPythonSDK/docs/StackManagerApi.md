# swagger_client.StackManagerApi

All URIs are relative to *https://localhost/controller/campus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack**](StackManagerApi.md#create_stack) | **POST** /controller/campus/v3/stack | 添加指定ESN设备到指定堆叠


# **create_stack**
> CreateStackOutDto create_stack(create_stack_dto)

添加指定ESN设备到指定堆叠

## 典型场景 ## 将指定ESN设备加入指定堆叠。 ## 接口功能 ## 将指定ESN设备加入指定堆叠。若堆叠名称存在则将指定ESN设备加入到堆叠；若堆叠名称不存在则将指定堆叠创建后加入指定ESN设备。 ## 接口约束 ## 该接口必须在用户会话建立后使用。加入同一个堆叠的设备必须在同一个站点内。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.StackManagerApi()
create_stack_dto = cloudcampus.CreateStackDto() # CreateStackDto | 创建堆叠入参。

try: 
    # 添加指定ESN设备到指定堆叠
    api_response = api_instance.create_stack(create_stack_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackManagerApi->create_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stack_dto** | [**CreateStackDto**](CreateStackDto.md)| 创建堆叠入参。 | 

### Return type

[**CreateStackOutDto**](CreateStackOutDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

