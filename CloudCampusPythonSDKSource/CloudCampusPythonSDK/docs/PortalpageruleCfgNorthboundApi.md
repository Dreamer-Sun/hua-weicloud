# swagger_client.PortalpageruleCfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v3/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portal_page_rule**](PortalpageruleCfgNorthboundApi.md#add_portal_page_rule) | **POST** /controller/campus/v3/networkconfig/site/{siteId}/apportalpagerule | 创建页面推送策略
[**delete_portal_page_rule**](PortalpageruleCfgNorthboundApi.md#delete_portal_page_rule) | **DELETE** /controller/campus/v3/networkconfig/site/{siteId}/apportalpagerule | 删除页面推送策略
[**get_portal_page_rule**](PortalpageruleCfgNorthboundApi.md#get_portal_page_rule) | **GET** /controller/campus/v3/networkconfig/site/{siteId}/apportalpagerule | 查询页面推送策略
[**update_portal_page_rule**](PortalpageruleCfgNorthboundApi.md#update_portal_page_rule) | **PUT** /controller/campus/v3/networkconfig/site/{siteId}/apportalpagerule/{id} | 修改页面推送策略


# **add_portal_page_rule**
> CommonPortalPageRuleOutputDto add_portal_page_rule(site_id, body)

创建页面推送策略

## 典型场景 ##  创建AP portal页面推送策略。 ## 接口功能 ##  创建AP portal页面推送策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalpageruleCfgNorthboundApi()
site_id = '2eab8922-a37d-43b2-9788-33caade63b3d' # str | 站点ID。
body = cloudcampus.AddPortalPageRuleInputDto() # AddPortalPageRuleInputDto | 策略结构。

try: 
    # 创建页面推送策略
    api_response = api_instance.add_portal_page_rule(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalpageruleCfgNorthboundApi->add_portal_page_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**AddPortalPageRuleInputDto**](AddPortalPageRuleInputDto.md)| 策略结构。 | 

### Return type

[**CommonPortalPageRuleOutputDto**](CommonPortalPageRuleOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portal_page_rule**
> DeletePortalPageRuleOutputDto delete_portal_page_rule(site_id, body)

删除页面推送策略

## 典型场景 ##  删除AP portal页面推送策略。 ## 接口功能 ##  删除AP portal页面推送策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalpageruleCfgNorthboundApi()
site_id = '2eab8922-a37d-43b2-9788-33caade63b3d' # str | 站点ID。
body = cloudcampus.DeletePortalPageRuleInputDto() # DeletePortalPageRuleInputDto | 策略结构。

try: 
    # 删除页面推送策略
    api_response = api_instance.delete_portal_page_rule(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalpageruleCfgNorthboundApi->delete_portal_page_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**DeletePortalPageRuleInputDto**](DeletePortalPageRuleInputDto.md)| 策略结构。 | 

### Return type

[**DeletePortalPageRuleOutputDto**](DeletePortalPageRuleOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_page_rule**
> GetPortalPageRuleOutputDto get_portal_page_rule(site_id)

查询页面推送策略

## 典型场景 ##  查询AP portal页面推送策略。 ## 接口功能 ##  查询AP portal页面推送策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalpageruleCfgNorthboundApi()
site_id = '2eab8922-a37d-43b2-9788-33caade63b3d' # str | 站点ID。

try: 
    # 查询页面推送策略
    api_response = api_instance.get_portal_page_rule(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalpageruleCfgNorthboundApi->get_portal_page_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**GetPortalPageRuleOutputDto**](GetPortalPageRuleOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portal_page_rule**
> CommonPortalPageRuleOutputDto update_portal_page_rule(site_id, id, body)

修改页面推送策略

## 典型场景 ##  修改页面推送策略北向接口。 ## 接口功能 ##  修改页面推送策略 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalpageruleCfgNorthboundApi()
site_id = '2eab8922-a37d-43b2-9788-33caade63b3d' # str | 站点ID。
id = '2eab8922a37d43b2978833caade63b5a' # str | 策略ID，格式为UUID。
body = cloudcampus.UpdatePortalPageRuleInputDto() # UpdatePortalPageRuleInputDto | 策略结构。

try: 
    # 修改页面推送策略
    api_response = api_instance.update_portal_page_rule(site_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalpageruleCfgNorthboundApi->update_portal_page_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **id** | **str**| 策略ID，格式为UUID。 | 
 **body** | [**UpdatePortalPageRuleInputDto**](UpdatePortalPageRuleInputDto.md)| 策略结构。 | 

### Return type

[**CommonPortalPageRuleOutputDto**](CommonPortalPageRuleOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

