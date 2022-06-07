# swagger_client.StationOpenApiApi

All URIs are relative to *https://localhost/controller/campus/v1/performanceservice/station*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_device_station_info**](StationOpenApiApi.md#query_device_station_info) | **GET** /controller/campus/v1/performanceservice/station/client/device/{deviceId} | 查询设备维度下终端用户信息
[**query_site_station_info**](StationOpenApiApi.md#query_site_station_info) | **GET** /controller/campus/v1/performanceservice/station/client/site/{siteId} | 查询站点维度下终端用户信息
[**query_traffic_statistic_info**](StationOpenApiApi.md#query_traffic_statistic_info) | **GET** /controller/campus/v1/performanceservice/station/traffic/statistic/site/{siteId} | 查询站点维度下TopN终端流量数据


# **query_device_station_info**
> StationDataResp query_device_station_info(device_id, page_index, page_size, status=status, terminal_mac=terminal_mac, terminal_ip=terminal_ip, ssid=ssid, sort_key=sort_key, account=account)

查询设备维度下终端用户信息

## 典型场景 ##    设备维度下终端用户信息查询接口。 ## 接口功能 ##    基于单设备查询用户列表。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.StationOpenApiApi()
device_id = 'b473118d-17ff-4f4f-9fa9-a4c0e1e87e42' # str | 设备ID。
page_index = 1 # int | 分页查询的页码。
page_size = 20 # int | 分页查询每页数量。
status = 'status_example' # str | 用户在线状态，online---在线、offline---离线，不填代表查询全部状态。 (optional)
terminal_mac = 'b006-000a-69f5' # str | 终端MAC，需要符合mac地址的格式，例如B0:06:00:0A:69:F5，需要区分大小写字母。 (optional)
terminal_ip = '192.168.1.2' # str | 终端IP，需要符合IP地址的格式，例如192.168.1.2。 (optional)
ssid = 'wifi' # str | WiFi名。 (optional)
sort_key = '+accessTime' # str | 排序列，所有支持accessTime/accessType/account/ap/authType/channel/cumulativeTraffic/downwardSpeed/dualFrequency/frequencyBand/hostName/mode/onlineStatus/onlineTime/packageLossRate/retransRate/rssi/sendPackageSpeed/signalNoiseRatio/ssid/stickyTags/terminalIP/terminalMac/timeStamp/upwardSpeed/vlan均支持排序。如：+accessTime:按accesstime升序，-accessTime:按accessTime降序。 (optional)
account = 'test' # str | 用户名。 (optional)

try: 
    # 查询设备维度下终端用户信息
    api_response = api_instance.query_device_station_info(device_id, page_index, page_size, status=status, terminal_mac=terminal_mac, terminal_ip=terminal_ip, ssid=ssid, sort_key=sort_key, account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationOpenApiApi->query_device_station_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **page_index** | **int**| 分页查询的页码。 | 
 **page_size** | **int**| 分页查询每页数量。 | 
 **status** | **str**| 用户在线状态，online---在线、offline---离线，不填代表查询全部状态。 | [optional] 
 **terminal_mac** | **str**| 终端MAC，需要符合mac地址的格式，例如B0:06:00:0A:69:F5，需要区分大小写字母。 | [optional] 
 **terminal_ip** | **str**| 终端IP，需要符合IP地址的格式，例如192.168.1.2。 | [optional] 
 **ssid** | **str**| WiFi名。 | [optional] 
 **sort_key** | **str**| 排序列，所有支持accessTime/accessType/account/ap/authType/channel/cumulativeTraffic/downwardSpeed/dualFrequency/frequencyBand/hostName/mode/onlineStatus/onlineTime/packageLossRate/retransRate/rssi/sendPackageSpeed/signalNoiseRatio/ssid/stickyTags/terminalIP/terminalMac/timeStamp/upwardSpeed/vlan均支持排序。如：+accessTime:按accesstime升序，-accessTime:按accessTime降序。 | [optional] 
 **account** | **str**| 用户名。 | [optional] 

### Return type

[**StationDataResp**](StationDataResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_site_station_info**
> StationDataResp query_site_station_info(site_id, page_index, page_size, status=status, terminal_mac=terminal_mac, terminal_ip=terminal_ip, ssid=ssid, sort_key=sort_key, account=account)

查询站点维度下终端用户信息

## 典型场景 ##    提供站点维度查询终端用户信息列表的接口。 ## 接口功能 ##    基于站点查询终端用户列表。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.StationOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
page_index = 1 # int | 分页查询的页码。
page_size = 20 # int | 分页查询每页数量。
status = 'status_example' # str | 用户在线状态，online---在线、offline---离线，不填代表查询全部状态。 (optional)
terminal_mac = 'B0:06:00:0A:69:F5' # str | 终端MAC，需要符合MAC地址的格式，例如B0:06:00:0A:69:F5，需要区分大小写字母。 (optional)
terminal_ip = '192.168.1.2' # str | 终端IP，需要符合IP地址的格式，例如192.168.1.2。 (optional)
ssid = 'wifi' # str | SSID名称。 (optional)
sort_key = '+accessTime' # str | 排序字段名称以及排序方式。支持按如下字段之一排序：accessTime/accessType/account/deviceName/authType/channel/cumulativeTraffic/downwardSpeed/dualFrequency/frequencyBand/hostName/mode/onlineStatus/onlineTime/packageLossRate/retransRate/rssi/sendPackageSpeed/signalNoiseRatio/ssid/stickyTags/terminalIP/terminalMac/timeStamp/upwardSpeed/vlan。如：+accessTime:按accesstime升序，-accessTime:按accessTime降序。 (optional)
account = 'user1' # str | 用户名称。 (optional)

try: 
    # 查询站点维度下终端用户信息
    api_response = api_instance.query_site_station_info(site_id, page_index, page_size, status=status, terminal_mac=terminal_mac, terminal_ip=terminal_ip, ssid=ssid, sort_key=sort_key, account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationOpenApiApi->query_site_station_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **page_index** | **int**| 分页查询的页码。 | 
 **page_size** | **int**| 分页查询每页数量。 | 
 **status** | **str**| 用户在线状态，online---在线、offline---离线，不填代表查询全部状态。 | [optional] 
 **terminal_mac** | **str**| 终端MAC，需要符合MAC地址的格式，例如B0:06:00:0A:69:F5，需要区分大小写字母。 | [optional] 
 **terminal_ip** | **str**| 终端IP，需要符合IP地址的格式，例如192.168.1.2。 | [optional] 
 **ssid** | **str**| SSID名称。 | [optional] 
 **sort_key** | **str**| 排序字段名称以及排序方式。支持按如下字段之一排序：accessTime/accessType/account/deviceName/authType/channel/cumulativeTraffic/downwardSpeed/dualFrequency/frequencyBand/hostName/mode/onlineStatus/onlineTime/packageLossRate/retransRate/rssi/sendPackageSpeed/signalNoiseRatio/ssid/stickyTags/terminalIP/terminalMac/timeStamp/upwardSpeed/vlan。如：+accessTime:按accesstime升序，-accessTime:按accessTime降序。 | [optional] 
 **account** | **str**| 用户名称。 | [optional] 

### Return type

[**StationDataResp**](StationDataResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_traffic_statistic_info**
> TrafficStatisticDataResp query_traffic_statistic_info(site_id, device_type, time_dimension, top, begin_time, end_time)

查询站点维度下TopN终端流量数据

## 典型场景 ##    提供查询指定站点的按照终端流量大小的Top N终端数据。 ## 接口功能 ##    基于站点查询TopN终端流量数据。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.StationOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
device_type = 'AP' # str | 查询过滤的设备类型，AP---AP设备、FW---FW设备、AC---AC（Fit AP）设备、ALL---所有设备。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月、year---年。
top = 5 # int | top数据个数，支持0、5、10、15、20。0代表查询所有终端流量。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。

try: 
    # 查询站点维度下TopN终端流量数据
    api_response = api_instance.query_traffic_statistic_info(site_id, device_type, time_dimension, top, begin_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationOpenApiApi->query_traffic_statistic_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **device_type** | **str**| 查询过滤的设备类型，AP---AP设备、FW---FW设备、AC---AC（Fit AP）设备、ALL---所有设备。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月、year---年。 | 
 **top** | **int**| top数据个数，支持0、5、10、15、20。0代表查询所有终端流量。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 

### Return type

[**TrafficStatisticDataResp**](TrafficStatisticDataResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

