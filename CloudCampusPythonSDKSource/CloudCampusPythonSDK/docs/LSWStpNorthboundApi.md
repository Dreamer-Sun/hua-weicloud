# swagger_client.LSWStpNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](LSWStpNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswstp/sites/{siteId}/stp | 全量修改站点内交换机的STP配置
[**delete**](LSWStpNorthboundApi.md#delete) | **POST** /controller/campus/v1/networkservice/networkconfig/net/lswstp/sites/{siteId}/action/batch-delete | 删除站点内交换机的STP配置
[**get_config**](LSWStpNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/lswstp/sites/{siteId}/stp | 查询站点内交换机的STP配置
[**incre_config**](LSWStpNorthboundApi.md#incre_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswstp/sites/{siteId}/stp-increment | 增量修改站点内交换机的STP配置


# **config**
> StpResponseDto config(site_id, body)

全量修改站点内交换机的STP配置

## 典型场景 ##    提供配置参数的接口，修改交换机STP配置。 ## 接口功能 ##    全量修改交换机STP配置，不支持并发。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。
body = cloudcampus.StpDto() # StpDto | 站点内交换机的STP配置参数体。

try: 
    # 全量修改站点内交换机的STP配置
    api_response = api_instance.config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**StpDto**](StpDto.md)| 站点内交换机的STP配置参数体。 | 

### Return type

[**StpResponseDto**](StpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> StpResponseDto delete(site_id, body)

删除站点内交换机的STP配置

## 典型场景 ##    提供配置参数的接口，删除交换机MSTP配置。    1、若只传入regionId，删除对应的MSTPregion；    2、若只传入regionId和instanceId，则删除指定regionId下的instanceId对应的mstpRegionInstance；    3、若只传入regionId和deviceId，则删除指定regionId下的regionDeviceList中的deviceId，且会删除指定regionID下，所有instance下的deviceId对应的regionInstanceDevice；    4、若传入regionId、instanceId和deviceId，只删除指定regionId下指定instanceId下的regionInstanceDevice，instanceId为0的树无法删除。 ## 接口功能 ##    删除交换机STP配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。
body = cloudcampus.DelStpDto() # DelStpDto | 站点内交换机的STP配置参数体。

try: 
    # 删除站点内交换机的STP配置
    api_response = api_instance.delete(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpNorthboundApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**DelStpDto**](DelStpDto.md)| 站点内交换机的STP配置参数体。 | 

### Return type

[**StpResponseDto**](StpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> StpResponseDto get_config(site_id)

查询站点内交换机的STP配置

## 典型场景 ##    提供查询配置参数的接口，查询LSW的STP配置信息。 ## 接口功能 ##    获取STP配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。

try: 
    # 查询站点内交换机的STP配置
    api_response = api_instance.get_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**StpResponseDto**](StpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incre_config**
> StpResponseDto incre_config(site_id, body)

增量修改站点内交换机的STP配置

## 典型场景 ##    提供配置参数的接口，增量修改交换机MSTP配置，根据regionId\\instanceId\\deviceId将输入的内容进行修改，未输入的内容保持不变；若要向树中加入该域未包含的设备，需要同时将该设备加入域（regionDeviceList）中。 ## 接口功能 ##    增量修改交换机STP配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWStpNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06db151e2e' # str | 站点ID。
body = cloudcampus.IncreStpDto() # IncreStpDto | 站点内交换机的STP配置参数体。

try: 
    # 增量修改站点内交换机的STP配置
    api_response = api_instance.incre_config(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWStpNorthboundApi->incre_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **body** | [**IncreStpDto**](IncreStpDto.md)| 站点内交换机的STP配置参数体。 | 

### Return type

[**StpResponseDto**](StpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

