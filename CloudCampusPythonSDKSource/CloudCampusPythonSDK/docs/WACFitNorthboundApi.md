# swagger_client.WACFitNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fit_aps**](WACFitNorthboundApi.md#add_fit_aps) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/wac/{acId}/bind-fitaps | 关联指定的WAC设备和Fit AP列表
[**delete_fit_aps**](WACFitNorthboundApi.md#delete_fit_aps) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/wac/{acId}/unbind-fitaps | 解除关联指定的WAC设备和Fit AP列表
[**get_fit_aps**](WACFitNorthboundApi.md#get_fit_aps) | **GET** /controller/campus/v1/networkservice/networkconfig/net/wac/{acId}/fitaps | 查询指定的WAC设备下关联的Fit AP列表


# **add_fit_aps**
> WACFitApResponseDto add_fit_aps(ac_id, body)

关联指定的WAC设备和Fit AP列表

## 典型场景 ##    提供指定的WAC关联Fit AP的接口。 ## 接口功能 ##    提供指定的WAC关联Fit AP的接口。 ## 接口约束 ##    无。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.WACFitNorthboundApi()
ac_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | WAC设备ID。
body = cloudcampus.WACFitApDto() # WACFitApDto | 添加的Fit AP设备信息。

try: 
    # 关联指定的WAC设备和Fit AP列表
    api_response = api_instance.add_fit_aps(ac_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WACFitNorthboundApi->add_fit_aps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| WAC设备ID。 | 
 **body** | [**WACFitApDto**](WACFitApDto.md)| 添加的Fit AP设备信息。 | 

### Return type

[**WACFitApResponseDto**](WACFitApResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fit_aps**
> WACFitApResponseDto delete_fit_aps(ac_id, body)

解除关联指定的WAC设备和Fit AP列表

## 典型场景 ##    提供指定的WAC解除关联的Fit AP的接口。 ## 接口功能 ##    提供指定的WAC解除关联的Fit AP的接口。 ## 接口约束 ##    无。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.WACFitNorthboundApi()
ac_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | WAC或SW设备ID。
body = cloudcampus.WACFitApDto() # WACFitApDto | 移除关联的Fit AP设备信息。

try: 
    # 解除关联指定的WAC设备和Fit AP列表
    api_response = api_instance.delete_fit_aps(ac_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WACFitNorthboundApi->delete_fit_aps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| WAC或SW设备ID。 | 
 **body** | [**WACFitApDto**](WACFitApDto.md)| 移除关联的Fit AP设备信息。 | 

### Return type

[**WACFitApResponseDto**](WACFitApResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fit_aps**
> WACFitQueryResponseDto get_fit_aps(ac_id, page_size, page_index)

查询指定的WAC设备下关联的Fit AP列表

## 典型场景 ##    提供查询指定WAC设备下关联的Fit AP列表的接口。 ## 接口功能 ##    根据指定的WAC设备的ID查询关联的Fit AP列表。 ## 接口约束 ##    无。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.WACFitNorthboundApi()
ac_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | WAC设备ID。
page_size = 20 # int | 分页的大小。
page_index = 1 # int | 分页的序号。

try: 
    # 查询指定的WAC设备下关联的Fit AP列表
    api_response = api_instance.get_fit_aps(ac_id, page_size, page_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WACFitNorthboundApi->get_fit_aps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| WAC设备ID。 | 
 **page_size** | **int**| 分页的大小。 | 
 **page_index** | **int**| 分页的序号。 | 

### Return type

[**WACFitQueryResponseDto**](WACFitQueryResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

