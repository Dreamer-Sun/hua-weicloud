# swagger_client.ApIotCardOpenapiApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**card_operation**](ApIotCardOpenapiApi.md#card_operation) | **POST** /controller/campus/v1/oamservice/apiot/card/operation | 操作AP网口IOT插卡
[**exec_iot_command**](ApIotCardOpenapiApi.md#exec_iot_command) | **POST** /controller/campus/v1/oamservice/apiot/cmd | 给IOT插卡下命令
[**query_ethernet_card_list**](ApIotCardOpenapiApi.md#query_ethernet_card_list) | **GET** /controller/campus/v1/oamservice/apiot/ethernetcardlist/sites/{siteId} | 查询AP网口IOT插卡
[**query_iot_command_result**](ApIotCardOpenapiApi.md#query_iot_command_result) | **GET** /controller/campus/v1/oamservice/apiot/cmd/result/{siteId} | 查询AP IOT命令下发的状态


# **card_operation**
> CardOperationOutputDto card_operation(request_dto)

操作AP网口IOT插卡

## 典型场景 ##   操作插卡。 ## 接口功能 ##   对插卡进行重启、重置网络配置等操作。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIotCardOpenapiApi()
request_dto = cloudcampus.IotCardOperationDto() # IotCardOperationDto | IOT插卡信息。

try: 
    # 操作AP网口IOT插卡
    api_response = api_instance.card_operation(request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIotCardOpenapiApi->card_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_dto** | [**IotCardOperationDto**](IotCardOperationDto.md)| IOT插卡信息。 | 

### Return type

[**CardOperationOutputDto**](CardOperationOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exec_iot_command**
> OpenApIotCommandOut exec_iot_command(ap_iot_open_comman_in)

给IOT插卡下命令

## 典型场景 ##   给IOT插卡下命令。 ## 接口功能 ##   对单个或者多个插卡进行下发CMD命令等操作。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIotCardOpenapiApi()
ap_iot_open_comman_in = cloudcampus.OpenApIotCommandIn() # OpenApIotCommandIn | IOT命令下发结构体

try: 
    # 给IOT插卡下命令
    api_response = api_instance.exec_iot_command(ap_iot_open_comman_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIotCardOpenapiApi->exec_iot_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_iot_open_comman_in** | [**OpenApIotCommandIn**](OpenApIotCommandIn.md)| IOT命令下发结构体 | 

### Return type

[**OpenApIotCommandOut**](OpenApIotCommandOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_ethernet_card_list**
> EthernetCardOutputDto query_ethernet_card_list(site_id, keyword=keyword, page_size=page_size, page_index=page_index)

查询AP网口IOT插卡

## 典型场景 ##   查询AP网口IOT插卡列表。 ## 接口功能 ##   查询AP网口IOT插卡列表。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIotCardOpenapiApi()
site_id = '00000000-0000-0000-0000-000000000000' # str | 站点ID，UUID格式。
keyword = '123' # str | 搜索关键字。匹配字段：设备ESN，是否必填：否。 (optional)
page_size = 20 # int | 每页展示数量。是否必填：否。 (optional)
page_index = 1 # int | 页面索引。是否必填：否。 (optional)

try: 
    # 查询AP网口IOT插卡
    api_response = api_instance.query_ethernet_card_list(site_id, keyword=keyword, page_size=page_size, page_index=page_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIotCardOpenapiApi->query_ethernet_card_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **keyword** | **str**| 搜索关键字。匹配字段：设备ESN，是否必填：否。 | [optional] 
 **page_size** | **int**| 每页展示数量。是否必填：否。 | [optional] 
 **page_index** | **int**| 页面索引。是否必填：否。 | [optional] 

### Return type

[**EthernetCardOutputDto**](EthernetCardOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_iot_command_result**
> QueryCmdResultOut query_iot_command_result(site_id, page_size, page_index, keyword=keyword)

查询AP IOT命令下发的状态

## 典型场景 ##   查询AP IOT命令下发的状态。 ## 接口功能 ##   查询AP IOT命令下发的状态，只返回最新一次下发结果。 ## 接口约束 ##   该接口支持租户下北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.ApIotCardOpenapiApi()
site_id = '00000000-0000-0000-0000-000000000000' # str | 站点ID，UUID格式。
page_size = 20 # int | 每页展示数量。
page_index = 1 # int | 页面索引。
keyword = '123' # str | 搜索关键字。模糊匹配字段：设备名称、设备ESN。 (optional)

try: 
    # 查询AP IOT命令下发的状态
    api_response = api_instance.query_iot_command_result(site_id, page_size, page_index, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApIotCardOpenapiApi->query_iot_command_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **page_size** | **int**| 每页展示数量。 | 
 **page_index** | **int**| 页面索引。 | 
 **keyword** | **str**| 搜索关键字。模糊匹配字段：设备名称、设备ESN。 | [optional] 

### Return type

[**QueryCmdResultOut**](QueryCmdResultOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

