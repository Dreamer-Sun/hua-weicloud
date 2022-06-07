# swagger_client.SiteTemplateApssidNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site_template_ssid_config**](SiteTemplateApssidNetcfgNorthboundApi.md#create_site_template_ssid_config) | **POST** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apssid | 新增该站点模板的SSID配置
[**delete_site_template_ssid_config**](SiteTemplateApssidNetcfgNorthboundApi.md#delete_site_template_ssid_config) | **POST** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apssid/batch-delete | 删除该站点模板的SSID配置
[**get_site_template_ssid_config**](SiteTemplateApssidNetcfgNorthboundApi.md#get_site_template_ssid_config) | **GET** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apssid | 查询该站点模板的SSID配置
[**update_site_template_ssid_config**](SiteTemplateApssidNetcfgNorthboundApi.md#update_site_template_ssid_config) | **PUT** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apssid/{id} | 修改该站点模板的SSID配置


# **create_site_template_ssid_config**
> SiteTemplateConfigSsidResponse create_site_template_ssid_config(site_template_id, site_template_ssid_config_dto)

新增该站点模板的SSID配置

## 典型场景 ##   提供新增站点模板内AP的SSID配置列表接口。 ## 接口功能 ##   新增站点模板内AP的SSID配置列表。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateApssidNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。
site_template_ssid_config_dto = cloudcampus.SiteTemplateSsidConfigDto() # SiteTemplateSsidConfigDto | 站点模板SSID配置参数。

try: 
    # 新增该站点模板的SSID配置
    api_response = api_instance.create_site_template_ssid_config(site_template_id, site_template_ssid_config_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateApssidNetcfgNorthboundApi->create_site_template_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 
 **site_template_ssid_config_dto** | [**SiteTemplateSsidConfigDto**](SiteTemplateSsidConfigDto.md)| 站点模板SSID配置参数。 | 

### Return type

[**SiteTemplateConfigSsidResponse**](SiteTemplateConfigSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_template_ssid_config**
> SiteTemplateDeleteSsidResponse delete_site_template_ssid_config(site_template_id, site_template_ssid_delete_dto)

删除该站点模板的SSID配置

## 典型场景 ##   提供删除站点模板内AP的SSID配置列表接口。 ## 接口功能 ##   删除站点模板内AP的SSID配置列表。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateApssidNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。
site_template_ssid_delete_dto = cloudcampus.SiteTemplateSsidDeleteDto() # SiteTemplateSsidDeleteDto | 站点模板SSID删除参数。

try: 
    # 删除该站点模板的SSID配置
    api_response = api_instance.delete_site_template_ssid_config(site_template_id, site_template_ssid_delete_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateApssidNetcfgNorthboundApi->delete_site_template_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 
 **site_template_ssid_delete_dto** | [**SiteTemplateSsidDeleteDto**](SiteTemplateSsidDeleteDto.md)| 站点模板SSID删除参数。 | 

### Return type

[**SiteTemplateDeleteSsidResponse**](SiteTemplateDeleteSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_template_ssid_config**
> SiteTemplateQuerySsidResponse get_site_template_ssid_config(site_template_id)

查询该站点模板的SSID配置

## 典型场景 ##   提供查询站点模板内AP的SSID配置列表接口。 ## 接口功能 ##   查询站点模板内AP的SSID配置列表。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateApssidNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。

try: 
    # 查询该站点模板的SSID配置
    api_response = api_instance.get_site_template_ssid_config(site_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateApssidNetcfgNorthboundApi->get_site_template_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 

### Return type

[**SiteTemplateQuerySsidResponse**](SiteTemplateQuerySsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_template_ssid_config**
> SiteTemplateConfigSsidResponse update_site_template_ssid_config(site_template_id, id, site_template_ssid_config_dto)

修改该站点模板的SSID配置

## 典型场景 ##   提供修改站点模板内AP的SSID配置列表接口。 ## 接口功能 ##   修改站点模板内AP的SSID配置。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateApssidNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板标识，UUID格式。
id = 'de5813f8ff1e41f5ba9c324da70b49ed' # str | SSID标识，创建或查询Response中的ID字段。
site_template_ssid_config_dto = cloudcampus.SiteTemplateSsidConfigDto() # SiteTemplateSsidConfigDto | 站点模板SSID配置参数。

try: 
    # 修改该站点模板的SSID配置
    api_response = api_instance.update_site_template_ssid_config(site_template_id, id, site_template_ssid_config_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateApssidNetcfgNorthboundApi->update_site_template_ssid_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板标识，UUID格式。 | 
 **id** | **str**| SSID标识，创建或查询Response中的ID字段。 | 
 **site_template_ssid_config_dto** | [**SiteTemplateSsidConfigDto**](SiteTemplateSsidConfigDto.md)| 站点模板SSID配置参数。 | 

### Return type

[**SiteTemplateConfigSsidResponse**](SiteTemplateConfigSsidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

