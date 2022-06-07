# swagger_client.ConfigSaveApiNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/config*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_save**](ConfigSaveApiNorthboundApi.md#config_save) | **POST** /controller/campus/v3/config/configsave | 保存配置
[**query_config_save**](ConfigSaveApiNorthboundApi.md#query_config_save) | **GET** /controller/campus/v3/config/configsave/{siteId} | 查询保存结果


# **config_save**
> CommonDto config_save(input)

保存配置

## 典型场景 ##   提供配置保存接口。<br> ## 接口功能 ##    配置保存。<br> ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ConfigSaveApiNorthboundApi()
input = cloudcampus.ConfigSaveDto() # ConfigSaveDto | 配置保存入参。

try: 
    # 保存配置
    api_response = api_instance.config_save(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigSaveApiNorthboundApi->config_save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ConfigSaveDto**](ConfigSaveDto.md)| 配置保存入参。 | 

### Return type

[**CommonDto**](CommonDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_config_save**
> ConfigSaveResult query_config_save(site_id, page_index=page_index, page_size=page_size, ids=ids)

查询保存结果

## 典型场景 ##   提供查询配置保存接口。<br> ## 接口功能 ##    查询配置保存。<br>  ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ConfigSaveApiNorthboundApi()
site_id = 'd623ead6-a2cc-4c3c-9039-dcc8fa898a11' # str | 站点ID，UUID格式。
page_index = 10 # int | 分页查询，起始值。 (optional)
page_size = 20 # int | 分页查询，每页数量。 (optional)
ids = ['ids_example'] # list[str] | 设备ID列表。调用示例：GET /configsave/d623ead6-a2cc-4c3c-9039-dcc8fa898a11?ids=deviceId1&ids=deviceId2&ids=deviceId3。 (optional)

try: 
    # 查询保存结果
    api_response = api_instance.query_config_save(site_id, page_index=page_index, page_size=page_size, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigSaveApiNorthboundApi->query_config_save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **page_index** | **int**| 分页查询，起始值。 | [optional] 
 **page_size** | **int**| 分页查询，每页数量。 | [optional] 
 **ids** | [**list[str]**](str.md)| 设备ID列表。调用示例：GET /configsave/d623ead6-a2cc-4c3c-9039-dcc8fa898a11?ids&#x3D;deviceId1&amp;ids&#x3D;deviceId2&amp;ids&#x3D;deviceId3。 | [optional] 

### Return type

[**ConfigSaveResult**](ConfigSaveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

