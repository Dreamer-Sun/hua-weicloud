# swagger_client.PPSKNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/authconfigservice/accessconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ppsk_account**](PPSKNorthboundApi.md#create_ppsk_account) | **POST** /controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk | 新增PPSK帐号
[**delete_ppsk_account**](PPSKNorthboundApi.md#delete_ppsk_account) | **DELETE** /controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk/{account} | 删除PPSK帐号
[**get_ppsk_account**](PPSKNorthboundApi.md#get_ppsk_account) | **GET** /controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk | 查询PPSK帐号
[**update_ppsk_account**](PPSKNorthboundApi.md#update_ppsk_account) | **PUT** /controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk/{account} | 修改PPSK帐号


# **create_ppsk_account**
> PpskPostOrPutResponseDto create_ppsk_account(site_id, body)

新增PPSK帐号

## 典型场景 ##    在一个站点内，一次新增一个PPSK帐号。 ## 接口功能 ##    新增PPSK帐号。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PPSKNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式。
body = cloudcampus.PPSKPostRequestDto() # PPSKPostRequestDto | PPSK帐号信息参数体。

try: 
    # 新增PPSK帐号
    api_response = api_instance.create_ppsk_account(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PPSKNorthboundApi->create_ppsk_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **body** | [**PPSKPostRequestDto**](PPSKPostRequestDto.md)| PPSK帐号信息参数体。 | 

### Return type

[**PpskPostOrPutResponseDto**](PpskPostOrPutResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ppsk_account**
> PpskDeleteResponseDto delete_ppsk_account(site_id, account)

删除PPSK帐号

## 典型场景 ##    通过帐号名删除PPSK帐号信息。 ## 接口功能 ##    通过帐号名删除PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PPSKNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式。
account = 'PPSK001' # str | PPSK帐号名称。

try: 
    # 删除PPSK帐号
    api_response = api_instance.delete_ppsk_account(site_id, account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PPSKNorthboundApi->delete_ppsk_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **account** | **str**| PPSK帐号名称。 | 

### Return type

[**PpskDeleteResponseDto**](PpskDeleteResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ppsk_account**
> PpskGetResponseDto get_ppsk_account(site_id, account=account, ssid_name=ssid_name, vlan=vlan, page_index=page_index, page_size=page_size)

查询PPSK帐号

## 典型场景 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口功能 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PPSKNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式。
account = 'PPSK001' # str | 帐号名称。 (optional)
ssid_name = 'Huawei-Guest' # str | SSID名称。 (optional)
vlan = 100 # int | 帐号绑定的VLAN。 (optional)
page_index = 1 # int | 页面索引。 (optional)
page_size = 20 # int | 每页显示记录数。 (optional)

try: 
    # 查询PPSK帐号
    api_response = api_instance.get_ppsk_account(site_id, account=account, ssid_name=ssid_name, vlan=vlan, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PPSKNorthboundApi->get_ppsk_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **account** | **str**| 帐号名称。 | [optional] 
 **ssid_name** | **str**| SSID名称。 | [optional] 
 **vlan** | **int**| 帐号绑定的VLAN。 | [optional] 
 **page_index** | **int**| 页面索引。 | [optional] 
 **page_size** | **int**| 每页显示记录数。 | [optional] 

### Return type

[**PpskGetResponseDto**](PpskGetResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ppsk_account**
> PpskPostOrPutResponseDto update_ppsk_account(site_id, account, body)

修改PPSK帐号

## 典型场景 ##    修改PPSK帐号信息，包括PSK、VLAN ID和帐号描述信息。 ## 接口功能 ##    修改PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PPSKNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID，UUID格式。
account = 'PPSK001' # str | PPSK帐号名称。
body = cloudcampus.PPSKPutRequestDto() # PPSKPutRequestDto | PPSK帐号信息参数体。

try: 
    # 修改PPSK帐号
    api_response = api_instance.update_ppsk_account(site_id, account, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PPSKNorthboundApi->update_ppsk_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **account** | **str**| PPSK帐号名称。 | 
 **body** | [**PPSKPutRequestDto**](PPSKPutRequestDto.md)| PPSK帐号信息参数体。 | 

### Return type

[**PpskPostOrPutResponseDto**](PpskPostOrPutResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

