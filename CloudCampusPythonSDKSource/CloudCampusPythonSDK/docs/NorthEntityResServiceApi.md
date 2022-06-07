# swagger_client.NorthEntityResServiceApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_frame_list**](NorthEntityResServiceApi.md#get_frame_list) | **GET** /rest/openapi/network/frame | 条件查询机框资源
[**get_ot_point_list**](NorthEntityResServiceApi.md#get_ot_point_list) | **GET** /rest/openapi/network/otpoint | 条件查询光口资源
[**get_port_list**](NorthEntityResServiceApi.md#get_port_list) | **GET** /rest/openapi/network/port | 条件查询端口资源
[**get_slot_list**](NorthEntityResServiceApi.md#get_slot_list) | **GET** /rest/openapi/network/slot | 条件查询单板资源
[**get_sub_slot_list**](NorthEntityResServiceApi.md#get_sub_slot_list) | **GET** /rest/openapi/network/subslot | 条件查询子卡资源


# **get_frame_list**
> FrameResResponse get_frame_list(nedn=nedn, nename=nename, framedn=framedn, shelfindex=shelfindex, frameindex=frameindex, frameno=frameno, vendortype=vendortype, mfgname=mfgname, serialnum=serialnum, physicalclass=physicalclass, descr=descr, framename=framename, adminstatus=adminstatus, operstatus=operstatus, standbystatus=standbystatus, softversion=softversion, start=start, size=size, orderby=orderby, desc=desc)

条件查询机框资源

## 典型场景 ##  北向接口支持条件查询机框资源。 ## 接口功能 ##  条件查询机框资源。 ## 接口约束 ##  该接口属于北向接口，由北向调用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NorthEntityResServiceApi()
nedn = '047f72d1-7ad3-11e9-b906-000c29b01448' # str | 设备dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 (optional)
nename = 'FW_B' # str | 网元名称，样例：FW_B。 (optional)
framedn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1' # str | 机框Dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1。 (optional)
shelfindex = -1 # int | 机架索引设备上有的，所有资源的根索引，样例：-1。 (optional)
frameindex = 67108867 # int | 机框索引，样例：67108867。 (optional)
frameno = 1 # int | 机框序号，样例：1。 (optional)
vendortype = '.1.3.6.1.4.1.2011.20021210.11.16715812' # str | 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.11.16715812。 (optional)
mfgname = 'Huawei' # str | 物理固件的制造厂商，样例：Huawei。 (optional)
serialnum = '020LKTD0A9000233' # str | 序列号，样例：020LKTD0A9000233。 (optional)
physicalclass = 3 # int | 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  (optional)
descr = 'Eudemon1000E-N6' # str | 机框描述，样例：Eudemon1000E-N6。 (optional)
framename = 'Eudemon1000E-N6' # str | 机框名称，样例：Eudemon1000E-N6。 (optional)
adminstatus = 4 # int | 管理状态，可以是如下值之一： 4、11：正常 2、3、12：错误 13：LoopBack 其他：未知  (optional)
operstatus = 3 # int | 操作状态，可以是如下值之一： 3、11、13、15、16：正常 2、12、17：错误 4：离线 其他：未知  (optional)
standbystatus = 1 # int | 主备状态： 1：notSupported  2：hotStandby  3：coldStandby  4：providingService  (optional)
softversion = 'V500R001C80SPC100' # str | 软件版本。 (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明，如果值小于0，将使用缺省值。 (optional)
size = 20 # int | 指定返回查询结果集总数。缺省值是20。说明，如果值小于0，将使用缺省值。 (optional)
orderby = 'nedn' # str | 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、framename（机框名称）。 (optional)
desc = true # bool | 指定查询结果是否按降序排序。缺省值是false。说明，此请求参数只有指定了“orderby”请求参数后才有效。 (optional)

try: 
    # 条件查询机框资源
    api_response = api_instance.get_frame_list(nedn=nedn, nename=nename, framedn=framedn, shelfindex=shelfindex, frameindex=frameindex, frameno=frameno, vendortype=vendortype, mfgname=mfgname, serialnum=serialnum, physicalclass=physicalclass, descr=descr, framename=framename, adminstatus=adminstatus, operstatus=operstatus, standbystatus=standbystatus, softversion=softversion, start=start, size=size, orderby=orderby, desc=desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NorthEntityResServiceApi->get_frame_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nedn** | **str**| 设备dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 | [optional] 
 **nename** | **str**| 网元名称，样例：FW_B。 | [optional] 
 **framedn** | **str**| 机框Dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1。 | [optional] 
 **shelfindex** | **int**| 机架索引设备上有的，所有资源的根索引，样例：-1。 | [optional] 
 **frameindex** | **int**| 机框索引，样例：67108867。 | [optional] 
 **frameno** | **int**| 机框序号，样例：1。 | [optional] 
 **vendortype** | **str**| 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.11.16715812。 | [optional] 
 **mfgname** | **str**| 物理固件的制造厂商，样例：Huawei。 | [optional] 
 **serialnum** | **str**| 序列号，样例：020LKTD0A9000233。 | [optional] 
 **physicalclass** | **int**| 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  | [optional] 
 **descr** | **str**| 机框描述，样例：Eudemon1000E-N6。 | [optional] 
 **framename** | **str**| 机框名称，样例：Eudemon1000E-N6。 | [optional] 
 **adminstatus** | **int**| 管理状态，可以是如下值之一： 4、11：正常 2、3、12：错误 13：LoopBack 其他：未知  | [optional] 
 **operstatus** | **int**| 操作状态，可以是如下值之一： 3、11、13、15、16：正常 2、12、17：错误 4：离线 其他：未知  | [optional] 
 **standbystatus** | **int**| 主备状态： 1：notSupported  2：hotStandby  3：coldStandby  4：providingService  | [optional] 
 **softversion** | **str**| 软件版本。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明，如果值小于0，将使用缺省值。 | [optional] 
 **size** | **int**| 指定返回查询结果集总数。缺省值是20。说明，如果值小于0，将使用缺省值。 | [optional] 
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、framename（机框名称）。 | [optional] 
 **desc** | **bool**| 指定查询结果是否按降序排序。缺省值是false。说明，此请求参数只有指定了“orderby”请求参数后才有效。 | [optional] 

### Return type

[**FrameResResponse**](FrameResResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ot_point_list**
> OTPointResResponse get_ot_point_list(nedn=nedn, start=start, size=size, fields=fields)

条件查询光口资源

## 典型场景 ##  北向接口支持条件查询光口资源。 ## 接口功能 ##  条件查询光口资源。 ## 接口约束 ##  该接口属于北向接口，由北向调用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NorthEntityResServiceApi()
nedn = '047f72d1-7ad3-11e9-b906-000c29b01448' # str | 设备DN，样例：NE=34604111。 (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 (optional)
size = 20 # int | 指定返回查询结果集总数，支持1～100条，缺省值是20。说明：如果值小于1或大于100时，将使用缺省值。 (optional)
fields = 'nedn' # str | 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了fields请求参数后才有效，不指定默认返回所有字段。 (optional)

try: 
    # 条件查询光口资源
    api_response = api_instance.get_ot_point_list(nedn=nedn, start=start, size=size, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NorthEntityResServiceApi->get_ot_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nedn** | **str**| 设备DN，样例：NE&#x3D;34604111。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 | [optional] 
 **size** | **int**| 指定返回查询结果集总数，支持1～100条，缺省值是20。说明：如果值小于1或大于100时，将使用缺省值。 | [optional] 
 **fields** | **str**| 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了fields请求参数后才有效，不指定默认返回所有字段。 | [optional] 

### Return type

[**OTPointResResponse**](OTPointResResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_list**
> PortResResponse get_port_list(neip=neip, nename=nename, nedn=nedn, portdn=portdn, framedn=framedn, slotdn=slotdn, subslotdn=subslotdn, frameno=frameno, slotno=slotno, subslotno=subslotno, portindex=portindex, portno=portno, descr=descr, name=name, adminstatus=adminstatus, operstatus=operstatus, ifindex=ifindex, iftype=iftype, ipaddress=ipaddress, ifspeed=ifspeed, start=start, size=size, orderby=orderby, desc=desc, fields=fields)

条件查询端口资源

## 典型场景 ##  北向接口支持条件查询端口资源。 ## 接口功能 ##  条件查询端口资源。 ## 接口约束 ##  该接口属于北向接口，由北向调用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NorthEntityResServiceApi()
neip = '10.136.252.60' # str | 设备IP地址，样例：10.136.252.60。 (optional)
nename = 'FW_B' # str | 设备名称，样例：FW_B。 (optional)
nedn = '047f72d1-7ad3-11e9-b906-000c29b01448' # str | 设备DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 (optional)
portdn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1,SS=-1,PP=|1025|0|GigabitEthernet1/0/0' # str | 端口DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1,SS=-1,PP=|1025|0|GigabitEthernet1/0/0。 (optional)
framedn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1' # str | 机框DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1。 (optional)
slotdn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1' # str | 单板DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1。 (optional)
subslotdn = '-1' # str | 子卡DN，样例：-1。 (optional)
frameno = 1 # int | 机框序号，样例：1。 (optional)
slotno = 1 # int | 单板序号，样例：1。 (optional)
subslotno = -1 # int | 子卡序号，样例：-1。 (optional)
portindex = 67387406 # int | 端口索引，样例：67387406。 (optional)
portno = 0 # int | 端口编号，样例：0。 (optional)
descr = 'Port' # str | 端口描述，样例：Port。 (optional)
name = 'GigabitEthernet1/0/0' # str | 端口名称，样例：GigabitEthernet1/0/0。 (optional)
adminstatus = 1 # int | 接口管理状态，可以是如下值之一： 1：up 2：down  (optional)
operstatus = 2 # int | 接口运行状态，可以是如下值之一： 1：up 2：down  (optional)
ifindex = 6 # int | 接口索引，样例：6。 (optional)
iftype = 2 # int | 端口类型，可以是如下值之一： 2：Ethernet 5：Atm 6：Pos 7：Serial 9：E1 10：T1 11：Cpos 19：Aux 20：E3 21：T3 22：Meth 32：Cellular  (optional)
ipaddress = '10.0.0.0' # str | 端口IP地址，样例：10.0.0.0。 (optional)
ifspeed = '1000000000' # str | 端口速率（bps），样例：1000000000。 (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 (optional)
size = 20 # int | 指定返回查询结果集总数，支持1～100条，缺省值是20。说明：如果值小于1或大于100时，将使用缺省值。 (optional)
orderby = 'nedn' # str | 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、portdn，name(端口名) 说明： 指定多个排序字段时字段间用英文半角逗号“,”分隔。 (optional)
desc = true # bool | 指定查询结果是否按降序排序。缺省值是false。说明：此请求参数只有指定了“orderby”请求参数后才有效。 (optional)
fields = 'nedn' # str | 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了fields请求参数后才有效，不指定默认返回所有字段。 (optional)

try: 
    # 条件查询端口资源
    api_response = api_instance.get_port_list(neip=neip, nename=nename, nedn=nedn, portdn=portdn, framedn=framedn, slotdn=slotdn, subslotdn=subslotdn, frameno=frameno, slotno=slotno, subslotno=subslotno, portindex=portindex, portno=portno, descr=descr, name=name, adminstatus=adminstatus, operstatus=operstatus, ifindex=ifindex, iftype=iftype, ipaddress=ipaddress, ifspeed=ifspeed, start=start, size=size, orderby=orderby, desc=desc, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NorthEntityResServiceApi->get_port_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neip** | **str**| 设备IP地址，样例：10.136.252.60。 | [optional] 
 **nename** | **str**| 设备名称，样例：FW_B。 | [optional] 
 **nedn** | **str**| 设备DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 | [optional] 
 **portdn** | **str**| 端口DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1,S&#x3D;1,SS&#x3D;-1,PP&#x3D;|1025|0|GigabitEthernet1/0/0。 | [optional] 
 **framedn** | **str**| 机框DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1。 | [optional] 
 **slotdn** | **str**| 单板DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1,S&#x3D;1。 | [optional] 
 **subslotdn** | **str**| 子卡DN，样例：-1。 | [optional] 
 **frameno** | **int**| 机框序号，样例：1。 | [optional] 
 **slotno** | **int**| 单板序号，样例：1。 | [optional] 
 **subslotno** | **int**| 子卡序号，样例：-1。 | [optional] 
 **portindex** | **int**| 端口索引，样例：67387406。 | [optional] 
 **portno** | **int**| 端口编号，样例：0。 | [optional] 
 **descr** | **str**| 端口描述，样例：Port。 | [optional] 
 **name** | **str**| 端口名称，样例：GigabitEthernet1/0/0。 | [optional] 
 **adminstatus** | **int**| 接口管理状态，可以是如下值之一： 1：up 2：down  | [optional] 
 **operstatus** | **int**| 接口运行状态，可以是如下值之一： 1：up 2：down  | [optional] 
 **ifindex** | **int**| 接口索引，样例：6。 | [optional] 
 **iftype** | **int**| 端口类型，可以是如下值之一： 2：Ethernet 5：Atm 6：Pos 7：Serial 9：E1 10：T1 11：Cpos 19：Aux 20：E3 21：T3 22：Meth 32：Cellular  | [optional] 
 **ipaddress** | **str**| 端口IP地址，样例：10.0.0.0。 | [optional] 
 **ifspeed** | **str**| 端口速率（bps），样例：1000000000。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 | [optional] 
 **size** | **int**| 指定返回查询结果集总数，支持1～100条，缺省值是20。说明：如果值小于1或大于100时，将使用缺省值。 | [optional] 
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、portdn，name(端口名) 说明： 指定多个排序字段时字段间用英文半角逗号“,”分隔。 | [optional] 
 **desc** | **bool**| 指定查询结果是否按降序排序。缺省值是false。说明：此请求参数只有指定了“orderby”请求参数后才有效。 | [optional] 
 **fields** | **str**| 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。 说明： 此请求参数只有指定了fields请求参数后才有效，不指定默认返回所有字段。 | [optional] 

### Return type

[**PortResResponse**](PortResResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slot_list**
> SlotResResponse get_slot_list(nedn=nedn, nename=nename, framedn=framedn, framename=framename, frameno=frameno, slotdn=slotdn, slotindex=slotindex, slotno=slotno, vendortype=vendortype, descr=descr, slotname=slotname, physicalclass=physicalclass, adminstatus=adminstatus, operstatus=operstatus, standbystatus=standbystatus, hardversion=hardversion, firmversion=firmversion, softversion=softversion, serialnum=serialnum, mfgname=mfgname, modelname=modelname, alarmlight=alarmlight, start=start, size=size, orderby=orderby, desc=desc, fields=fields)

条件查询单板资源

## 典型场景 ##  北向接口支持条件查询单板资源。 ## 接口功能 ##  条件查询单板资源。 ## 接口约束 ##  该接口属于北向接口，由北向调用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NorthEntityResServiceApi()
nedn = '047f72d1-7ad3-11e9-b906-000c29b01448' # str | 设备DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 (optional)
nename = 'FW_B' # str | 设备名称，样例：FW_B。 (optional)
framedn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1' # str | 机框DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1。 (optional)
framename = 'Eudemon1000E-N6' # str | 机框名称，样例：Eudemon1000E-N6。 (optional)
frameno = 1 # int | 机框序号，样例：1。 (optional)
slotdn = '047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1' # str | 单板Dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR=1,S=1。 (optional)
slotindex = 67371017 # int | 单板索引，样例：67371017。 (optional)
slotno = 1 # int | 单板序号，样例：1。 (optional)
vendortype = '.1.3.6.1.4.1.2011.20021210.12.16719978' # str | 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.12.16719978。 (optional)
descr = '--' # str | 单板描述，样例：--。 (optional)
slotname = '2XG8GE' # str | 单板名称，样例：2XG8GE。 (optional)
physicalclass = 9 # int | 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  (optional)
adminstatus = 4 # int | 管理状态： 4、11：正常 2、3、12：错误 13：LoopBack  (optional)
operstatus = 3 # int | 操作状态： 3、11、13、15、16：正 2、12、17：错误 4：离线 其他：未知  (optional)
standbystatus = 1 # int | 主备状态： 1：notSupported 2： hotStandby 3：coldStandby 4：providingService  (optional)
hardversion = 'VER.A' # str | 硬件版本，样例：VER.A。 (optional)
firmversion = '221 Nov 28 2017 17:23:17' # str | 固件版本，样例：221 Nov 28 2017 17:23:17 。 (optional)
softversion = 'V500R001C80SPC100' # str | 软件版本，样例：V500R001C80SPC100。 (optional)
serialnum = '210235G7FW0123456789' # str | 序列号，样例：210235G7FW0123456789。 (optional)
mfgname = 'Huawei' # str | 组件名称，样例：Huawei。 (optional)
modelname = 'huawei' # str | 模块名称，样例：huawei。 (optional)
alarmlight = 'huawei' # str | 预留字段，当前无意义。 (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明： 如果值小于0，将使用缺省值。 (optional)
size = 20 # int | 指定返回查询结果集总数。缺省值是20。说明： 1、如果值小于0，将使用缺省值。2、数据的size，最大建议10000条。 (optional)
orderby = 'nedn' # str | 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、framename、slotdn说明：指定多个排序字段时字段间用英文半角逗号“,”分隔。 (optional)
desc = true # bool | 指定查询结果是否按降序排序。缺省值是false。说明： 此请求参数只有指定了“orderby”请求参数后才有效。 (optional)
fields = 'nedn' # str | 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。说明：此请求参数只有指定了“fields”请求参数后才有效，不指定默认返回所有字段。 (optional)

try: 
    # 条件查询单板资源
    api_response = api_instance.get_slot_list(nedn=nedn, nename=nename, framedn=framedn, framename=framename, frameno=frameno, slotdn=slotdn, slotindex=slotindex, slotno=slotno, vendortype=vendortype, descr=descr, slotname=slotname, physicalclass=physicalclass, adminstatus=adminstatus, operstatus=operstatus, standbystatus=standbystatus, hardversion=hardversion, firmversion=firmversion, softversion=softversion, serialnum=serialnum, mfgname=mfgname, modelname=modelname, alarmlight=alarmlight, start=start, size=size, orderby=orderby, desc=desc, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NorthEntityResServiceApi->get_slot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nedn** | **str**| 设备DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448。 | [optional] 
 **nename** | **str**| 设备名称，样例：FW_B。 | [optional] 
 **framedn** | **str**| 机框DN，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1。 | [optional] 
 **framename** | **str**| 机框名称，样例：Eudemon1000E-N6。 | [optional] 
 **frameno** | **int**| 机框序号，样例：1。 | [optional] 
 **slotdn** | **str**| 单板Dn，样例：047f72d1-7ad3-11e9-b906-000c29b01448,FR&#x3D;1,S&#x3D;1。 | [optional] 
 **slotindex** | **int**| 单板索引，样例：67371017。 | [optional] 
 **slotno** | **int**| 单板序号，样例：1。 | [optional] 
 **vendortype** | **str**| 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.12.16719978。 | [optional] 
 **descr** | **str**| 单板描述，样例：--。 | [optional] 
 **slotname** | **str**| 单板名称，样例：2XG8GE。 | [optional] 
 **physicalclass** | **int**| 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  | [optional] 
 **adminstatus** | **int**| 管理状态： 4、11：正常 2、3、12：错误 13：LoopBack  | [optional] 
 **operstatus** | **int**| 操作状态： 3、11、13、15、16：正 2、12、17：错误 4：离线 其他：未知  | [optional] 
 **standbystatus** | **int**| 主备状态： 1：notSupported 2： hotStandby 3：coldStandby 4：providingService  | [optional] 
 **hardversion** | **str**| 硬件版本，样例：VER.A。 | [optional] 
 **firmversion** | **str**| 固件版本，样例：221 Nov 28 2017 17:23:17 。 | [optional] 
 **softversion** | **str**| 软件版本，样例：V500R001C80SPC100。 | [optional] 
 **serialnum** | **str**| 序列号，样例：210235G7FW0123456789。 | [optional] 
 **mfgname** | **str**| 组件名称，样例：Huawei。 | [optional] 
 **modelname** | **str**| 模块名称，样例：huawei。 | [optional] 
 **alarmlight** | **str**| 预留字段，当前无意义。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明： 如果值小于0，将使用缺省值。 | [optional] 
 **size** | **int**| 指定返回查询结果集总数。缺省值是20。说明： 1、如果值小于0，将使用缺省值。2、数据的size，最大建议10000条。 | [optional] 
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、framename、slotdn说明：指定多个排序字段时字段间用英文半角逗号“,”分隔。 | [optional] 
 **desc** | **bool**| 指定查询结果是否按降序排序。缺省值是false。说明： 此请求参数只有指定了“orderby”请求参数后才有效。 | [optional] 
 **fields** | **str**| 指定查询结果所包含的列。需要查询的列名为fields参数的值，多个列名时可用英文逗号隔开。说明：此请求参数只有指定了“fields”请求参数后才有效，不指定默认返回所有字段。 | [optional] 

### Return type

[**SlotResResponse**](SlotResResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_slot_list**
> SubSlotResResponse get_sub_slot_list(nedn=nedn, nename=nename, framedn=framedn, slotdn=slotdn, slotname=slotname, subslotdn=subslotdn, frameno=frameno, slotno=slotno, subslotindex=subslotindex, subslotno=subslotno, descr=descr, subslotname=subslotname, vendortype=vendortype, physicalclass=physicalclass, hardversion=hardversion, firmversion=firmversion, softversion=softversion, adminstatus=adminstatus, operstatus=operstatus, modelname=modelname, serialnum=serialnum, mfgname=mfgname, start=start, size=size, orderby=orderby, desc=desc)

条件查询子卡资源

## 典型场景 ##  北向接口支持条件查询子卡资源。 ## 接口功能 ##  条件查询子卡资源。 ## 接口约束 ##  该接口属于北向接口，由北向调用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NorthEntityResServiceApi()
nedn = 'a4059c31-7ad3-11e9-b906-000c29b01448' # str | 设备Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448。 (optional)
nename = 'AR1220-56' # str | 设备名称，样例：AR1220-56。 (optional)
framedn = 'a4059c31-7ad3-11e9-b906-000c29b01448,FR=0' # str | 机框Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR=0。 (optional)
slotdn = 'a4059c31-7ad3-11e9-b906-000c29b01448,FR=0,S=0' # str | 单板Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR=0,S=0。 (optional)
slotname = 'SRU Board 0' # str | 单板名称，样例：SRU Board 0。 (optional)
subslotdn = 'a4059c31-7ad3-11e9-b906-000c29b01448,FR=0,S=0,SS=0' # str | 子卡Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR=0,S=0,SS=0。 (optional)
frameno = 0 # int | 机框序号，样例：0。 (optional)
slotno = 0 # int | 单板序号，样例：0。 (optional)
subslotindex = 16397 # int | 子卡索引，样例：16397。 (optional)
subslotno = 0 # int | 子卡序号，样例：0。 (optional)
descr = 'FAN Card' # str | 子卡描述，样例：FAN Card。 (optional)
subslotname = 'FAN Card 0/1' # str | 子卡名称，样例：FAN Card 0/1。 (optional)
vendortype = '.1.3.6.1.4.1.2011.20021210.13.0' # str | 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.13.0。 (optional)
physicalclass = 9 # int | 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  (optional)
hardversion = 'VER.0' # str | 硬件版本，样例：VER.0。 (optional)
firmversion = 'Hex:31 30 39' # str | 固件版本，样例：Hex： 31 30 39 。 (optional)
softversion = '0' # str | 软件版本，样例：0。 (optional)
adminstatus = 4 # int | 管理状态： 4、11：正常 2、3、12：错误 13：LoopBack  (optional)
operstatus = 3 # int | 操作状态： 3、11、13、15、16：正常 2、12、17：错误 4：离线 其他：未知  (optional)
modelname = '--' # str | 模块名称，样例：--。 (optional)
serialnum = '030KSB10B3000060' # str | 序列号，样例：030KSB10B3000060。 (optional)
mfgname = 'Huawei' # str | 组件名称，物理固件的制造厂商，样例：Huawei。 (optional)
start = 0 # int | 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 (optional)
size = 20 # int | 指定返回查询结果集总数。缺省值是20。说明：如果值小于0，将使用缺省值。 (optional)
orderby = 'nedn' # str | 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、slotdn、slotname。说明：指定多个排序字段时字段间用英文半角逗号“,”分隔。 (optional)
desc = true # bool | 指定查询结果是否按降序排序。缺省值是false。说明：此请求参数只有指定了“orderby”请求参数后才有效。 (optional)

try: 
    # 条件查询子卡资源
    api_response = api_instance.get_sub_slot_list(nedn=nedn, nename=nename, framedn=framedn, slotdn=slotdn, slotname=slotname, subslotdn=subslotdn, frameno=frameno, slotno=slotno, subslotindex=subslotindex, subslotno=subslotno, descr=descr, subslotname=subslotname, vendortype=vendortype, physicalclass=physicalclass, hardversion=hardversion, firmversion=firmversion, softversion=softversion, adminstatus=adminstatus, operstatus=operstatus, modelname=modelname, serialnum=serialnum, mfgname=mfgname, start=start, size=size, orderby=orderby, desc=desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NorthEntityResServiceApi->get_sub_slot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nedn** | **str**| 设备Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448。 | [optional] 
 **nename** | **str**| 设备名称，样例：AR1220-56。 | [optional] 
 **framedn** | **str**| 机框Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR&#x3D;0。 | [optional] 
 **slotdn** | **str**| 单板Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR&#x3D;0,S&#x3D;0。 | [optional] 
 **slotname** | **str**| 单板名称，样例：SRU Board 0。 | [optional] 
 **subslotdn** | **str**| 子卡Dn，样例：a4059c31-7ad3-11e9-b906-000c29b01448,FR&#x3D;0,S&#x3D;0,SS&#x3D;0。 | [optional] 
 **frameno** | **int**| 机框序号，样例：0。 | [optional] 
 **slotno** | **int**| 单板序号，样例：0。 | [optional] 
 **subslotindex** | **int**| 子卡索引，样例：16397。 | [optional] 
 **subslotno** | **int**| 子卡序号，样例：0。 | [optional] 
 **descr** | **str**| 子卡描述，样例：FAN Card。 | [optional] 
 **subslotname** | **str**| 子卡名称，样例：FAN Card 0/1。 | [optional] 
 **vendortype** | **str**| 厂商类型，样例：.1.3.6.1.4.1.2011.20021210.13.0。 | [optional] 
 **physicalclass** | **int**| 设备上实体大类型： 3：框 4：背板 5：子槽 6：电源 7：风扇 9：板 10：端口  | [optional] 
 **hardversion** | **str**| 硬件版本，样例：VER.0。 | [optional] 
 **firmversion** | **str**| 固件版本，样例：Hex： 31 30 39 。 | [optional] 
 **softversion** | **str**| 软件版本，样例：0。 | [optional] 
 **adminstatus** | **int**| 管理状态： 4、11：正常 2、3、12：错误 13：LoopBack  | [optional] 
 **operstatus** | **int**| 操作状态： 3、11、13、15、16：正常 2、12、17：错误 4：离线 其他：未知  | [optional] 
 **modelname** | **str**| 模块名称，样例：--。 | [optional] 
 **serialnum** | **str**| 序列号，样例：030KSB10B3000060。 | [optional] 
 **mfgname** | **str**| 组件名称，物理固件的制造厂商，样例：Huawei。 | [optional] 
 **start** | **int**| 指定从哪个起始记录位置开始返回查询结果集。缺省值是0。说明：如果值小于0，将使用缺省值。 | [optional] 
 **size** | **int**| 指定返回查询结果集总数。缺省值是20。说明：如果值小于0，将使用缺省值。 | [optional] 
 **orderby** | **str**| 指定查询结果集采用的排序字段。缺省排序字段是nedn。可指定的排序字段包括：nedn、nename、framedn、slotdn、slotname。说明：指定多个排序字段时字段间用英文半角逗号“,”分隔。 | [optional] 
 **desc** | **bool**| 指定查询结果是否按降序排序。缺省值是false。说明：此请求参数只有指定了“orderby”请求参数后才有效。 | [optional] 

### Return type

[**SubSlotResResponse**](SubSlotResResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

