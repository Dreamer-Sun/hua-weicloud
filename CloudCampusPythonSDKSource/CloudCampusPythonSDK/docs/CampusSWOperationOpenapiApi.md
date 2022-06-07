# swagger_client.CampusSWOperationOpenapiApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fan_info**](CampusSWOperationOpenapiApi.md#get_fan_info) | **GET** /controller/campus/v1/oamservice/faninfo/devices/{id}/frame/{frameNo} | 查询设备风扇信息
[**get_power_info**](CampusSWOperationOpenapiApi.md#get_power_info) | **GET** /controller/campus/v1/oamservice/powerinfo/devices/{id}/frame/{frameNo} | 查询设备电源信息
[**get_reset_reason**](CampusSWOperationOpenapiApi.md#get_reset_reason) | **GET** /controller/campus/v1/oamservice/resetreason/devices/{id}/frame/{frameNo}/board/{boardName} | 查询指定单板复位原因
[**get_system_power_info**](CampusSWOperationOpenapiApi.md#get_system_power_info) | **GET** /controller/campus/v1/oamservice/systempowerinfo/devices/{id}/frame/{frameNo} | 查询设备系统电源信息
[**power_supply**](CampusSWOperationOpenapiApi.md#power_supply) | **POST** /controller/campus/v1/oamservice/powersupply | 配置单板上下电
[**query_all_boards**](CampusSWOperationOpenapiApi.md#query_all_boards) | **GET** /controller/campus/v1/oamservice/boards/devices/{deviceId}/frame/{frameNo} | 查询插卡框式交换机单板信息
[**query_interface_detail**](CampusSWOperationOpenapiApi.md#query_interface_detail) | **GET** /controller/campus/v1/oamservice/interface/devices/{deviceId}/frame/{frameNo}/slot/{slotNo} | 查询单板接口信息
[**reset_board**](CampusSWOperationOpenapiApi.md#reset_board) | **POST** /controller/campus/v1/oamservice/reset/devices/{id}/frame/{frameNo}/board/{boardName} | 复位单板
[**reset_chassis**](CampusSWOperationOpenapiApi.md#reset_chassis) | **PUT** /controller/campus/v1/oamservice/resetchassis/devices/{deviceId}/frame/{frameNo} | 框式交换机整框重启
[**switchover**](CampusSWOperationOpenapiApi.md#switchover) | **PUT** /controller/campus/v1/oamservice/switchover/{deviceId} | 框式交换机主备倒换


# **get_fan_info**
> GetFanInfoOutputDto get_fan_info(id, frame_no)

查询设备风扇信息

## 典型场景 ##   查询设备风扇信息，支持堆叠设备风扇查询。 ## 接口功能 ##   查询设备风扇信息。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
id = '00000000-0000-0000-0000-000000000000' # str | 设备ID，UUID格式。
frame_no = 1 # int | 机框号。

try: 
    # 查询设备风扇信息
    api_response = api_instance.get_fan_info(id, frame_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->get_fan_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 设备ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 

### Return type

[**GetFanInfoOutputDto**](GetFanInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_info**
> GetPowerInfoOutputDto get_power_info(id, frame_no)

查询设备电源信息

## 典型场景 ##   查询设备电源信息，支持查询堆叠设备的电源信息。 ## 接口功能 ##   查询设备电源信息。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
id = '00000000-0000-0000-0000-000000000000' # str | 设备ID，UUID格式。
frame_no = 1 # int | 机框号。

try: 
    # 查询设备电源信息
    api_response = api_instance.get_power_info(id, frame_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->get_power_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 设备ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 

### Return type

[**GetPowerInfoOutputDto**](GetPowerInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reset_reason**
> GetResetReasonOutputDto get_reset_reason(id, frame_no, board_name)

查询指定单板复位原因

## 典型场景 ##   查询指定单板复位原因。 ## 接口功能 ##   查询指定单板复位原因。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
id = '00000000-0000-0000-0000-000000000000' # str | 设备ID，UUID格式。
frame_no = 1 # int | 机框号。
board_name = '8' # str | 槽位名称。

try: 
    # 查询指定单板复位原因
    api_response = api_instance.get_reset_reason(id, frame_no, board_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->get_reset_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 设备ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 
 **board_name** | **str**| 槽位名称。 | 

### Return type

[**GetResetReasonOutputDto**](GetResetReasonOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_power_info**
> GetSystemPowerInfoOutputDto get_system_power_info(id, frame_no)

查询设备系统电源信息

## 典型场景 ##   查询设备系统电源信息，支持查询堆叠设备的系统电源信息。 ## 接口功能 ##   查询设备系统电源信息。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
id = '00000000-0000-0000-0000-000000000000' # str | 设备ID，UUID格式。
frame_no = 1 # int | 机框号。

try: 
    # 查询设备系统电源信息
    api_response = api_instance.get_system_power_info(id, frame_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->get_system_power_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 设备ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 

### Return type

[**GetSystemPowerInfoOutputDto**](GetSystemPowerInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **power_supply**
> PowerSupplyOutputDto power_supply(request)

配置单板上下电

## 典型场景 ##   根据设备ID和单板名称，给指定单板上下电。 ## 接口功能 ##   配置单板上下电。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
request = cloudcampus.PowerSupplyDto() # PowerSupplyDto | 请求参数。

try: 
    # 配置单板上下电
    api_response = api_instance.power_supply(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->power_supply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PowerSupplyDto**](PowerSupplyDto.md)| 请求参数。 | 

### Return type

[**PowerSupplyOutputDto**](PowerSupplyOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_all_boards**
> BoardsInfoOutputDto query_all_boards(device_id, frame_no)

查询插卡框式交换机单板信息

## 典型场景 ##    提供查询框式交换机单板信息接口。 ## 接口功能 ##    基于单板维度查询框式交换机单板信息。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID或堆叠ID，UUID格式。
frame_no = 1 # int | 机框号。

try: 
    # 查询插卡框式交换机单板信息
    api_response = api_instance.query_all_boards(device_id, frame_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->query_all_boards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID或堆叠ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 

### Return type

[**BoardsInfoOutputDto**](BoardsInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_interface_detail**
> InterfacesInfoOutputDto query_interface_detail(device_id, frame_no, slot_no)

查询单板接口信息

## 典型场景 ##    根据设备ID和槽位号，查询单板接口信息。 ## 接口功能 ##    基于单板维度查询接口信息。 ## 接口约束 ##    该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID或堆叠ID， UUID格式。
frame_no = 1 # int | 机框号。
slot_no = 1 # int | 单板索引号，槽位号。

try: 
    # 查询单板接口信息
    api_response = api_instance.query_interface_detail(device_id, frame_no, slot_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->query_interface_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID或堆叠ID， UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 
 **slot_no** | **int**| 单板索引号，槽位号。 | 

### Return type

[**InterfacesInfoOutputDto**](InterfacesInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_board**
> ResetBoardOutputDto reset_board(id, frame_no, board_name)

复位单板

## 典型场景 ##   根据设备ID和单板名称，复位指定单板。 ## 接口功能 ##   复位单板。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
id = '00000000-0000-0000-0000-000000000000' # str | 设备ID，UUID格式。
frame_no = 1 # int | 机框号。
board_name = '8' # str | 槽位名称。

try: 
    # 复位单板
    api_response = api_instance.reset_board(id, frame_no, board_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->reset_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 设备ID，UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 
 **board_name** | **str**| 槽位名称。 | 

### Return type

[**ResetBoardOutputDto**](ResetBoardOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_chassis**
> ResetChassisOutputDto reset_chassis(device_id, frame_no)

框式交换机整框重启

## 典型场景 ##    框式交换机整框重启。 ## 接口功能 ##    框式整框重启。 ## 接口约束 ##    北向接口管理员可以访问。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID或堆叠ID， UUID格式。
frame_no = 1 # int | 机框号。

try: 
    # 框式交换机整框重启
    api_response = api_instance.reset_chassis(device_id, frame_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->reset_chassis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID或堆叠ID， UUID格式。 | 
 **frame_no** | **int**| 机框号。 | 

### Return type

[**ResetChassisOutputDto**](ResetChassisOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switchover**
> SwitchoverOutputDto switchover(device_id)

框式交换机主备倒换

## 典型场景 ##    框式交换机主备倒换。 ## 接口功能 ##    框式或者框式堆叠主备倒换。 ## 接口约束 ##    北向接口管理员可以访问。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.CampusSWOperationOpenapiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 设备ID或者堆叠ID， UUID格式。

try: 
    # 框式交换机主备倒换
    api_response = api_instance.switchover(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampusSWOperationOpenapiApi->switchover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID或者堆叠ID， UUID格式。 | 

### Return type

[**SwitchoverOutputDto**](SwitchoverOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

