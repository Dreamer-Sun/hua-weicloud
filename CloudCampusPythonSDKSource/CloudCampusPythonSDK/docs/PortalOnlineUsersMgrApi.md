# swagger_client.PortalOnlineUsersMgrApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cut_portal_online_users**](PortalOnlineUsersMgrApi.md#cut_portal_online_users) | **POST** /controller/campus/v1/accountservice/onlineusers/batch-delete | 管理员强制Portal在线用户下线
[**query_portal_online_user**](PortalOnlineUsersMgrApi.md#query_portal_online_user) | **GET** /controller/campus/v1/accountservice/onlineusers | 查询Portal在线用户


# **cut_portal_online_users**
> CutPortalOnlineUserOutputDto cut_portal_online_users(body)

管理员强制Portal在线用户下线

## 典型场景 ##  提供管理员强制Portal在线用户下线北向接口。 ## 接口功能 ##  管理员强制Portal在线用户下线 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalOnlineUsersMgrApi()
body = cloudcampus.CutPortalOnlineUserInputDto() # CutPortalOnlineUserInputDto | 管理员强制Portal在线用户下线参数。

try: 
    # 管理员强制Portal在线用户下线
    api_response = api_instance.cut_portal_online_users(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalOnlineUsersMgrApi->cut_portal_online_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CutPortalOnlineUserInputDto**](CutPortalOnlineUserInputDto.md)| 管理员强制Portal在线用户下线参数。 | 

### Return type

[**CutPortalOnlineUserOutputDto**](CutPortalOnlineUserOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_portal_online_user**
> list[QueryPortalOnlineUserInfoOutputDto] query_portal_online_user(user_type=user_type, auth_mode=auth_mode, page_index=page_index, page_size=page_size, user_name=user_name, begin_time_long=begin_time_long, end_time_long=end_time_long, access_policy=access_policy, terminal_ip=terminal_ip, terminal_mac=terminal_mac, ssid=ssid, user_group_id=user_group_id, site_id=site_id)

查询Portal在线用户

## 典型场景 ##  提供查询Portal在线用户北向接口。 ## 接口功能 ##  查询Portal在线用户列表。默认按照认证时间降序排列。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PortalOnlineUsersMgrApi()
user_type = '-1' # str | 用户类型： 0---普通用户 1---短信注册用户 2---自注册用户 4---社交媒体用户 5---微信用户 6---Passcode用户 7---第三方用户 11---PPSK 20---普通访客 64---匿名用户 如果不填，查询所有类型。  (optional) (default to -1)
auth_mode = '0' # str | 认证方式： 1---Portal认证 2---Mac优先认证 3---第三方认证 4---PPSK 如果不填，查询所有类型。  (optional) (default to 0)
page_index = 1 # int | 起始页。 (optional) (default to 1)
page_size = 20 # int | 分页大小。 (optional) (default to 20)
user_name = 'user1' # str | 用户名。用户名使用模糊查询。 (optional)
begin_time_long = 1541389780672 # int | 查询起始时间。 (optional)
end_time_long = 1541390000000 # int | 查询结束时间。 (optional)
access_policy = 'policy_for_guest' # str | 认证策略名。 (optional)
terminal_ip = '10.10.10.10' # str | 认证终端IP。 (optional)
terminal_mac = '64-80-99-CF-8A-32' # str | 认证终端MAC。 (optional)
ssid = 'portal-guest' # str | SSID (optional)
user_group_id = '2eab8922-a37d-43b2-9788-33caade63b5a' # str | 用户组ID。 (optional)
site_id = '2eab8922-a37d-43b2-9788-33caade63b5a' # str | 站点ID。 (optional)

try: 
    # 查询Portal在线用户
    api_response = api_instance.query_portal_online_user(user_type=user_type, auth_mode=auth_mode, page_index=page_index, page_size=page_size, user_name=user_name, begin_time_long=begin_time_long, end_time_long=end_time_long, access_policy=access_policy, terminal_ip=terminal_ip, terminal_mac=terminal_mac, ssid=ssid, user_group_id=user_group_id, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalOnlineUsersMgrApi->query_portal_online_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | **str**| 用户类型： 0---普通用户 1---短信注册用户 2---自注册用户 4---社交媒体用户 5---微信用户 6---Passcode用户 7---第三方用户 11---PPSK 20---普通访客 64---匿名用户 如果不填，查询所有类型。  | [optional] [default to -1]
 **auth_mode** | **str**| 认证方式： 1---Portal认证 2---Mac优先认证 3---第三方认证 4---PPSK 如果不填，查询所有类型。  | [optional] [default to 0]
 **page_index** | **int**| 起始页。 | [optional] [default to 1]
 **page_size** | **int**| 分页大小。 | [optional] [default to 20]
 **user_name** | **str**| 用户名。用户名使用模糊查询。 | [optional] 
 **begin_time_long** | **int**| 查询起始时间。 | [optional] 
 **end_time_long** | **int**| 查询结束时间。 | [optional] 
 **access_policy** | **str**| 认证策略名。 | [optional] 
 **terminal_ip** | **str**| 认证终端IP。 | [optional] 
 **terminal_mac** | **str**| 认证终端MAC。 | [optional] 
 **ssid** | **str**| SSID | [optional] 
 **user_group_id** | **str**| 用户组ID。 | [optional] 
 **site_id** | **str**| 站点ID。 | [optional] 

### Return type

[**list[QueryPortalOnlineUserInfoOutputDto]**](QueryPortalOnlineUserInfoOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

