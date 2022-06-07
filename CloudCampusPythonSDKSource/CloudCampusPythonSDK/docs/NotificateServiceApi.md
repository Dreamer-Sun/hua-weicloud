# swagger_client.NotificateServiceApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_it_notificate_message**](NotificateServiceApi.md#cancel_it_notificate_message) | **DELETE** /rest/openapi/notification/it/link | 取消订阅IT设备链路变更通知
[**cancel_network_notificate_message**](NotificateServiceApi.md#cancel_network_notificate_message) | **DELETE** /rest/openapi/notification/network/link | 取消订阅网络链路变更通知
[**do_get**](NotificateServiceApi.md#do_get) | **GET** /rest/openapi/network/link | 查询网络链路列表信息
[**query_it_links**](NotificateServiceApi.md#query_it_links) | **GET** /rest/openapi/it/link | 查询IT设备链路信息
[**suscrbie_it_link_change_message**](NotificateServiceApi.md#suscrbie_it_link_change_message) | **PUT** /rest/openapi/notification/it/link | 订阅IT设备链路变更通知
[**suscrbie_network_link_change_message**](NotificateServiceApi.md#suscrbie_network_link_change_message) | **PUT** /rest/openapi/notification/network/link | 订阅网络链路变更通知


# **cancel_it_notificate_message**
> SubscribeResponse cancel_it_notificate_message(openid, system_id, desc=desc)

取消订阅IT设备链路变更通知

## 典型场景 ##   需要取消IT设备链路变更通知时使用。 ## 接口功能 ##   删除IT设备链路变更通知，IT设备链路发生变更时，不再发送通知消息。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于Open API的鉴权。
system_id = '10.10.10.10' # str | 第三方系统标识（可为IP地址）
desc = 'desc_example' # str | 第三方系统描述 (optional)

try: 
    # 取消订阅IT设备链路变更通知
    api_response = api_instance.cancel_it_notificate_message(openid, system_id, desc=desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->cancel_it_notificate_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于Open API的鉴权。 | 
 **system_id** | **str**| 第三方系统标识（可为IP地址） | 
 **desc** | **str**| 第三方系统描述 | [optional] 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_network_notificate_message**
> SubscribeResponse cancel_network_notificate_message(openid, system_id, desc=desc)

取消订阅网络链路变更通知

## 典型场景 ##   需要取消网络链路变更通知时使用。 ## 接口功能 ##   删除网络链路变更通知，网络链路发生变更时，不再发送通知消息。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于Open API的鉴权。
system_id = '10.10.10.10' # str | 第三方系统标识（可为IP地址）
desc = 'desc_example' # str | 第三方系统描述 (optional)

try: 
    # 取消订阅网络链路变更通知
    api_response = api_instance.cancel_network_notificate_message(openid, system_id, desc=desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->cancel_network_notificate_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于Open API的鉴权。 | 
 **system_id** | **str**| 第三方系统标识（可为IP地址） | 
 **desc** | **str**| 第三方系统描述 | [optional] 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_get**
> NorthResponse do_get(openid, anedn=anedn, anename=anename, aneip=aneip, anestate=anestate, aportdn=aportdn, aportname=aportname, aportip=aportip, aportadminstatus=aportadminstatus, aportoperstatus=aportoperstatus, znedn=znedn, znename=znename, zneip=zneip, znestate=znestate, zportdn=zportdn, zportname=zportname, zportip=zportip, zportadminstatus=zportadminstatus, zportoperstatus=zportoperstatus, linkdn=linkdn, linkname=linkname, linkstatus=linkstatus, linktype=linktype, speed=speed, start=start, size=size, orderby=orderby, desc=desc)

查询网络链路列表信息

## 典型场景 ##   需要查询网络链路列表使用。 ## 接口功能 ##  查询网络链路信息，包括链路列表，符合查询条件的设备记录总数以及分页查询总页数。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于Open API的鉴权。
anedn = 'anedn_example' # str | 源网元DN (optional)
anename = 'anename_example' # str | 源网元名称 (optional)
aneip = 'aneip_example' # str | 源网元IP (optional)
anestate = 56 # int | 源网元状态取值： 0：未管理 1：在线 2：离线 3：未知  (optional)
aportdn = 'aportdn_example' # str | 源端口DN (optional)
aportname = 'aportname_example' # str | 源端口名称 (optional)
aportip = 'aportip_example' # str | 源端口IP (optional)
aportadminstatus = 56 # int | 源端口管理状态： 1：up正常状态 2：down故障状态 3：testing测试状态  (optional)
aportoperstatus = 56 # int | 源端口运行状态： 1：up正常状态 2：down故障状态 3：testing测试状态 4：unknown未知状态 5：dormant休眠状态 6：notPresent不存在状态 7：lowerLayerDown下层状态down状态  (optional)
znedn = 'znedn_example' # str | 宿网元DN (optional)
znename = 'znename_example' # str | 宿网元名称 (optional)
zneip = 'zneip_example' # str | 宿网元IP (optional)
znestate = 56 # int | 宿网元状态： 0：未管理 1：在线 2：离线 3：未知  (optional)
zportdn = 'zportdn_example' # str | 宿端口DN (optional)
zportname = 'zportname_example' # str | 宿端口名称 (optional)
zportip = 'zportip_example' # str | 宿端口IP (optional)
zportadminstatus = 56 # int | 宿端口管理状态： 1：up正常状态 2：down故障状态 3：testing测试状态  (optional)
zportoperstatus = 56 # int | 宿端口运行状态： 1：up正常状态 2：down故障状态 3：testing测试状态 4：unknown未知状态 5：dormant休眠状态 6：notPresent不存在状态 7：lowerLayerDown下层状态down状态  (optional)
linkdn = 'linkdn_example' # str | 链路DN (optional)
linkname = 'linkname_example' # str | 链路名称 (optional)
linkstatus = 56 # int | 链路状态： 0：正常 1：未知 2：重要故障 3：紧急故障 4：离线 5：不管理  (optional)
linktype = 56 # int | 链路类型： 1：LLDP 2：Side-By-Side链路 3：MACARP 4：CDP 5：IP 6：由物理链路生成Eth-Trunk链路 99：手工  (optional)
speed = 'speed_example' # str | 单位：Mbit/s (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。小于0使用缺省值。 (optional) (default to 0)
size = 20 # int | 指定返回查询结果集总数。缺省值是20。（如果值小于0，将使用缺省值。） (optional) (default to 20)
orderby = 'linkdn' # str | 指定查询结果集采用的排序字段。缺省排序字段是linkdn。可指定的排序字段包括：linkdn，linkname，anedn，anename，aportdn，aportname，znedn，znename，zportdn，zportname，linktype，speed。指定多个排序字段时字段间用英文半角逗号“,”分隔。 (optional) (default to linkdn)
desc = false # bool | 指定查询结果是否按照降序排序。只有指定orderby请求参数才生效 (optional) (default to false)

try: 
    # 查询网络链路列表信息
    api_response = api_instance.do_get(openid, anedn=anedn, anename=anename, aneip=aneip, anestate=anestate, aportdn=aportdn, aportname=aportname, aportip=aportip, aportadminstatus=aportadminstatus, aportoperstatus=aportoperstatus, znedn=znedn, znename=znename, zneip=zneip, znestate=znestate, zportdn=zportdn, zportname=zportname, zportip=zportip, zportadminstatus=zportadminstatus, zportoperstatus=zportoperstatus, linkdn=linkdn, linkname=linkname, linkstatus=linkstatus, linktype=linktype, speed=speed, start=start, size=size, orderby=orderby, desc=desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->do_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于Open API的鉴权。 | 
 **anedn** | **str**| 源网元DN | [optional] 
 **anename** | **str**| 源网元名称 | [optional] 
 **aneip** | **str**| 源网元IP | [optional] 
 **anestate** | **int**| 源网元状态取值： 0：未管理 1：在线 2：离线 3：未知  | [optional] 
 **aportdn** | **str**| 源端口DN | [optional] 
 **aportname** | **str**| 源端口名称 | [optional] 
 **aportip** | **str**| 源端口IP | [optional] 
 **aportadminstatus** | **int**| 源端口管理状态： 1：up正常状态 2：down故障状态 3：testing测试状态  | [optional] 
 **aportoperstatus** | **int**| 源端口运行状态： 1：up正常状态 2：down故障状态 3：testing测试状态 4：unknown未知状态 5：dormant休眠状态 6：notPresent不存在状态 7：lowerLayerDown下层状态down状态  | [optional] 
 **znedn** | **str**| 宿网元DN | [optional] 
 **znename** | **str**| 宿网元名称 | [optional] 
 **zneip** | **str**| 宿网元IP | [optional] 
 **znestate** | **int**| 宿网元状态： 0：未管理 1：在线 2：离线 3：未知  | [optional] 
 **zportdn** | **str**| 宿端口DN | [optional] 
 **zportname** | **str**| 宿端口名称 | [optional] 
 **zportip** | **str**| 宿端口IP | [optional] 
 **zportadminstatus** | **int**| 宿端口管理状态： 1：up正常状态 2：down故障状态 3：testing测试状态  | [optional] 
 **zportoperstatus** | **int**| 宿端口运行状态： 1：up正常状态 2：down故障状态 3：testing测试状态 4：unknown未知状态 5：dormant休眠状态 6：notPresent不存在状态 7：lowerLayerDown下层状态down状态  | [optional] 
 **linkdn** | **str**| 链路DN | [optional] 
 **linkname** | **str**| 链路名称 | [optional] 
 **linkstatus** | **int**| 链路状态： 0：正常 1：未知 2：重要故障 3：紧急故障 4：离线 5：不管理  | [optional] 
 **linktype** | **int**| 链路类型： 1：LLDP 2：Side-By-Side链路 3：MACARP 4：CDP 5：IP 6：由物理链路生成Eth-Trunk链路 99：手工  | [optional] 
 **speed** | **str**| 单位：Mbit/s | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。小于0使用缺省值。 | [optional] [default to 0]
 **size** | **int**| 指定返回查询结果集总数。缺省值是20。（如果值小于0，将使用缺省值。） | [optional] [default to 20]
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是linkdn。可指定的排序字段包括：linkdn，linkname，anedn，anename，aportdn，aportname，znedn，znename，zportdn，zportname，linktype，speed。指定多个排序字段时字段间用英文半角逗号“,”分隔。 | [optional] [default to linkdn]
 **desc** | **bool**| 指定查询结果是否按照降序排序。只有指定orderby请求参数才生效 | [optional] [default to false]

### Return type

[**NorthResponse**](NorthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_it_links**
> ItQueryResonse query_it_links(openid, anedn=anedn, znedn=znedn, start=start, size=size)

查询IT设备链路信息

## 典型场景 ##   需要查询IT设备链路使用。 ## 接口功能 ##  查询IT设备链路信息，包括链路列表，符合查询条件的设备记录总数以及分页查询总页数。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于OpenAPI的鉴权。
anedn = 'anedn_example' # str | 源网元DN (optional)
znedn = 'znedn_example' # str | 目的网元DN (optional)
start = 1 # int | 页查询的第几页，从1开始，默认取第1页。 (optional) (default to 1)
size = 20 # int | 分页查询的每页记录数，支持1～100条，默认值20条。说明pageSize小于1或大于100时，使用默认值20。 (optional) (default to 20)

try: 
    # 查询IT设备链路信息
    api_response = api_instance.query_it_links(openid, anedn=anedn, znedn=znedn, start=start, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->query_it_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于OpenAPI的鉴权。 | 
 **anedn** | **str**| 源网元DN | [optional] 
 **znedn** | **str**| 目的网元DN | [optional] 
 **start** | **int**| 页查询的第几页，从1开始，默认取第1页。 | [optional] [default to 1]
 **size** | **int**| 分页查询的每页记录数，支持1～100条，默认值20条。说明pageSize小于1或大于100时，使用默认值20。 | [optional] [default to 20]

### Return type

[**ItQueryResonse**](ItQueryResonse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suscrbie_it_link_change_message**
> SubscribeResponse suscrbie_it_link_change_message(openid, registry_info)

订阅IT设备链路变更通知

## 典型场景 ##   需要接受IT设备链路变更消息时使用。 ## 接口功能 ##   注册IT设备链路变更通知，注册时携带URL路径，IT设备链路发生变更时，网管以POST方式向该URL发送通知消息。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于Open API的鉴权。
registry_info = cloudcampus.RegistryInfo() # RegistryInfo | 

try: 
    # 订阅IT设备链路变更通知
    api_response = api_instance.suscrbie_it_link_change_message(openid, registry_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->suscrbie_it_link_change_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于Open API的鉴权。 | 
 **registry_info** | [**RegistryInfo**](RegistryInfo.md)|  | 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suscrbie_network_link_change_message**
> SubscribeResponse suscrbie_network_link_change_message(openid, registry_info)

订阅网络链路变更通知

## 典型场景 ##   需要接受网络链路变更消息时使用。 ## 接口功能 ##   注册网络链路变更通知，注册时携带URL路径，网络链路发生变更时，网管以POST方式向该URL发送通知消息。 ## 接口约束 ##   该接口支持北向用户访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NotificateServiceApi()
openid = 'x-3wurfw2mrsum874amnelmm5haovyuns706iooanu8989c4rukaphle9dld47o8rwjwg686ip5gpfdgiqjxhf84s6k6juth0bpeulqmimiodf2p3u6ro93xink5qng5jy' # str | 会话标识，用于Open API的鉴权。
registry_info = cloudcampus.RegistryInfo() # RegistryInfo | 

try: 
    # 订阅网络链路变更通知
    api_response = api_instance.suscrbie_network_link_change_message(openid, registry_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificateServiceApi->suscrbie_network_link_change_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openid** | **str**| 会话标识，用于Open API的鉴权。 | 
 **registry_info** | [**RegistryInfo**](RegistryInfo.md)|  | 

### Return type

[**SubscribeResponse**](SubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

