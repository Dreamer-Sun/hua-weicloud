# swagger_client.TimeFlowStInfosApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice/user*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_flow_st_info_list**](TimeFlowStInfosApi.md#get_time_flow_st_info_list) | **GET** /controller/campus/v1/accountservice/user/timeflowstinfos | 查询用户流量信息


# **get_time_flow_st_info_list**
> TimeFlowStInfosOutputDto get_time_flow_st_info_list(site_id=site_id, page_index=page_index, page_size=page_size, sort=sort, user_name=user_name, used_time=used_time, used_flow=used_flow, begin_time=begin_time, end_time=end_time)

查询用户流量信息

## 典型场景 ##  提供查询指定时间内流量和时长发生变化的用户流量信息分页查询北向接口。 ## 接口功能 ##  根据租户ID查询最后一次计费时间在指定时间范围之内的用户流量信息。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeFlowStInfosApi()
site_id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | 站点ID，UUID格式。 (optional)
page_index = 1 # int | 当前页数，默认为1。 (optional)
page_size = 20 # int | 每页显示的最大数量，默认为20。 (optional)
sort = 'userName' # str | 排序字段，目前只支持用户名排序。userName为正序，-userName为逆序。 (optional)
user_name = 'zhangsan' # str | 用户名，最大长度为64。 (optional)
used_time = '20' # str | 已使用时长(分钟)大于等于当前条件值。 (optional)
used_flow = '10' # str | 已使用流量(兆)大于等于当前条件值。 (optional)
begin_time = '2017-11-24 17:26:55' # str | 最后一次计费时间起始时间。 (optional)
end_time = '2017-11-25 17:26:55' # str | 最后一次计费时间截止时间。 (optional)

try: 
    # 查询用户流量信息
    api_response = api_instance.get_time_flow_st_info_list(site_id=site_id, page_index=page_index, page_size=page_size, sort=sort, user_name=user_name, used_time=used_time, used_flow=used_flow, begin_time=begin_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeFlowStInfosApi->get_time_flow_st_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | [optional] 
 **page_index** | **int**| 当前页数，默认为1。 | [optional] 
 **page_size** | **int**| 每页显示的最大数量，默认为20。 | [optional] 
 **sort** | **str**| 排序字段，目前只支持用户名排序。userName为正序，-userName为逆序。 | [optional] 
 **user_name** | **str**| 用户名，最大长度为64。 | [optional] 
 **used_time** | **str**| 已使用时长(分钟)大于等于当前条件值。 | [optional] 
 **used_flow** | **str**| 已使用流量(兆)大于等于当前条件值。 | [optional] 
 **begin_time** | **str**| 最后一次计费时间起始时间。 | [optional] 
 **end_time** | **str**| 最后一次计费时间截止时间。 | [optional] 

### Return type

[**TimeFlowStInfosOutputDto**](TimeFlowStInfosOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

