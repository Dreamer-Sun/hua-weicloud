# swagger_client.NeListOpenApiServiceApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_ne_list**](NeListOpenApiServiceApi.md#query_ne_list) | **GET** /rest/openapi/network/nedevice | 查询列表信息


# **query_ne_list**
> NeListOpenApiResponse query_ne_list(nedn=nedn, neid=neid, aliasname=aliasname, nename=nename, necategory=necategory, netype=netype, nevendorname=nevendorname, neesn=neesn, neip=neip, nemac=nemac, version=version, nepatchversion=nepatchversion, nesysoid=nesysoid, nestate=nestate, lastpolltime=lastpolltime, createtime=createtime, timezoneid=timezoneid, neiptype=neiptype, subnet=subnet, negroupname=negroupname, neosversion=neosversion, necontact=necontact, neposition=neposition, memo=memo, maintainunit=maintainunit, putintoactiontime=putintoactiontime, usefullife=usefullife, neruntime=neruntime, nedescribe=nedescribe, asset_manager=asset_manager, asset_number=asset_number, asset_date=asset_date, start=start, size=size, orderby=orderby, desc=desc, fields=fields)

查询列表信息

## 典型场景 ##  查询网络设备信息时使用。 ## 接口功能 ##  查询网络设备信息，包括设备网元id，网元dn，网元名称，网元别名，网元IP，网元状态， 网元具体类型，设备类型，厂商名称， 序列号。 ## 接口约束 ##  该接口的查询条件参数可以为空。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NeListOpenApiServiceApi()
nedn = '00000000-1234-0000-0000-000000000001' # str | 设备DN。 (optional)
neid = '00000000-1234-0000-0000-000000000001' # str | 设备ID。 (optional)
aliasname = 'aliasname_example' # str | 网管名称。 (optional)
nename = 'nename_example' # str | 设备名称。 (optional)
necategory = 'necategory_example' # str | 设备分类。 (optional)
netype = 'netype_example' # str | 设备类型。 (optional)
nevendorname = 'nevendorname_example' # str | 设备厂商信息(设备厂商ID)。 (optional)
neesn = 'neesn_example' # str | 设备序列号。 (optional)
neip = 'neip_example' # str | 设备IP地址。 (optional)
nemac = 'nemac_example' # str | 设备MAC地址。 (optional)
version = 'version_example' # str | 设备版本。 (optional)
nepatchversion = 'nepatchversion_example' # str | 补丁版本。 (optional)
nesysoid = 'nesysoid_example' # str | 设备sysoid。 (optional)
nestate = 56 # int | 网络设备状态，可以是如下值之一： 0：未管理 1：在线 2：离线 3：未知 4：snmp不可达 5：错误  (optional)
lastpolltime = 'lastpolltime_example' # str | 上次同步时间。 (optional)
createtime = 'createtime_example' # str | 设备创建时间。 (optional)
timezoneid = 'timezoneid_example' # str | 设备时区。 (optional)
neiptype = 56 # int | ip地址类型，可以是如下值之一： 0：IPv4 1：IPv6  (optional)
subnet = 'subnet_example' # str | 所属子网。 (optional)
negroupname = 'negroupname_example' # str | 所属分组名称。 (optional)
neosversion = 'neosversion_example' # str | 软件版本。 (optional)
necontact = 'necontact_example' # str | 设备联系人。 (optional)
neposition = 'neposition_example' # str | 设备位置。 (optional)
memo = 'memo_example' # str | 设备备注。 (optional)
maintainunit = 'maintainunit_example' # str | 维保单位。 (optional)
putintoactiontime = 'putintoactiontime_example' # str | 投入使用时间。 (optional)
usefullife = 'usefullife_example' # str | 维保到期时间。 (optional)
neruntime = 'neruntime_example' # str | 设备启动时间。 (optional)
nedescribe = 'nedescribe_example' # str | 设备描述。 (optional)
asset_manager = 'asset_manager_example' # str | 资产管理人。 (optional)
asset_number = 'asset_number_example' # str | 资产编号。 (optional)
asset_date = 'asset_date_example' # str | 购买日期。 (optional)
start = 56 # int | 指定从哪个起始记录位置开始返回查询结果集，缺省值是0。 说明： 如果值小于0，将使用缺省值。  (optional)
size = 56 # int | 指定返回查询结果集总数。缺省值是20。 说明： 1、如果值小于0，将使用缺省值。 2、数据的size，最大建议10000条。  (optional)
orderby = 'orderby_example' # str | 指定查询结果集采用的排序字段。缺省排序字段是nedn。 可指定的排序字段包括：nedn、nename、necategory、netype、neip、nesysoid、nestate。  (optional)
desc = true # bool | 指定查询结果是否按降序排序。缺省值是false。 说明： 此请求参数只有指定了“orderby”请求参数后才有效。  (optional)
fields = 'fields_example' # str | 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了“fields”请求参数后才有效，不指定默认返回所有字段。  (optional)

try: 
    # 查询列表信息
    api_response = api_instance.query_ne_list(nedn=nedn, neid=neid, aliasname=aliasname, nename=nename, necategory=necategory, netype=netype, nevendorname=nevendorname, neesn=neesn, neip=neip, nemac=nemac, version=version, nepatchversion=nepatchversion, nesysoid=nesysoid, nestate=nestate, lastpolltime=lastpolltime, createtime=createtime, timezoneid=timezoneid, neiptype=neiptype, subnet=subnet, negroupname=negroupname, neosversion=neosversion, necontact=necontact, neposition=neposition, memo=memo, maintainunit=maintainunit, putintoactiontime=putintoactiontime, usefullife=usefullife, neruntime=neruntime, nedescribe=nedescribe, asset_manager=asset_manager, asset_number=asset_number, asset_date=asset_date, start=start, size=size, orderby=orderby, desc=desc, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeListOpenApiServiceApi->query_ne_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nedn** | **str**| 设备DN。 | [optional] 
 **neid** | **str**| 设备ID。 | [optional] 
 **aliasname** | **str**| 网管名称。 | [optional] 
 **nename** | **str**| 设备名称。 | [optional] 
 **necategory** | **str**| 设备分类。 | [optional] 
 **netype** | **str**| 设备类型。 | [optional] 
 **nevendorname** | **str**| 设备厂商信息(设备厂商ID)。 | [optional] 
 **neesn** | **str**| 设备序列号。 | [optional] 
 **neip** | **str**| 设备IP地址。 | [optional] 
 **nemac** | **str**| 设备MAC地址。 | [optional] 
 **version** | **str**| 设备版本。 | [optional] 
 **nepatchversion** | **str**| 补丁版本。 | [optional] 
 **nesysoid** | **str**| 设备sysoid。 | [optional] 
 **nestate** | **int**| 网络设备状态，可以是如下值之一： 0：未管理 1：在线 2：离线 3：未知 4：snmp不可达 5：错误  | [optional] 
 **lastpolltime** | **str**| 上次同步时间。 | [optional] 
 **createtime** | **str**| 设备创建时间。 | [optional] 
 **timezoneid** | **str**| 设备时区。 | [optional] 
 **neiptype** | **int**| ip地址类型，可以是如下值之一： 0：IPv4 1：IPv6  | [optional] 
 **subnet** | **str**| 所属子网。 | [optional] 
 **negroupname** | **str**| 所属分组名称。 | [optional] 
 **neosversion** | **str**| 软件版本。 | [optional] 
 **necontact** | **str**| 设备联系人。 | [optional] 
 **neposition** | **str**| 设备位置。 | [optional] 
 **memo** | **str**| 设备备注。 | [optional] 
 **maintainunit** | **str**| 维保单位。 | [optional] 
 **putintoactiontime** | **str**| 投入使用时间。 | [optional] 
 **usefullife** | **str**| 维保到期时间。 | [optional] 
 **neruntime** | **str**| 设备启动时间。 | [optional] 
 **nedescribe** | **str**| 设备描述。 | [optional] 
 **asset_manager** | **str**| 资产管理人。 | [optional] 
 **asset_number** | **str**| 资产编号。 | [optional] 
 **asset_date** | **str**| 购买日期。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集，缺省值是0。 说明： 如果值小于0，将使用缺省值。  | [optional] 
 **size** | **int**| 指定返回查询结果集总数。缺省值是20。 说明： 1、如果值小于0，将使用缺省值。 2、数据的size，最大建议10000条。  | [optional] 
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是nedn。 可指定的排序字段包括：nedn、nename、necategory、netype、neip、nesysoid、nestate。  | [optional] 
 **desc** | **bool**| 指定查询结果是否按降序排序。缺省值是false。 说明： 此请求参数只有指定了“orderby”请求参数后才有效。  | [optional] 
 **fields** | **str**| 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了“fields”请求参数后才有效，不指定默认返回所有字段。  | [optional] 

### Return type

[**NeListOpenApiResponse**](NeListOpenApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

