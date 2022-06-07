# swagger_client.SitesNorthBoundApi

All URIs are relative to *https://localhost/controller/campus/v1/indoormapservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buildings_info**](SitesNorthBoundApi.md#get_buildings_info) | **GET** /controller/campus/v1/indoormapservice/sites/{siteId}/buildings | 查询站点中所有楼栋基本信息


# **get_buildings_info**
> QueryBuildingsResponse get_buildings_info(site_id)

查询站点中所有楼栋基本信息

## 典型场景 ##  查询站点中所有楼栋。 ## 接口功能 ##  查询站点中所有楼栋基本信息，包含楼栋ID，楼栋名称，楼层列表。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SitesNorthBoundApi()
site_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | 站点标识，格式UUID。

try: 
    # 查询站点中所有楼栋基本信息
    api_response = api_instance.get_buildings_info(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesNorthBoundApi->get_buildings_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，格式UUID。 | 

### Return type

[**QueryBuildingsResponse**](QueryBuildingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

