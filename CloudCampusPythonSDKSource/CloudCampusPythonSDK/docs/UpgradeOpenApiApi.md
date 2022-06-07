# swagger_client.UpgradeOpenApiApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice/upgrade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_policy**](UpgradeOpenApiApi.md#cancel_policy) | **POST** /controller/campus/v1/oamservice/upgrade/policy/device/cancel | 取消设备升级
[**cancel_site_policy**](UpgradeOpenApiApi.md#cancel_site_policy) | **POST** /controller/campus/v1/oamservice/upgrade/policy/site/cancel | 删除站点升级
[**policy_configuration**](UpgradeOpenApiApi.md#policy_configuration) | **POST** /controller/campus/v1/oamservice/upgrade/policy | 创建站点升级
[**query_policy**](UpgradeOpenApiApi.md#query_policy) | **GET** /controller/campus/v1/oamservice/upgrade/policy/{siteId} | 查询站点升级
[**query_policy_detail**](UpgradeOpenApiApi.md#query_policy_detail) | **GET** /controller/campus/v1/oamservice/upgrade/policy-detail/{siteId} | 查询设备升级
[**query_version**](UpgradeOpenApiApi.md#query_version) | **GET** /controller/campus/v1/oamservice/upgrade/version | 查询设备文件
[**re_upgrade**](UpgradeOpenApiApi.md#re_upgrade) | **POST** /controller/campus/v1/oamservice/upgrade/reupgrade | 重新升级设备


# **cancel_policy**
> CommonResponseBody cancel_policy(policy_device_cancel_input_list)

取消设备升级

## 典型场景 ##    取消设备升级。 ## 接口功能 ##    取消设备升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
policy_device_cancel_input_list = cloudcampus.PolicyDeviceCancelInputList() # PolicyDeviceCancelInputList | 取消设备升级入参。

try: 
    # 取消设备升级
    api_response = api_instance.cancel_policy(policy_device_cancel_input_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->cancel_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_device_cancel_input_list** | [**PolicyDeviceCancelInputList**](PolicyDeviceCancelInputList.md)| 取消设备升级入参。 | 

### Return type

[**CommonResponseBody**](CommonResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_site_policy**
> CommonResponseBody cancel_site_policy(policy_site_cancel_input_list)

删除站点升级

## 典型场景 ##    删除多站点升级计划。 ## 接口功能 ##    删除多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。    建议先取消所有站点下正在升级的设备。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
policy_site_cancel_input_list = cloudcampus.PolicySiteCancelInputList() # PolicySiteCancelInputList | 删除多站点升级计划入参。

try: 
    # 删除站点升级
    api_response = api_instance.cancel_site_policy(policy_site_cancel_input_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->cancel_site_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_site_cancel_input_list** | [**PolicySiteCancelInputList**](PolicySiteCancelInputList.md)| 删除多站点升级计划入参。 | 

### Return type

[**CommonResponseBody**](CommonResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_configuration**
> PolicyConfigRes policy_configuration(policy_config)

创建站点升级

## 典型场景 ##    创建多站点升级计划。 ## 接口功能 ##    创建多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
policy_config = cloudcampus.PolicyConfig() # PolicyConfig | 多站点升级计划。

try: 
    # 创建站点升级
    api_response = api_instance.policy_configuration(policy_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->policy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_config** | [**PolicyConfig**](PolicyConfig.md)| 多站点升级计划。 | 

### Return type

[**PolicyConfigRes**](PolicyConfigRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_policy**
> PolicyConfigRes query_policy(site_id, device_model=device_model)

查询站点升级

## 典型场景 ##    查询站点升级计划概要。 ## 接口功能 ##    查询站点升级计划概要。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
device_model = 'AR161FW' # str | 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级计划。  (optional)

try: 
    # 查询站点升级
    api_response = api_instance.query_policy(site_id, device_model=device_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->query_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **device_model** | **str**| 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级计划。  | [optional] 

### Return type

[**PolicyConfigRes**](PolicyConfigRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_policy_detail**
> DeviceDetailListRes query_policy_detail(site_id, device_model=device_model)

查询设备升级

## 典型场景 ##    查询站点下具体设备的升级状态。 ## 接口功能 ##    查询站点下具体设备的升级状态。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359ca' # str | 站点ID。
device_model = 'AR161FW' # str | 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级状态。  (optional)

try: 
    # 查询设备升级
    api_response = api_instance.query_policy_detail(site_id, device_model=device_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->query_policy_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID。 | 
 **device_model** | **str**| 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级状态。  | [optional] 

### Return type

[**DeviceDetailListRes**](DeviceDetailListRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_version**
> AvailableVersion query_version(device_model)

查询设备文件

## 典型场景 ##    根据设备款型查询可用文件列表。 ## 接口功能 ##    根据设备款型查询可用文件列表。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
device_model = 'AP6050DN' # str | 设备款型。

try: 
    # 查询设备文件
    api_response = api_instance.query_version(device_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->query_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model** | **str**| 设备款型。 | 

### Return type

[**AvailableVersion**](AvailableVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_upgrade**
> CommonResponseBody re_upgrade(reupgrade_request_body)

重新升级设备

## 典型场景 ##    升级失败的设备重新升级。 ## 接口功能 ##    升级失败的设备重新升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UpgradeOpenApiApi()
reupgrade_request_body = cloudcampus.ReupgradeRequestBody() # ReupgradeRequestBody | 重新升级入参。

try: 
    # 重新升级设备
    api_response = api_instance.re_upgrade(reupgrade_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeOpenApiApi->re_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reupgrade_request_body** | [**ReupgradeRequestBody**](ReupgradeRequestBody.md)| 重新升级入参。 | 

### Return type

[**CommonResponseBody**](CommonResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

