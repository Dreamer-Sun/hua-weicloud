# swagger_client.FloorsNorthBoundApi

All URIs are relative to *https://localhost/controller/campus/v1/indoormapservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_details_by_floor_id**](FloorsNorthBoundApi.md#get_device_details_by_floor_id) | **GET** /controller/campus/v1/indoormapservice/floors/{floorId}/devices-details | 查询楼栋中楼层已布放设备详细信息
[**get_floor_details**](FloorsNorthBoundApi.md#get_floor_details) | **GET** /controller/campus/v1/indoormapservice/floors/{floorId} | 查询楼栋中所有楼层详细信息
[**get_floor_location_details**](FloorsNorthBoundApi.md#get_floor_location_details) | **GET** /controller/campus/v1/indoormapservice/floors/{floorId}/locaion-details | 查询楼栋中楼层和设备布放信息


# **get_device_details_by_floor_id**
> QueryLocatedDeviceDetailsResponse get_device_details_by_floor_id(floor_id, device_type=device_type)

查询楼栋中楼层已布放设备详细信息

## 典型场景 ##  查询楼层已布放设备详细信息。 ## 接口功能 ##  查询楼层已布放设备详细信息，支持基于设备类型查询。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FloorsNorthBoundApi()
floor_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | 楼层ID，格式UUID。
device_type = 'device_type_example' # str | 设备类型，类型取值范围：\"AP\"，\"LSW\"，\"ALL\"。 (optional)

try: 
    # 查询楼栋中楼层已布放设备详细信息
    api_response = api_instance.get_device_details_by_floor_id(floor_id, device_type=device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloorsNorthBoundApi->get_device_details_by_floor_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floor_id** | **str**| 楼层ID，格式UUID。 | 
 **device_type** | **str**| 设备类型，类型取值范围：\&quot;AP\&quot;，\&quot;LSW\&quot;，\&quot;ALL\&quot;。 | [optional] 

### Return type

[**QueryLocatedDeviceDetailsResponse**](QueryLocatedDeviceDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_floor_details**
> QueryFloorDetailsResponse get_floor_details(floor_id)

查询楼栋中所有楼层详细信息

## 典型场景 ##  查询楼层详细信息。 ## 接口功能 ##  查询楼层详细信息，包含楼层名称，楼层号，楼层图纸和比例尺。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FloorsNorthBoundApi()
floor_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | 楼层ID，格式UUID。

try: 
    # 查询楼栋中所有楼层详细信息
    api_response = api_instance.get_floor_details(floor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloorsNorthBoundApi->get_floor_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floor_id** | **str**| 楼层ID，格式UUID。 | 

### Return type

[**QueryFloorDetailsResponse**](QueryFloorDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_floor_location_details**
> QueryFloorLocationDetailsResponse get_floor_location_details(floor_id)

查询楼栋中楼层和设备布放信息

## 典型场景 ##  查询楼层和设备布放信息。 ## 接口功能 ##  查询楼层和设备布放信息，包含楼层名称，楼层所属楼栋名称，楼层图纸，比例尺，已布放设备列表和未布放设备列表。 ## 接口约束 ##  1、只有租户管理员获取token并建立会话后才能调用该接口。  2、楼层未添加图纸时，该接口不能使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FloorsNorthBoundApi()
floor_id = '75ade72a-e7a9-4c81-8fca-894e7ca9c2c2' # str | 楼层ID，格式UUID。

try: 
    # 查询楼栋中楼层和设备布放信息
    api_response = api_instance.get_floor_location_details(floor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloorsNorthBoundApi->get_floor_location_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floor_id** | **str**| 楼层ID，格式UUID。 | 

### Return type

[**QueryFloorLocationDetailsResponse**](QueryFloorLocationDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

