# swagger_client.PerformanceOpenApiApi

All URIs are relative to *https://localhost/controller/campus/v1/performanceservice/basicperformance*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_device_count_trend**](PerformanceOpenApiApi.md#query_device_count_trend) | **GET** /controller/campus/v1/performanceservice/basicperformance/devicecounttrend | 查询租户维度下设备状态历史数据列表
[**query_device_station_statistic**](PerformanceOpenApiApi.md#query_device_station_statistic) | **GET** /controller/campus/v1/performanceservice/basicperformance/station/device/{deviceId} | 查询设备连接终端数历史数据
[**query_device_traffic**](PerformanceOpenApiApi.md#query_device_traffic) | **GET** /controller/campus/v1/performanceservice/basicperformance/devicetraffic/statistic/site/{siteId} | 查询站点维度TopN设备或者全部设备的上行流量、下行流量
[**query_network_traffic**](PerformanceOpenApiApi.md#query_network_traffic) | **GET** /controller/campus/v1/performanceservice/basicperformance/networktraffic | 查询设备网络速率历史数据
[**query_site_health_list**](PerformanceOpenApiApi.md#query_site_health_list) | **GET** /controller/campus/v1/performanceservice/basicperformance/siteshealth/{siteId} | 基于站点的站点健康度查询
[**query_site_station_statistic**](PerformanceOpenApiApi.md#query_site_station_statistic) | **GET** /controller/campus/v1/performanceservice/basicperformance/station/sites/{siteId} | 查询站点维度设备连接终端数历史数据
[**query_top_nssid_traffic**](PerformanceOpenApiApi.md#query_top_nssid_traffic) | **GET** /controller/campus/v1/performanceservice/basicperformance/topnssidtraffic/{siteId} | 查询TOP N SSID流量和最近在线用户数
[**single_device_performance_detail**](PerformanceOpenApiApi.md#single_device_performance_detail) | **GET** /controller/campus/v1/performanceservice/basicperformance/device/{deviceId} | 查询单设备的性能数据


# **query_device_count_trend**
> DeviceCountTrendResp query_device_count_trend(mode, time_dimension, begin_time, end_time)

查询租户维度下设备状态历史数据列表

## 典型场景 ##    提供查询租户维度下设备状态历史数据             ## 接口功能 ##    查询租户维度下设备状态历史数据 ## 接口约束 ##    无。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
mode = 'tenant' # str | 查询维度，tenant---租户。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。

try: 
    # 查询租户维度下设备状态历史数据列表
    api_response = api_instance.query_device_count_trend(mode, time_dimension, begin_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_device_count_trend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| 查询维度，tenant---租户。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 

### Return type

[**DeviceCountTrendResp**](DeviceCountTrendResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_device_station_statistic**
> DeviceStationStatisticResp query_device_station_statistic(device_id, time_dimension, begin_time, end_time)

查询设备连接终端数历史数据

## 典型场景 ##    提供查询设备连接终端数历史数据的接口。 ## 接口功能 ##    支持查询设备连接终端数历史数据。 ## 接口约束 ##    无。   

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 设备ID。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月、year---年。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。

try: 
    # 查询设备连接终端数历史数据
    api_response = api_instance.query_device_station_statistic(device_id, time_dimension, begin_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_device_station_statistic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月、year---年。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 

### Return type

[**DeviceStationStatisticResp**](DeviceStationStatisticResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_device_traffic**
> DeviceTrafficStatisticResp query_device_traffic(site_id, time_dimension, top, begin_time, end_time)

查询站点维度TopN设备或者全部设备的上行流量、下行流量

## 典型场景 ##    提供查询站点维度TopN设备或者全部设备的上行流量、下行流量的接口。           ## 接口功能 ##    支持查询站点维度TopN设备或者全部设备的上行流量、下行流量。 ## 接口约束 ##    无。   

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月、year---年。
top = 5 # int | top数据个数，支持0、5、10、15、20。0代表查询全部设备的上下行流量。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。

try: 
    # 查询站点维度TopN设备或者全部设备的上行流量、下行流量
    api_response = api_instance.query_device_traffic(site_id, time_dimension, top, begin_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_device_traffic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月、year---年。 | 
 **top** | **int**| top数据个数，支持0、5、10、15、20。0代表查询全部设备的上下行流量。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 

### Return type

[**DeviceTrafficStatisticResp**](DeviceTrafficStatisticResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_network_traffic**
> NetworkTrafficResp query_network_traffic(mode, id, time_dimension, begin_time, end_time)

查询设备网络速率历史数据

## 典型场景 ##    提供查询设备网络速率历史数据的接口。           ## 接口功能 ##    查询设备网络速率历史数据。 ## 接口约束 ##    无。   

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
mode = 'device' # str | 查询维度，device---设备、site---站点。
id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | mode为device时该ID为设备ID，mode为site时，该ID为站点ID。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。

try: 
    # 查询设备网络速率历史数据
    api_response = api_instance.query_network_traffic(mode, id, time_dimension, begin_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_network_traffic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| 查询维度，device---设备、site---站点。 | 
 **id** | **str**| mode为device时该ID为设备ID，mode为site时，该ID为站点ID。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 

### Return type

[**NetworkTrafficResp**](NetworkTrafficResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_site_health_list**
> SiteHealthOutputDto query_site_health_list(site_id)

基于站点的站点健康度查询

## 典型场景 ##    根据设备健康度和射频健康度来计算站点健康度。 ## 接口功能 ##    查询基于站点的站点健康度。 ## 接口约束 ##    该接口支持租户下北向管理员（用户角色为“Open Api Operator”）访问，必须在用户会话建立后使用。     

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
site_id = '5cd2d350-b530-4469-8df6-4e5b6c70ff6d' # str | 站点ID。

try: 
    # 基于站点的站点健康度查询
    api_response = api_instance.query_site_health_list(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_site_health_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 

### Return type

[**SiteHealthOutputDto**](SiteHealthOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_site_station_statistic**
> SiteStationStatisticResp query_site_station_statistic(site_id, time_dimension, begin_time, end_time, device_type)

查询站点维度设备连接终端数历史数据

## 典型场景 ##    提供查询站点维度设备连接终端数历史数据的接口。           ## 接口功能 ##    支持查询站点维度设备连接终端数历史数据。 ## 接口约束 ##    无。   

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
time_dimension = 'day' # str | 统计周期，day---天、week---周、month---月、year---年。
begin_time = 1537408636 # int | 起始格林威治时间（时间精度对应到秒）。
end_time = 1537495036 # int | 结束格林威治时间（时间精度对应到秒）。
device_type = 'AP' # str | 查询过滤的设备类型，AP---AP设备、FW---FW设备、AC---AC（Fit AP）设备、ALL---所有设备。

try: 
    # 查询站点维度设备连接终端数历史数据
    api_response = api_instance.query_site_station_statistic(site_id, time_dimension, begin_time, end_time, device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_site_station_statistic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **time_dimension** | **str**| 统计周期，day---天、week---周、month---月、year---年。 | 
 **begin_time** | **int**| 起始格林威治时间（时间精度对应到秒）。 | 
 **end_time** | **int**| 结束格林威治时间（时间精度对应到秒）。 | 
 **device_type** | **str**| 查询过滤的设备类型，AP---AP设备、FW---FW设备、AC---AC（Fit AP）设备、ALL---所有设备。 | 

### Return type

[**SiteStationStatisticResp**](SiteStationStatisticResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_top_nssid_traffic**
> TopNSSIDTrafficListDto query_top_nssid_traffic(site_id, begin_time, end_time, time_granularity, top, device_type)

查询TOP N SSID流量和最近在线用户数

## 典型场景 ##    提供站点下TOP N SSID流量和最近在线用户数的查询。 ## 接口功能 ##    查询站点下TOP N SSID流量和最近在线用户数。 ## 接口约束 ##    该接口支持租户下北向管理员（用户角色为“Open Api Operator”）访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
site_id = '5cd2d350-b530-4469-8df6-4e5b6c70ff6d' # str | 站点ID。
begin_time = 1568044800561 # int | 起始格林威治时间(毫秒)。
end_time = 1568044800561 # int | 结束格林威治时间(毫秒)。
time_granularity = 'day' # str | 统计周期，day---天、week---周、month---月、year---年。
top = '5' # str | top数据个数，取值范围：5、10、15、20。5 - 代表TOP 5、10 - 代表TOP 10、15 - 代表TOP 15、20 - 代表TOP 20。
device_type = '1' # str | 设备类型，取值范围：0、1、6。0-代表全部设备，1-代表AP，6-代表WAC。

try: 
    # 查询TOP N SSID流量和最近在线用户数
    api_response = api_instance.query_top_nssid_traffic(site_id, begin_time, end_time, time_granularity, top, device_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->query_top_nssid_traffic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **begin_time** | **int**| 起始格林威治时间(毫秒)。 | 
 **end_time** | **int**| 结束格林威治时间(毫秒)。 | 
 **time_granularity** | **str**| 统计周期，day---天、week---周、month---月、year---年。 | 
 **top** | **str**| top数据个数，取值范围：5、10、15、20。5 - 代表TOP 5、10 - 代表TOP 10、15 - 代表TOP 15、20 - 代表TOP 20。 | 
 **device_type** | **str**| 设备类型，取值范围：0、1、6。0-代表全部设备，1-代表AP，6-代表WAC。 | 

### Return type

[**TopNSSIDTrafficListDto**](TopNSSIDTrafficListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **single_device_performance_detail**
> DevicePerformanceResp single_device_performance_detail(device_id)

查询单设备的性能数据

## 典型场景 ##  查询单个设备基本信息、总流量以及最近一次设备上报的终端连接数、CPU利用率、上行速率、下行速率。           ## 接口功能 ##  单个设备基本信息、总流量以及最近一次设备上报的终端连接数、CPU利用率、上行速率、下行速率。 ## 接口约束 ##  无。   

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PerformanceOpenApiApi()
device_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 设备ID。

try: 
    # 查询单设备的性能数据
    api_response = api_instance.single_device_performance_detail(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceOpenApiApi->single_device_performance_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| 设备ID。 | 

### Return type

[**DevicePerformanceResp**](DevicePerformanceResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

