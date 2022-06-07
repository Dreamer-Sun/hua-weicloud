# swagger_client.NatSessionLogServiceApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configap_nat_session_log**](NatSessionLogServiceApi.md#configap_nat_session_log) | **PUT** /controller/campus/v1/oamservice/site/{siteId}/apnatsessionlog | 配置站点内AP设备Nat日志上报信息
[**get_ap_nat_session_log_config**](NatSessionLogServiceApi.md#get_ap_nat_session_log_config) | **GET** /controller/campus/v1/oamservice/site/{siteId}/apnatsessionlog | 查询站点内AP设备Nat日志上报配置


# **configap_nat_session_log**
> NatSessionLogConfigResult configap_nat_session_log(site_id, config_param)

配置站点内AP设备Nat日志上报信息

## 典型场景 ##  配置站点内AP设备Nat日志上报信息。 ## 接口功能 ##  配置站点内AP设备Nat日志上报信息。 ## 接口约束 ##  该接口支持北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NatSessionLogServiceApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点标识，UUID格式。
config_param = cloudcampus.NatSessionLogConfigParam() # NatSessionLogConfigParam | 配置参数。

try: 
    # 配置站点内AP设备Nat日志上报信息
    api_response = api_instance.configap_nat_session_log(site_id, config_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NatSessionLogServiceApi->configap_nat_session_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **config_param** | [**NatSessionLogConfigParam**](NatSessionLogConfigParam.md)| 配置参数。 | 

### Return type

[**NatSessionLogConfigResult**](NatSessionLogConfigResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ap_nat_session_log_config**
> NatSessionLogConfigResult get_ap_nat_session_log_config(site_id)

查询站点内AP设备Nat日志上报配置

## 典型场景 ##  查询站点内AP设备的Nat日志上报的配置。 ## 接口功能 ##  查询站点内AP设备的Nat日志上报的配置。 ## 接口约束 ##  该接口支持北向接口管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.NatSessionLogServiceApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点标识，UUID格式。

try: 
    # 查询站点内AP设备Nat日志上报配置
    api_response = api_instance.get_ap_nat_session_log_config(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NatSessionLogServiceApi->get_ap_nat_session_log_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 

### Return type

[**NatSessionLogConfigResult**](NatSessionLogConfigResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

