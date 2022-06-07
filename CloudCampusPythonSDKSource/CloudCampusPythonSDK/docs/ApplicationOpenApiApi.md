# swagger_client.ApplicationOpenApiApi

All URIs are relative to *https://localhost/controller/campus/v1/performanceservice/application*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_application_info**](ApplicationOpenApiApi.md#query_application_info) | **GET** /controller/campus/v1/performanceservice/application/apptraffic/topapp | 查询终端TopN应用流量


# **query_application_info**
> ApplicationInfoResp query_application_info(app_dimension, time_dimension, top, site_id=site_id)

查询终端TopN应用流量

## 典型场景 ##    提供查询终端TopN应用流量列表的接口。           ## 接口功能 ##    查询终端TopN应用流量列表。 ## 接口约束 ##    1、当前只支持Top5查询，后续扩展更多维度。    2、当前不支持自由选择时间段统计数据，只支持当前一天，当前一周或者当前一个月的数据查询。     

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApplicationOpenApiApi()
app_dimension = 'apptype' # str | 查询维度，app---应用名称、apptype---应用类型。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月。
top = 5 # int | top流量数据个数，当前目前只支持范围5。
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID，如果为空，代表租户维度。 (optional)

try: 
    # 查询终端TopN应用流量
    api_response = api_instance.query_application_info(app_dimension, time_dimension, top, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationOpenApiApi->query_application_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_dimension** | **str**| 查询维度，app---应用名称、apptype---应用类型。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月。 | 
 **top** | **int**| top流量数据个数，当前目前只支持范围5。 | 
 **site_id** | **str**| 站点ID，如果为空，代表租户维度。 | [optional] 

### Return type

[**ApplicationInfoResp**](ApplicationInfoResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

