# swagger_client.LSWStpProtectionNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stp_protection**](LSWStpProtectionNorthboundApi.md#create_stp_protection) | **POST** /controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection | 创建交换机STP保护配置
[**delete_stp_protection**](LSWStpProtectionNorthboundApi.md#delete_stp_protection) | **POST** /controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection/batch-delete | 删除交换机STP保护配置
[**get_stp_protection**](LSWStpProtectionNorthboundApi.md#get_stp_protection) | **GET** /controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection | 查询交换机STP保护配置
[**update_stp_protection**](LSWStpProtectionNorthboundApi.md#update_stp_protection) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection | 修改交换机STP保护配置


# **create_stp_protection**
> StpProtectionResponseDto create_stp_protection(site_id, body)

创建交换机STP保护配置

## 典型场景 ##    提供配置参数的接口，创建交换机STP保护配置。 ## 接口功能 ##    创建交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpProtectionNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.StpProtectionRequestDto() # StpProtectionRequestDto | 创建交换机STP保护配置信息。

try: 
    # 创建交换机STP保护配置
    api_response = api_instance.create_stp_protection(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpProtectionNorthboundApi->create_stp_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**StpProtectionRequestDto**](StpProtectionRequestDto.md)| 创建交换机STP保护配置信息。 | 

### Return type

[**StpProtectionResponseDto**](StpProtectionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stp_protection**
> DeleteStpProtectionResponseDto delete_stp_protection(site_id, body)

删除交换机STP保护配置

## 典型场景 ##    提供删除配置参数的接口，删除交换机STP保护配置。 ## 接口功能 ##    删除交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpProtectionNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.DeleteStpProtectionRequestDto() # DeleteStpProtectionRequestDto | 删除交换机STP保护配置请求参数体。

try: 
    # 删除交换机STP保护配置
    api_response = api_instance.delete_stp_protection(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpProtectionNorthboundApi->delete_stp_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**DeleteStpProtectionRequestDto**](DeleteStpProtectionRequestDto.md)| 删除交换机STP保护配置请求参数体。 | 

### Return type

[**DeleteStpProtectionResponseDto**](DeleteStpProtectionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stp_protection**
> GetStpProtectionResponseDto get_stp_protection(site_id)

查询交换机STP保护配置

## 典型场景 ##    提供查询配置参数的接口，查询交换机STP保护配置信息。 ## 接口功能 ##    查询交换机STP保护配置信息。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpProtectionNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d6151e2e' # str | 站点ID。

try: 
    # 查询交换机STP保护配置
    api_response = api_instance.get_stp_protection(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpProtectionNorthboundApi->get_stp_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**GetStpProtectionResponseDto**](GetStpProtectionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stp_protection**
> StpProtectionResponseDto update_stp_protection(site_id, body)

修改交换机STP保护配置

## 典型场景 ##    提供配置参数的接口，修改交换机STP保护配置。 ## 接口功能 ##    修改交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpProtectionNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点ID。
body = cloudcampus.StpProtectionRequestDto() # StpProtectionRequestDto | 修改交换机STP保护配置参数体。

try: 
    # 修改交换机STP保护配置
    api_response = api_instance.update_stp_protection(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpProtectionNorthboundApi->update_stp_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**StpProtectionRequestDto**](StpProtectionRequestDto.md)| 修改交换机STP保护配置参数体。 | 

### Return type

[**StpProtectionResponseDto**](StpProtectionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

