# swagger_client.ApdhcpCfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site_dhcp_config**](ApdhcpCfgNorthboundApi.md#get_site_dhcp_config) | **GET** /controller/campus/v3/networkconfig/site/{siteId}/apdhcp | 查询站点全局DHCP配置
[**update_site_dhcp_config**](ApdhcpCfgNorthboundApi.md#update_site_dhcp_config) | **PUT** /controller/campus/v3/networkconfig/site/{siteId}/apdhcp | 修改站点全局DHCP配置


# **get_site_dhcp_config**
> ApDhcpConfigResponsesDto get_site_dhcp_config(site_id)

查询站点全局DHCP配置

## 典型场景 ##  提供查询AP DHCP接口。<br> ## 接口功能 ##  查询AP DHCP。<br>  ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApdhcpCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点ID，UUID格式。

try: 
    # 查询站点全局DHCP配置
    api_response = api_instance.get_site_dhcp_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApdhcpCfgNorthboundApi->get_site_dhcp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 

### Return type

[**ApDhcpConfigResponsesDto**](ApDhcpConfigResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_dhcp_config**
> ApDhcpConfigResponsesDto update_site_dhcp_config(site_id, ap_dhcp_config_api_dto)

修改站点全局DHCP配置

## 典型场景 ##  提供修改AP DHCP接口。<br>  ## 接口功能 ##  修改AP DHCP。<br>  ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。<br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApdhcpCfgNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点ID，UUID格式。
ap_dhcp_config_api_dto = cloudcampus.ApDhcpConfigApiDto() # ApDhcpConfigApiDto | 修改站点全局DHCP配置入参。

try: 
    # 修改站点全局DHCP配置
    api_response = api_instance.update_site_dhcp_config(site_id, ap_dhcp_config_api_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApdhcpCfgNorthboundApi->update_site_dhcp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **ap_dhcp_config_api_dto** | [**ApDhcpConfigApiDto**](ApDhcpConfigApiDto.md)| 修改站点全局DHCP配置入参。 | 

### Return type

[**ApDhcpConfigResponsesDto**](ApDhcpConfigResponsesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

