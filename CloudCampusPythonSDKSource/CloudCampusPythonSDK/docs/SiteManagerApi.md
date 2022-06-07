# swagger_client.SiteManagerApi

All URIs are relative to *https://localhost/controller/campus/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sites**](SiteManagerApi.md#create_sites) | **POST** /controller/campus/v3/sites | 创建站点
[**delete_sites**](SiteManagerApi.md#delete_sites) | **DELETE** /controller/campus/v3/sites | 删除站点
[**query_sites**](SiteManagerApi.md#query_sites) | **GET** /controller/campus/v3/sites | 查询站点
[**update_site**](SiteManagerApi.md#update_site) | **PUT** /controller/campus/v3/sites/{siteId} | 修改站点


# **create_sites**
> CreateSiteOut create_sites(create_site_dto)

创建站点

## 典型场景 ## 根据站点名称和描述，创建站点。 ## 接口功能 ## 创建站点。 ## 接口约束 ## 该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteManagerApi()
create_site_dto = cloudcampus.CreateSiteDto() # CreateSiteDto | 创建站点入参。

try: 
    # 创建站点
    api_response = api_instance.create_sites(create_site_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteManagerApi->create_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_site_dto** | [**CreateSiteDto**](CreateSiteDto.md)| 创建站点入参。 | 

### Return type

[**CreateSiteOut**](CreateSiteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sites**
> DeleteSiteOut delete_sites(delete_site_dto)

删除站点

## 典型场景 ## 根据站点ID列表，删除对应的站点。 ## 接口功能 ## 删除站点。 ## 接口约束 ## 该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteManagerApi()
delete_site_dto = cloudcampus.DeleteSiteDto() # DeleteSiteDto | 删除站点请求体。

try: 
    # 删除站点
    api_response = api_instance.delete_sites(delete_site_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteManagerApi->delete_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_site_dto** | [**DeleteSiteDto**](DeleteSiteDto.md)| 删除站点请求体。 | 

### Return type

[**DeleteSiteOut**](DeleteSiteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_sites**
> QuerySitesOut query_sites(page_index=page_index, page_size=page_size, name=name)

查询站点

## 典型场景 ## 传入页面索引和页面长度，查询站点信息。 ## 接口功能 ## 查询站点列表。 ## 接口约束 ## 该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteManagerApi()
page_index = 1 # int | 分页时，当前页面索引，值<=0时默认获取前20条数据。 (optional) (default to 1)
page_size = 20 # int | 分页时，当前页面设备数据长度；pageIndex为空或<=0时，此参数默认20。 (optional) (default to 20)
name = 'siteName' # str | 站点名称模糊查询，支持精确和模糊匹配，不支持正则。 (optional)

try: 
    # 查询站点
    api_response = api_instance.query_sites(page_index=page_index, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteManagerApi->query_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| 分页时，当前页面索引，值&lt;&#x3D;0时默认获取前20条数据。 | [optional] [default to 1]
 **page_size** | **int**| 分页时，当前页面设备数据长度；pageIndex为空或&lt;&#x3D;0时，此参数默认20。 | [optional] [default to 20]
 **name** | **str**| 站点名称模糊查询，支持精确和模糊匹配，不支持正则。 | [optional] 

### Return type

[**QuerySitesOut**](QuerySitesOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> UpdateSitesOut update_site(site_id, update_site_dto)

修改站点

## 典型场景 ## 根据站点ID，修改站点的名称和描述信息。 ## 接口功能 ## 修改站点。 ## 接口约束 ## 该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SiteManagerApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
update_site_dto = cloudcampus.UpdateSitesDto() # UpdateSitesDto | 修改站点请求体。

try: 
    # 修改站点
    api_response = api_instance.update_site(site_id, update_site_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteManagerApi->update_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **update_site_dto** | [**UpdateSitesDto**](UpdateSitesDto.md)| 修改站点请求体。 | 

### Return type

[**UpdateSitesOut**](UpdateSitesOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

