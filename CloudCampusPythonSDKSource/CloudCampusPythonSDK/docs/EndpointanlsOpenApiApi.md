# swagger_client.EndpointanlsOpenApiApi

All URIs are relative to *https://localhost/controller/campus/v1/performanceservice/endpointbehavior*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_group_tags**](EndpointanlsOpenApiApi.md#get_device_group_tags) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/tags | 获取设备标签
[**get_history_flow_distr**](EndpointanlsOpenApiApi.md#get_history_flow_distr) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/historyflow | 查询历史接入客户数量
[**get_realtime_flow_distr**](EndpointanlsOpenApiApi.md#get_realtime_flow_distr) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/realtimeflow | 查询实时接入客户数量
[**query_capture_rate_distr**](EndpointanlsOpenApiApi.md#query_capture_rate_distr) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/capturerate | 查询访客、路人、接入用户的历史趋势
[**query_dwell_time_distr**](EndpointanlsOpenApiApi.md#query_dwell_time_distr) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/dwelltime | 查询访客驻留时长的历史趋势
[**query_loyalty_distr**](EndpointanlsOpenApiApi.md#query_loyalty_distr) | **GET** /controller/campus/v1/performanceservice/endpointbehavior/loyalty | 查询回头客记录


# **get_device_group_tags**
> DeviceGroupTagResp get_device_group_tags(site_id, page_size, page_index)

获取设备标签

## 典型场景 ##    提供查询设备标签。           ## 接口功能 ##    查询设备标签，设备标签在监控->设备360->AP-AP中创建，单个设备最多可以创建10个标签。 ## 接口约束 ##    1、只有租户管理员获取token并建立会话后才能调用该接口。    2、若pageSize和pageIndex参数不传或者为非法参数，则默认按照pageSize=1000，pageIndex=0返回查询结果。     

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
site_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 站点ID。
page_size = 20 # int | 分页的大小。
page_index = 1 # int | 分页的序号。

try: 
    # 获取设备标签
    api_response = api_instance.get_device_group_tags(site_id, page_size, page_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->get_device_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **page_size** | **int**| 分页的大小。 | 
 **page_index** | **int**| 分页的序号。 | 

### Return type

[**DeviceGroupTagResp**](DeviceGroupTagResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_flow_distr**
> FlowDistrResp get_history_flow_distr(site_id, start_time, end_time, tag_id=tag_id)

查询历史接入客户数量

## 典型场景 ##    查询历史客户流量。           ## 接口功能 ##    查询历史接入客户流量。 ## 接口约束 ##    1、只有租户管理员获取token并建立会话后才能调用该接口。    2、若时间差大于一个月小于一年，则以月时间粒度返回查询结果。    3、若时间差小于一个月大于一周，则以天时间维度返回查询结果。    4、若时间差小于一周，则以小时维度返回查询结果。    5、不支持超过一年以上的数据查询。         

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
site_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 站点ID。
start_time = 1568563200000 # int | 时间戳（毫秒），最大时间差不超过一年。
end_time = 1568573200000 # int | 时间戳（毫秒），最大时间差不超过一年。
tag_id = '31f35021-e656-472a-8937-9c6d6da76e6e' # str | 标签ID，UUID格式，非必填，若不填，则默认查询站点下所有设备。 (optional)

try: 
    # 查询历史接入客户数量
    api_response = api_instance.get_history_flow_distr(site_id, start_time, end_time, tag_id=tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->get_history_flow_distr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **start_time** | **int**| 时间戳（毫秒），最大时间差不超过一年。 | 
 **end_time** | **int**| 时间戳（毫秒），最大时间差不超过一年。 | 
 **tag_id** | **str**| 标签ID，UUID格式，非必填，若不填，则默认查询站点下所有设备。 | [optional] 

### Return type

[**FlowDistrResp**](FlowDistrResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_realtime_flow_distr**
> FlowDistrResp get_realtime_flow_distr(site_id, tag_id=tag_id)

查询实时接入客户数量

## 典型场景 ##    查询历史实时客户流量。           ## 接口功能 ##    查询历史实时客户数量，返回最近5分钟内接入客户流量。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
site_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 站点ID。
tag_id = '31f35021-e656-472a-8937-9c6d6da76e6e' # str | 标签ID，若不设置，则默认查询站点下所有设备。 (optional)

try: 
    # 查询实时接入客户数量
    api_response = api_instance.get_realtime_flow_distr(site_id, tag_id=tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->get_realtime_flow_distr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **tag_id** | **str**| 标签ID，若不设置，则默认查询站点下所有设备。 | [optional] 

### Return type

[**FlowDistrResp**](FlowDistrResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_capture_rate_distr**
> FlowDistrResp query_capture_rate_distr(tag_id, tag_type, start_time, end_time, time_unit)

查询访客、路人、接入用户的历史趋势

## 典型场景 ##    查询访客、路人、接入用户的历史趋势。           ## 接口功能 ##    查询访客、路人、接入用户的历史趋势。    访客：以一小时为周期，一小时内连续5分钟都被探测到的终端，识别为访客。    路人：不满足访客条件的终端，均识别为路人。    接入用户：已关联或已认证的终端，识别为接入用户。 ## 接口约束 ##    1、只有租户管理员获取token并建立会话后才能调用该接口。    2、若时间差大于一个月小于一年，则以月时间粒度返回查询结果。    3、若时间差小于一个月大于一周，则以天时间维度返回查询结果。    4、若时间差小于一周，则以小时维度返回查询结果。    5、不支持超过一年以上的数据查询。            

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
tag_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。
tag_type = '0' # str | 标签类型：  0---TagID为站点ID。  1---TagID为标签ID。 
start_time = 1567526400 # int | 时间戳（秒），最大时间差不超过一年。
end_time = 1567527800 # int | 时间戳（秒），最大时间差不超过一年。
time_unit = 'day' # str | 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度 

try: 
    # 查询访客、路人、接入用户的历史趋势
    api_response = api_instance.query_capture_rate_distr(tag_id, tag_type, start_time, end_time, time_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->query_capture_rate_distr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。 | 
 **tag_type** | **str**| 标签类型：  0---TagID为站点ID。  1---TagID为标签ID。  | 
 **start_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **end_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **time_unit** | **str**| 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度  | 

### Return type

[**FlowDistrResp**](FlowDistrResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_dwell_time_distr**
> FlowDistrResp query_dwell_time_distr(tag_id, tag_type, start_time, end_time, time_unit)

查询访客驻留时长的历史趋势

## 典型场景 ##    查询访客驻留时长的历史趋势。           ## 接口功能 ##    查询访客驻留时长的历史趋势。 ## 接口约束 ##    1、只有租户管理员获取token并建立会话后才能调用该接口。    2、若时间差大于一个月小于一年，则以月时间粒度返回查询结果。    3、若时间差小于一个月大于一周，则以天时间维度返回查询结果。    4、若时间差小于一周，则以小时维度返回查询结果。    5、不支持超过一年以上的数据查询。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
tag_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。
tag_type = '0' # str | 标签类型：  0---TagID为站点ID，  1---TagID为标签ID。 
start_time = 1567526400 # int | 时间戳（秒），最大时间差不超过一年。
end_time = 1567527800 # int | 时间戳（秒），最大时间差不超过一年。
time_unit = 'day' # str | 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度 

try: 
    # 查询访客驻留时长的历史趋势
    api_response = api_instance.query_dwell_time_distr(tag_id, tag_type, start_time, end_time, time_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->query_dwell_time_distr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。 | 
 **tag_type** | **str**| 标签类型：  0---TagID为站点ID，  1---TagID为标签ID。  | 
 **start_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **end_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **time_unit** | **str**| 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度  | 

### Return type

[**FlowDistrResp**](FlowDistrResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_loyalty_distr**
> FlowDistrResp query_loyalty_distr(tag_id, tag_type, start_time, end_time, time_unit)

查询回头客记录

## 典型场景 ##    查询回头客记录。           ## 接口功能 ##    查询回头客记录。    首次访问是指半年内无访问记录的访客。    偶尔访问是指半年内存在访问记录的访客。    经常访问是指最近一个月内访问超过7天的访客。    频繁访问时指最近一个月内访问超过15天的访客。 ## 接口约束 ##    1、只有租户管理员获取token并建立会话后才能调用该接口。    2、若时间差大于一个月小于一年，则以月时间粒度返回查询结果。    3、若时间差小于一个月大于一周，则以天时间维度返回查询结果。    4、若时间差小于一周，则以小时维度返回查询结果。    5、不支持超过一年以上的数据查询。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.EndpointanlsOpenApiApi()
tag_id = '9dffc44b-1824-42a4-ac48-616e3f0eaa2a' # str | 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。
tag_type = '0' # str | 标签类型：  0---TagID为站点ID，  1---TagID为标签ID。 
start_time = 1567526400 # int | 时间戳（秒），最大时间差不超过一年。
end_time = 1567527800 # int | 时间戳（秒），最大时间差不超过一年。
time_unit = 'day' # str | 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度 

try: 
    # 查询回头客记录
    api_response = api_instance.query_loyalty_distr(tag_id, tag_type, start_time, end_time, time_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointanlsOpenApiApi->query_loyalty_distr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| 设备标签，若设备标签不存在或查询所有设备，需填写站点ID。 | 
 **tag_type** | **str**| 标签类型：  0---TagID为站点ID，  1---TagID为标签ID。  | 
 **start_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **end_time** | **int**| 时间戳（秒），最大时间差不超过一年。 | 
 **time_unit** | **str**| 时间维度。   day---天维度   week---周维度   month---月维度   custom---自定义维度  | 

### Return type

[**FlowDistrResp**](FlowDistrResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

