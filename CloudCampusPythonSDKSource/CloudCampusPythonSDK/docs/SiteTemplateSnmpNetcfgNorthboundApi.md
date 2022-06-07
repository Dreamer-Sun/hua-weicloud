# swagger_client.SiteTemplateSnmpNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site_template_snmp**](SiteTemplateSnmpNetcfgNorthboundApi.md#get_site_template_snmp) | **GET** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/snmp | 查询该站点模板SNMP配置信息
[**update_site_template_snmp**](SiteTemplateSnmpNetcfgNorthboundApi.md#update_site_template_snmp) | **PUT** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/snmp | 修改该站点模板SNMP配置信息


# **get_site_template_snmp**
> SiteTemplateSnmpResponseDto get_site_template_snmp(site_template_id)

查询该站点模板SNMP配置信息

## 典型场景 ##   提供查询该站点模板SNMP配置信息接口。 ## 接口功能 ##   查询该站点模板SNMP配置信息。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateSnmpNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。

try: 
    # 查询该站点模板SNMP配置信息
    api_response = api_instance.get_site_template_snmp(site_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateSnmpNetcfgNorthboundApi->get_site_template_snmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 

### Return type

[**SiteTemplateSnmpResponseDto**](SiteTemplateSnmpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_template_snmp**
> SiteTemplateSnmpResponseDto update_site_template_snmp(site_template_id, site_template_snmp_dto)

修改该站点模板SNMP配置信息

## 典型场景 ##   提供修改该站点模板SNMP配置信息接口 ## 接口功能 ##   修改该站点模板SNMP配置信息。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateSnmpNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。
site_template_snmp_dto = cloudcampus.SiteTemplateSnmpDto() # SiteTemplateSnmpDto | 站点模板SNMP配置信息

try: 
    # 修改该站点模板SNMP配置信息
    api_response = api_instance.update_site_template_snmp(site_template_id, site_template_snmp_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateSnmpNetcfgNorthboundApi->update_site_template_snmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 
 **site_template_snmp_dto** | [**SiteTemplateSnmpDto**](SiteTemplateSnmpDto.md)| 站点模板SNMP配置信息 | 

### Return type

[**SiteTemplateSnmpResponseDto**](SiteTemplateSnmpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

