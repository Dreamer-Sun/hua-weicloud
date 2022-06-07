# swagger_client.LogManagerServiceNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_log_data**](LogManagerServiceNorthboundApi.md#query_log_data) | **GET** /controller/campus/v1/oamservice/devicelog | 查询设备上报日志记录


# **query_log_data**
> QueryResponse query_log_data(page_size, site_id, begin_time, end_time, start_query_row_key=start_query_row_key, scene_name=scene_name, device_mac=device_mac, station_mac=station_mac)

查询设备上报日志记录

## 典型场景 ##   查询设备上报日志记录。 ## 接口功能 ##   查询设备上报日志记录。 ## 接口约束 ##   只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LogManagerServiceNorthboundApi()
page_size = 10 # int | 当页大小。
site_id = '2682da07-fc14-4866-950b-fad73172a4c6' # str | 站点ID，UUID格式。
begin_time = 1541561948 # int | 起始格林威治时间，起始与结束时间不可大于5天。
end_time = 1541561948 # int | 结束时间格林威治时间，起始与结束时间不可大于5天。
start_query_row_key = '0,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,91,87,38,38,65,65,58,65,65,58,65,65,58,48,48,58,50,48,58,52,53,102,102,53,97,48,48,48,48,32,32,32,32,32,32,52,102,48,50,53,48,98,55,97,97,45,98,98,45,51,51,45,52,52,45,53,53,45,54,54' # str | 起始rowkey，首次查询可输入空值来查询当页数据，翻页查询时输入的值根据前一次返回值中的nextRowkey填入。 (optional)
scene_name = '1' # str | 场景名称。取值范围：不填表示全部场景。 1、Station login and logout：终端上下线。 2、Login and logout of cloud managed device：云盒上下线。 3、Device operation：设备操作。 4、Wireless radio：无线射频。 5、Hardware fault：硬件故障。  (optional)
device_mac = 'AA-AA-AA-00-20-44' # str | 设备MAC地址，格式必须是xx-xx-xx-xx-xx-xx，支持大小写模糊。 (optional)
station_mac = 'D8-8F-76-7D-91-12' # str | 终端MAC地址，格式必须是xx-xx-xx-xx-xx-xx，支持大小写模糊。 入参stationMac有值时，仅查询终端上下线场景范围内的日志。  (optional)

try: 
    # 查询设备上报日志记录
    api_response = api_instance.query_log_data(page_size, site_id, begin_time, end_time, start_query_row_key=start_query_row_key, scene_name=scene_name, device_mac=device_mac, station_mac=station_mac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogManagerServiceNorthboundApi->query_log_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| 当页大小。 | 
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **begin_time** | **int**| 起始格林威治时间，起始与结束时间不可大于5天。 | 
 **end_time** | **int**| 结束时间格林威治时间，起始与结束时间不可大于5天。 | 
 **start_query_row_key** | **str**| 起始rowkey，首次查询可输入空值来查询当页数据，翻页查询时输入的值根据前一次返回值中的nextRowkey填入。 | [optional] 
 **scene_name** | **str**| 场景名称。取值范围：不填表示全部场景。 1、Station login and logout：终端上下线。 2、Login and logout of cloud managed device：云盒上下线。 3、Device operation：设备操作。 4、Wireless radio：无线射频。 5、Hardware fault：硬件故障。  | [optional] 
 **device_mac** | **str**| 设备MAC地址，格式必须是xx-xx-xx-xx-xx-xx，支持大小写模糊。 | [optional] 
 **station_mac** | **str**| 终端MAC地址，格式必须是xx-xx-xx-xx-xx-xx，支持大小写模糊。 入参stationMac有值时，仅查询终端上下线场景范围内的日志。  | [optional] 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

