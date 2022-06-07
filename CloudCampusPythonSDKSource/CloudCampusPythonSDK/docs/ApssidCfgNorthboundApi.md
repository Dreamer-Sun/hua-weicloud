# swagger_client.ApssidCfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site_ssid_config**](ApssidCfgNorthboundApi.md#create_site_ssid_config) | **POST** /controller/campus/v3/networkconfig/site/{siteId}/apssid | 创建指定站点的SSID配置
[**delete_site_ssid_config**](ApssidCfgNorthboundApi.md#delete_site_ssid_config) | **DELETE** /controller/campus/v3/networkconfig/site/{siteId}/apssid | 删除指定站点的SSID配置
[**get_site_ssid_config**](ApssidCfgNorthboundApi.md#get_site_ssid_config) | **GET** /controller/campus/v3/networkconfig/site/{siteId}/apssid | 查询指定站点的SSID配置
[**update_site_ssid_config**](ApssidCfgNorthboundApi.md#update_site_ssid_config) | **PUT** /controller/campus/v3/networkconfig/site/{siteId}/apssid/{id} | 修改指定站点的SSID配置


# **create_site_ssid_config**
> ConfigSsidResponse create_site_ssid_config(site_id, ssid_config_dto)

创建指定站点的SSID配置

## 典型场景 ##   提供在指定站点，新增AP的SSID配置的接口。<br> ## 接口功能 ##   新增站点内AP的SSID配置。<br> ## 接口约束 ##   该接口租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApssidCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
ssid_config_dto = cloudcampus.SsidConfigDto() # SsidConfigDto | SSID配置

try: 
    # 创建指定站点的SSID配置
    api_response = api_instance.create_site_ssid_config(site_id, ssid_config_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApssidCfgNorthboundApi->create_site_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **ssid_config_dto** | [**SsidConfigDto**](SsidConfigDto.md)| SSID配置 | 

### Return type

[**ConfigSsidResponse**](ConfigSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_ssid_config**
> DeleteSsidResponse delete_site_ssid_config(site_id, id)

删除指定站点的SSID配置

## 典型场景 ##   删除AP的SSID配置的接口。<br> ## 接口功能 ##   删除站点内AP的SSID配置。<br> ## 接口约束 ##   该接口租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApssidCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
id = cloudcampus.SsidDeleteDto() # SsidDeleteDto | 待删除的ID。

try: 
    # 删除指定站点的SSID配置
    api_response = api_instance.delete_site_ssid_config(site_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApssidCfgNorthboundApi->delete_site_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **id** | [**SsidDeleteDto**](SsidDeleteDto.md)| 待删除的ID。 | 

### Return type

[**DeleteSsidResponse**](DeleteSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_ssid_config**
> QuerySsidResponse get_site_ssid_config(site_id)

查询指定站点的SSID配置

## 典型场景 ##   提供siteId查询站点内AP的SSID配置列表。<br> ## 接口功能 ##   查询站点内AP的SSID配置列表。<br> ## 接口约束 ##   该接口租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApssidCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。

try: 
    # 查询指定站点的SSID配置
    api_response = api_instance.get_site_ssid_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApssidCfgNorthboundApi->get_site_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 

### Return type

[**QuerySsidResponse**](QuerySsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_ssid_config**
> ConfigSsidResponse update_site_ssid_config(site_id, id, ssid_config_dto)

修改指定站点的SSID配置

## 典型场景 ##   提供在指定站点，修改AP的SSID配置的接口。<br> ## 接口功能 ##   修改站点内AP的SSID配置。<br> ## 接口约束 ##   该接口租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApssidCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
id = 'de5813f8ff1e41f5ba9c324da70b49ed' # str | SSID标识，创建或查询Response中的ID字段。
ssid_config_dto = cloudcampus.SsidConfigDto() # SsidConfigDto | ssid配置。

try: 
    # 修改指定站点的SSID配置
    api_response = api_instance.update_site_ssid_config(site_id, id, ssid_config_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApssidCfgNorthboundApi->update_site_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **id** | **str**| SSID标识，创建或查询Response中的ID字段。 | 
 **ssid_config_dto** | [**SsidConfigDto**](SsidConfigDto.md)| ssid配置。 | 

### Return type

[**ConfigSsidResponse**](ConfigSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

