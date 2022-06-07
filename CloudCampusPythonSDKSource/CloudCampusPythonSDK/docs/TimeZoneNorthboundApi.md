# swagger_client.TimeZoneNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_timezone**](TimeZoneNorthboundApi.md#get_timezone) | **GET** /controller/campus/v1/networkservice/networkconfig/net/timezones | 查询站点内时区资源


# **get_timezone**
> TimezoneRespDto get_timezone()

查询站点内时区资源

## 典型场景 ##    提供查询接口，查询时区资源。 ## 接口功能 ##    获取时区资源。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeZoneNorthboundApi()

try: 
    # 查询站点内时区资源
    api_response = api_instance.get_timezone()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeZoneNorthboundApi->get_timezone: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimezoneRespDto**](TimezoneRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

