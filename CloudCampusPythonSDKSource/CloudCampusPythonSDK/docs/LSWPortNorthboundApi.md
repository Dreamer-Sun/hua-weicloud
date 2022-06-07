# swagger_client.LSWPortNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config**](LSWPortNorthboundApi.md#config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethernet-ports | 修改交换机端口配置
[**create_eth_trunk**](LSWPortNorthboundApi.md#create_eth_trunk) | **POST** /controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports | 创建交换机EthTrunk端口
[**delete_eth_trunk**](LSWPortNorthboundApi.md#delete_eth_trunk) | **DELETE** /controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports/{name} | 删除交换机EthTrunk端口
[**get_config**](LSWPortNorthboundApi.md#get_config) | **GET** /controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ports | 查询交换机端口配置
[**update_eth_trunk**](LSWPortNorthboundApi.md#update_eth_trunk) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports/{name} | 修改交换机EthTrunk端口


# **config**
> PutResponseDto config(device_id, body)

修改交换机端口配置

## 典型场景 ##    提供配置参数的接口，修改交换机以太端口配置。 ## 接口功能 ##    修改交换机以太端口配置，支持同时配置多个端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWPortNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。
body = [cloudcampus.LSWEthPortDto()] # list[LSWEthPortDto] | 交换机以太端口配置参数体。

try: 
    # 修改交换机端口配置
    api_response = api_instance.config(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWPortNorthboundApi->config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **body** | [**list[LSWEthPortDto]**](LSWEthPortDto.md)| 交换机以太端口配置参数体。 | 

### Return type

[**PutResponseDto**](PutResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_eth_trunk**
> EthTrunkResponseDto create_eth_trunk(device_id, body)

创建交换机EthTrunk端口

## 典型场景 ##    提供配置参数的接口，创建交换机EthTrunk端口。 ## 接口功能 ##    创建交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWPortNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。
body = cloudcampus.LSWEthTrunkPortDto() # LSWEthTrunkPortDto | 创建交换机EthTrunk端口参数体。

try: 
    # 创建交换机EthTrunk端口
    api_response = api_instance.create_eth_trunk(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWPortNorthboundApi->create_eth_trunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **body** | [**LSWEthTrunkPortDto**](LSWEthTrunkPortDto.md)| 创建交换机EthTrunk端口参数体。 | 

### Return type

[**EthTrunkResponseDto**](EthTrunkResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_eth_trunk**
> ResponseDto delete_eth_trunk(device_id, name)

删除交换机EthTrunk端口

## 典型场景 ##    提供配置参数的接口，删除交换机EthTrunk端口。 ## 接口功能 ##    删除交换机EthTrunk端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWPortNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。
name = 'Eth-Trunk0' # str | EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。

try: 
    # 删除交换机EthTrunk端口
    api_response = api_instance.delete_eth_trunk(device_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWPortNorthboundApi->delete_eth_trunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **name** | **str**| EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 | 

### Return type

[**ResponseDto**](ResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> GetResponseDto get_config(device_id)

查询交换机端口配置

## 典型场景 ##    提供查询配置参数的接口，查询交换机端口配置。 ## 接口功能 ##    查询交换机端口配置（包括以太口和EthTrunk口）。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWPortNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。

try: 
    # 查询交换机端口配置
    api_response = api_instance.get_config(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWPortNorthboundApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 

### Return type

[**GetResponseDto**](GetResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_eth_trunk**
> EthTrunkResponseDto update_eth_trunk(device_id, name, body)

修改交换机EthTrunk端口

## 典型场景 ##    提供配置参数的接口，修改交换机EthTrunk端口。 ## 接口功能 ##    修改交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LSWPortNorthboundApi()
device_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 设备ID。
name = 'Eth-Trunk0' # str | EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。
body = cloudcampus.LSWEthTrunkPortDto() # LSWEthTrunkPortDto | 修改交换机EthTrunk端口参数体。

try: 
    # 修改交换机EthTrunk端口
    api_response = api_instance.update_eth_trunk(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LSWPortNorthboundApi->update_eth_trunk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **name** | **str**| EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 | 
 **body** | [**LSWEthTrunkPortDto**](LSWEthTrunkPortDto.md)| 修改交换机EthTrunk端口参数体。 | 

### Return type

[**EthTrunkResponseDto**](EthTrunkResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

