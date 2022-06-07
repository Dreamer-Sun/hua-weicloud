# swagger_client.SiteTemplateGroupradioNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site_template_group_radio**](SiteTemplateGroupradioNetcfgNorthboundApi.md#get_site_template_group_radio) | **GET** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apradio | 查询AP站点模板射频配置信息
[**update_site_template_group_radio**](SiteTemplateGroupradioNetcfgNorthboundApi.md#update_site_template_group_radio) | **PUT** /controller/campus/v3/networkconfig/site-templates/{siteTemplateId}/apradio | 修改AP站点模板射频配置信息


# **get_site_template_group_radio**
> SiteTemplateGroupRadioResponseDto get_site_template_group_radio(site_template_id)

查询AP站点模板射频配置信息

## 典型场景 ##  提供查询AP站点模板射频配置信息接口。 ## 接口功能 ##  查询AP站点模板射频配置信息。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateGroupradioNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板ID，UUID格式。

try: 
    # 查询AP站点模板射频配置信息
    api_response = api_instance.get_site_template_group_radio(site_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateGroupradioNetcfgNorthboundApi->get_site_template_group_radio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 

### Return type

[**SiteTemplateGroupRadioResponseDto**](SiteTemplateGroupRadioResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_template_group_radio**
> SiteTemplateGroupRadioResponseDto update_site_template_group_radio(site_template_id, site_template_group_radio_dto)

修改AP站点模板射频配置信息

## 典型场景 ## 提供修改AP站点模板射频配置信息接口。 ## 接口功能 ## 修改AP站点模板射频配置信息。 ## 接口约束 ## 该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateGroupradioNetcfgNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点模板ID，UUID格式。
site_template_group_radio_dto = cloudcampus.SiteTemplateGroupRadioDto() # SiteTemplateGroupRadioDto | 修改AP站点模板射频配置信息。

try: 
    # 修改AP站点模板射频配置信息
    api_response = api_instance.update_site_template_group_radio(site_template_id, site_template_group_radio_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateGroupradioNetcfgNorthboundApi->update_site_template_group_radio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 
 **site_template_group_radio_dto** | [**SiteTemplateGroupRadioDto**](SiteTemplateGroupRadioDto.md)| 修改AP站点模板射频配置信息。 | 

### Return type

[**SiteTemplateGroupRadioResponseDto**](SiteTemplateGroupRadioResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

