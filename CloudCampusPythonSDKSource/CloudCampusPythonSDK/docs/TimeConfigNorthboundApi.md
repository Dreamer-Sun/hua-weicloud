# swagger_client.TimeConfigNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](TimeConfigNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/time/sites/{siteId}/times | 修改站点内时间配置
[**get_config**](TimeConfigNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/time/sites/{siteId}/times | 查询站点内时间配置
[**get_site_template_time_config**](TimeConfigNorthboundApi.md#get_site_template_time_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/time/site-templates/{siteTemplateId}/times | 查询站点模板时间配置
[**site_template_time_config**](TimeConfigNorthboundApi.md#site_template_time_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/time/site-templates/{siteTemplateId}/times | 修改站点模板时间配置


# **config**
> TimeConfigRespDto config(site_id, body)

修改站点内时间配置

## 典型场景 ##    提供配置参数的接口，进行时间配置。 ## 接口功能 ##    修改时间配置。    配置NTP时，设备通过NTP进行时间同步；否则设备通过控制器进行时间同步。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口，若站点已绑定有NTP时间特性的站点模板则不能使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeConfigNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID，格式为UUID格式。
body = cloudcampus.TimeConfigDto() # TimeConfigDto | 站点内时间配置参数体。

try: 
    # 修改站点内时间配置
    api_response = api_instance.config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeConfigNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，格式为UUID格式。 | 
 **body** | [**TimeConfigDto**](TimeConfigDto.md)| 站点内时间配置参数体。 | 

### Return type

[**TimeConfigRespDto**](TimeConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> TimeConfigRespDto get_config(site_id)

查询站点内时间配置

## 典型场景 ##    提供查询配置参数的接口，查询时间配置信息。 ## 接口功能 ##    获取时间配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口，若站点已绑定有NTP时间特性的站点模板则不能使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeConfigNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID，格式为UUID格式。

try: 
    # 查询站点内时间配置
    api_response = api_instance.get_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeConfigNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，格式为UUID格式。 | 

### Return type

[**TimeConfigRespDto**](TimeConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_template_time_config**
> TimeConfigRespDto get_site_template_time_config(site_template_id)

查询站点模板时间配置

## 典型场景 ##    提供查询配置参数的接口，查询站点模板时间配置信息。 ## 接口功能 ##    获取站点模板时间配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeConfigNorthboundApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点模板ID，格式为UUID格式。

try: 
    # 查询站点模板时间配置
    api_response = api_instance.get_site_template_time_config(site_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeConfigNorthboundApi->get_site_template_time_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，格式为UUID格式。 | 

### Return type

[**TimeConfigRespDto**](TimeConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_template_time_config**
> TimeConfigRespDto site_template_time_config(site_template_id, body)

修改站点模板时间配置

## 典型场景 ##    提供配置参数的接口，进行站点模板时间配置。 ## 接口功能 ##    修改站点模板时间配置。    配置NTP时，设备通过NTP进行时间同步；否则设备通过控制器进行时间同步。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeConfigNorthboundApi()
site_template_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点模板ID，格式为UUID格式。
body = cloudcampus.TimeConfigDto() # TimeConfigDto | 站点内时间配置参数体。

try: 
    # 修改站点模板时间配置
    api_response = api_instance.site_template_time_config(site_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeConfigNorthboundApi->site_template_time_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，格式为UUID格式。 | 
 **body** | [**TimeConfigDto**](TimeConfigDto.md)| 站点内时间配置参数体。 | 

### Return type

[**TimeConfigRespDto**](TimeConfigRespDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

