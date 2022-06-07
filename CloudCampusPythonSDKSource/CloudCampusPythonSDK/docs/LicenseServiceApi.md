# swagger_client.LicenseServiceApi

All URIs are relative to *https://localhost/controller/campus/v3/license*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_active_code**](LicenseServiceApi.md#import_active_code) | **PUT** /controller/campus/v3/license/package/activecode/{id} | 导入激活码


# **import_active_code**
> ImportActiveCodeOut import_active_code(id, import_active_code_dto)

导入激活码

## 典型场景 ##  用户为license导入激活码时使用。 ## 接口功能 ##  给license导入激活码，可以选择延期或者扩容方式，默认选择延期方式导入。 ## 接口约束 ##  该接口必须在用户会话建立后使用，本接口响应时间较长，最长300秒。本接口支持单次导入激活码数量上限为10个。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LicenseServiceApi()
id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | license的ID。
import_active_code_dto = cloudcampus.ImportActiveCodeDto() # ImportActiveCodeDto | 导入激活码请求体。

try: 
    # 导入激活码
    api_response = api_instance.import_active_code(id, import_active_code_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseServiceApi->import_active_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| license的ID。 | 
 **import_active_code_dto** | [**ImportActiveCodeDto**](ImportActiveCodeDto.md)| 导入激活码请求体。 | 

### Return type

[**ImportActiveCodeOut**](ImportActiveCodeOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

