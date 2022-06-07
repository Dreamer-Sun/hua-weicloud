# swagger_client.AuthenticationLogApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authentication_log_info_list**](AuthenticationLogApi.md#get_authentication_log_info_list) | **GET** /controller/campus/v1/accountservice/user/authenticationlog | 查询用户上下线日志信息


# **get_authentication_log_info_list**
> get_authentication_log_info_list(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, user_name=user_name, terminal_mac=terminal_mac, user_type=user_type, access_ssid=access_ssid)

查询用户上下线日志信息

## 典型场景 ##  提供租户查询指定时间内用户上下线信息，按分页返回查询结果。例如：查询8月1日至8月7号这段时间哪些用户上线过。 ## 接口功能 ##  根据租户ID查询指定时间内用户上下线信息，每次最多返回101条数据，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。下一页查询以上一次查询返回的endRowKey的值作为本次查询条件startRowKey的值。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.AuthenticationLogApi()
start_row_key = '0000000000000000003000000000000000000100000000000000001529648625738B5F4EF82E97A4BD69FFF258082996290' # str | 起始rowkey（首次查询为空字符串，分页查询时取上一次查询结果endRowKey的值）。
site_id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | 站点ID（使用站点查询接口获取站点ID），格式为UUID。
auth_result = '1' # str | 认证结果（0---成功，1---失败）。
lower_online_time = 1529510400000 # int | 用户上线起始时间（接口调用方格林威治时间戳）。
upper_online_time = 1529683199000 # int | 用户上线的结束时间（接口调用方格林威治时间戳）。查询时不允许查询时间跨度大于7天的数据。
user_name = 'zhangsan' # str | 用户名（短信认证则为手机号码）。 (optional)
terminal_mac = '11-22-33-44-55-66' # str | 接入终端MAC地址（格式：AA-BB-CC-DD-EE-FF）。 (optional)
user_type = '1' # str | 用户类型（0---普通用户。1---短信注册用户。2---自注册用户。4---社交媒体用户。5---微信用户。6---Passcode用户。7---三方用户。20---普通访客。64---匿名用户）。 (optional)
access_ssid = 'guest' # str | 接入SSID名称。 (optional)

try: 
    # 查询用户上下线日志信息
    api_instance.get_authentication_log_info_list(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, user_name=user_name, terminal_mac=terminal_mac, user_type=user_type, access_ssid=access_ssid)
except ApiException as e:
    print("Exception when calling AuthenticationLogApi->get_authentication_log_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_row_key** | **str**| 起始rowkey（首次查询为空字符串，分页查询时取上一次查询结果endRowKey的值）。 | 
 **site_id** | **str**| 站点ID（使用站点查询接口获取站点ID），格式为UUID。 | 
 **auth_result** | **str**| 认证结果（0---成功，1---失败）。 | 
 **lower_online_time** | **int**| 用户上线起始时间（接口调用方格林威治时间戳）。 | 
 **upper_online_time** | **int**| 用户上线的结束时间（接口调用方格林威治时间戳）。查询时不允许查询时间跨度大于7天的数据。 | 
 **user_name** | **str**| 用户名（短信认证则为手机号码）。 | [optional] 
 **terminal_mac** | **str**| 接入终端MAC地址（格式：AA-BB-CC-DD-EE-FF）。 | [optional] 
 **user_type** | **str**| 用户类型（0---普通用户。1---短信注册用户。2---自注册用户。4---社交媒体用户。5---微信用户。6---Passcode用户。7---三方用户。20---普通访客。64---匿名用户）。 | [optional] 
 **access_ssid** | **str**| 接入SSID名称。 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

