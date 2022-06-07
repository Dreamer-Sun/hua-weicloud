# swagger_client.TopoMgrServiceApi

All URIs are relative to *https://localhost/controller/campus/v1/networkresource/topomanager*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lacp_lag_info**](TopoMgrServiceApi.md#get_lacp_lag_info) | **GET** /controller/campus/v1/networkresource/topomanager/device/{deviceId}/ethtrunk | 查询LACP LAG信息
[**get_neighbors_info**](TopoMgrServiceApi.md#get_neighbors_info) | **GET** /controller/campus/v1/networkresource/topomanager/device/{deviceId}/neighbors | 查询LLDP信息


# **get_lacp_lag_info**
> LacpLagInfoResultDto get_lacp_lag_info(device_id)

查询LACP LAG信息

## 典型场景 ##  根据设备ID查询LACP LAG信息。 ## 接口功能 ##  查询LACP LAG信息。 ## 接口约束 ##  1、当前仅LSW支持该接口。  2、该接口必须在用户会话建立后使用。  3、该接口需从设备查询信息，数据量大时会导致查询响应慢。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TopoMgrServiceApi()
device_id = 'd4e8513d-69f7-41bb-a3f5-b3a0fcc7b6e0' # str | 设备ID，UUID格式。

try: 
    # 查询LACP LAG信息
    api_response = api_instance.get_lacp_lag_info(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopoMgrServiceApi->get_lacp_lag_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 

### Return type

[**LacpLagInfoResultDto**](LacpLagInfoResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_neighbors_info**
> NeighborsInfoResultDto get_neighbors_info(device_id, local_if_name=local_if_name, page_index=page_index, page_size=page_size)

查询LLDP信息

## 典型场景 ##  根据设备ID查询LLDP信息。 ## 接口功能 ##  查询LLDP信息。 ## 接口约束 ##  1、当前仅LSW和云AP支持该接口。  2、该接口必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TopoMgrServiceApi()
device_id = 'd4e8513d-69f7-41bb-a3f5-b3a0fcc7b6e0' # str | 设备ID，UUID格式。
local_if_name = 'GigabitEthernet0/0/0' # str | 本端接口名称，值为空时表示查询该设备所有接口的LLDP连接。 (optional)
page_index = 0 # int | 分页时，当前页面索引，值<=0时表示获取所有数据。 (optional) (default to 0)
page_size = 20 # int | 分页时，当前页面设备数据长度；pageIndex为空或<=0时，此参数无意义。 (optional) (default to 20)

try: 
    # 查询LLDP信息
    api_response = api_instance.get_neighbors_info(device_id, local_if_name=local_if_name, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopoMgrServiceApi->get_neighbors_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID，UUID格式。 | 
 **local_if_name** | **str**| 本端接口名称，值为空时表示查询该设备所有接口的LLDP连接。 | [optional] 
 **page_index** | **int**| 分页时，当前页面索引，值&lt;&#x3D;0时表示获取所有数据。 | [optional] [default to 0]
 **page_size** | **int**| 分页时，当前页面设备数据长度；pageIndex为空或&lt;&#x3D;0时，此参数无意义。 | [optional] [default to 20]

### Return type

[**NeighborsInfoResultDto**](NeighborsInfoResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

