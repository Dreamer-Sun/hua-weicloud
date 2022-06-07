# swagger_client.SiteTemplateNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_site_template**](SiteTemplateNorthboundApi.md#add_site_template) | **POST** /controller/campus/v1/networkservice/networkconfig/site-templates | 创建站点模板
[**bind_site_template**](SiteTemplateNorthboundApi.md#bind_site_template) | **POST** /controller/campus/v1/networkservice/networkconfig/site-template-binding-relationship/{siteTemplateId} | 绑定一个或多个站点到站点模板
[**delete_site_templates**](SiteTemplateNorthboundApi.md#delete_site_templates) | **POST** /controller/campus/v1/networkservice/networkconfig/site-templates/batch-delete | 删除站点模板
[**get_binding_site_list**](SiteTemplateNorthboundApi.md#get_binding_site_list) | **GET** /controller/campus/v1/networkservice/networkconfig/site-template-binding-relationship/{siteTemplateId}/sites | 根据站点模板ID查询绑定的站点
[**get_binding_site_template**](SiteTemplateNorthboundApi.md#get_binding_site_template) | **GET** /controller/campus/v1/networkservice/networkconfig/site-template-binding-relationship/{siteId}/site-template | 根据站点ID查询绑定的站点模板
[**get_site_templates**](SiteTemplateNorthboundApi.md#get_site_templates) | **GET** /controller/campus/v1/networkservice/networkconfig/site-templates | 查询站点模板
[**unbind_site_template**](SiteTemplateNorthboundApi.md#unbind_site_template) | **POST** /controller/campus/v1/networkservice/networkconfig/site-template-binding-relationship/{siteTemplateId}/batch-delete | 站点模板解绑定一个或多个站点
[**update_site_template**](SiteTemplateNorthboundApi.md#update_site_template) | **PUT** /controller/campus/v1/networkservice/networkconfig/site-templates/{siteTemplateId} | 修改站点模板


# **add_site_template**
> CreateSiteTempResponseDto add_site_template(body)

创建站点模板

## 典型场景 ##  提供创建站点模板接口。 ## 接口功能 ##  创建站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
body = cloudcampus.CreateSiteTempDto() # CreateSiteTempDto | 待创建的站点模板信息。

try: 
    # 创建站点模板
    api_response = api_instance.add_site_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->add_site_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSiteTempDto**](CreateSiteTempDto.md)| 待创建的站点模板信息。 | 

### Return type

[**CreateSiteTempResponseDto**](CreateSiteTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bind_site_template**
> SiteTemplateAndSiteListResponseDto bind_site_template(site_template_id, body)

绑定一个或多个站点到站点模板

## 典型场景 ##  提供绑定一个或多个站点到站点模板接口。 ## 接口功能 ##  绑定一个或多个站点到站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e451' # str | 站点模板ID，UUID格式。
body = cloudcampus.BindingSiteListDto() # BindingSiteListDto | 站点ID列表。

try: 
    # 绑定一个或多个站点到站点模板
    api_response = api_instance.bind_site_template(site_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->bind_site_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 
 **body** | [**BindingSiteListDto**](BindingSiteListDto.md)| 站点ID列表。 | 

### Return type

[**SiteTemplateAndSiteListResponseDto**](SiteTemplateAndSiteListResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_templates**
> DeleteSiteTempResponseDto delete_site_templates(body)

删除站点模板

## 典型场景 ##  提供删除站点模板接口。 ## 接口功能 ##  删除站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
body = cloudcampus.DeleteSiteTempDto() # DeleteSiteTempDto | 待删除的站点模板ID列表。

try: 
    # 删除站点模板
    api_response = api_instance.delete_site_templates(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->delete_site_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteSiteTempDto**](DeleteSiteTempDto.md)| 待删除的站点模板ID列表。 | 

### Return type

[**DeleteSiteTempResponseDto**](DeleteSiteTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binding_site_list**
> GetSiteListDto get_binding_site_list(site_template_id, page_size=page_size, page_index=page_index, sort=sort)

根据站点模板ID查询绑定的站点

## 典型场景 ##  提供根据站点模板ID查询绑定的站点接口。 ## 接口功能 ##  根据站点模板ID查询绑定的站点。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e451' # str | 站点模板ID，UUID格式。
page_size = 20 # int | 每页大小。 (optional)
page_index = 1 # int | 页码。 (optional)
sort = 'name' # str | 排序字段，支持name。 (optional)

try: 
    # 根据站点模板ID查询绑定的站点
    api_response = api_instance.get_binding_site_list(site_template_id, page_size=page_size, page_index=page_index, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->get_binding_site_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 
 **page_size** | **int**| 每页大小。 | [optional] 
 **page_index** | **int**| 页码。 | [optional] 
 **sort** | **str**| 排序字段，支持name。 | [optional] 

### Return type

[**GetSiteListDto**](GetSiteListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binding_site_template**
> GetSiteTempDto get_binding_site_template(site_id)

根据站点ID查询绑定的站点模板

## 典型场景 ##  提供根据站点ID查询绑定的站点模板接口。 ## 接口功能 ##  根据站点ID查询绑定的站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e451' # str | 站点ID，UUID格式。

try: 
    # 根据站点ID查询绑定的站点模板
    api_response = api_instance.get_binding_site_template(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->get_binding_site_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 

### Return type

[**GetSiteTempDto**](GetSiteTempDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_templates**
> GetSiteTempResponseDto get_site_templates(page_size=page_size, page_index=page_index, sort=sort)

查询站点模板

## 典型场景 ##  提供查询站点模板接口。 ## 接口功能 ##  查询站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
page_size = 20 # int | 每页大小。 (optional)
page_index = 1 # int | 页码。 (optional)
sort = 'name' # str | 排序字段，支持name和type，开头带有+表示升序，带有-表示降序，若不设置，默认以name升序返回。 (optional)

try: 
    # 查询站点模板
    api_response = api_instance.get_site_templates(page_size=page_size, page_index=page_index, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->get_site_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| 每页大小。 | [optional] 
 **page_index** | **int**| 页码。 | [optional] 
 **sort** | **str**| 排序字段，支持name和type，开头带有+表示升序，带有-表示降序，若不设置，默认以name升序返回。 | [optional] 

### Return type

[**GetSiteTempResponseDto**](GetSiteTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unbind_site_template**
> SiteTemplateAndSiteListResponseDto unbind_site_template(site_template_id, body)

站点模板解绑定一个或多个站点

## 典型场景 ##  提供站点模板解绑定一个或多个站点接口。 ## 接口功能 ##  站点模板解绑定一个或多个站点。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e451' # str | 站点模板ID，UUID格式。
body = cloudcampus.BindingSiteListDto() # BindingSiteListDto | 站点ID列表。

try: 
    # 站点模板解绑定一个或多个站点
    api_response = api_instance.unbind_site_template(site_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->unbind_site_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 
 **body** | [**BindingSiteListDto**](BindingSiteListDto.md)| 站点ID列表。 | 

### Return type

[**SiteTemplateAndSiteListResponseDto**](SiteTemplateAndSiteListResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_template**
> UpdateSiteTempResponseDto update_site_template(site_template_id, body)

修改站点模板

## 典型场景 ##  提供修改站点模板接口。 ## 接口功能 ##  修改站点模板。 ## 接口约束 ##  该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteTemplateNorthboundApi()
site_template_id = 'fbde1c5d-5b94-49e3-a912-48641015e451' # str | 站点模板ID，UUID格式。
body = cloudcampus.UpdateSiteTempDto() # UpdateSiteTempDto | 站点模板修改内容。

try: 
    # 修改站点模板
    api_response = api_instance.update_site_template(site_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteTemplateNorthboundApi->update_site_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_template_id** | **str**| 站点模板ID，UUID格式。 | 
 **body** | [**UpdateSiteTempDto**](UpdateSiteTempDto.md)| 站点模板修改内容。 | 

### Return type

[**UpdateSiteTempResponseDto**](UpdateSiteTempResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

