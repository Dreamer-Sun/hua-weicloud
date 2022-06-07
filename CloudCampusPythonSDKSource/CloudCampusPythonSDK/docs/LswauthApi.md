# swagger_client.LswauthApi

All URIs are relative to *https://localhost/controller/campus/v1/authconfigservice/accessconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lsw_auth**](LswauthApi.md#create_lsw_auth) | **POST** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles | 创建站点下交换机有线认证模板配置
[**delete_lsw_auth**](LswauthApi.md#delete_lsw_auth) | **POST** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/batch-delete | 删除站点下交换机有线认证模板配置
[**get_lsw_auth**](LswauthApi.md#get_lsw_auth) | **GET** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles | 查询站点下交换机有线认证模板配置
[**update_lsw_auth**](LswauthApi.md#update_lsw_auth) | **PUT** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/{profileId} | 修改站点下交换机有线认证模板配置
[**update_lsw_auth_inc**](LswauthApi.md#update_lsw_auth_inc) | **POST** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/{profileId}/devices | 增量绑定交换机无线认证模板配置
[**update_lsw_auth_pro_inc**](LswauthApi.md#update_lsw_auth_pro_inc) | **PUT** /controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profileInfos/{profileId} | 修改站点交换机有线认证部分模板配置


# **create_lsw_auth**
> LswAuthConfigResponse create_lsw_auth(lsw_auth_config_core, site_id)

创建站点下交换机有线认证模板配置

## 典型场景 ##  创建站点下交换机有线认证模板配置。<br> ## 接口功能 ##  创建站点下交换机有线认证模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
lsw_auth_config_core = cloudcampus.LswAuthConfigCore() # LswAuthConfigCore | 交换机认证模板配置信息。
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。

try: 
    # 创建站点下交换机有线认证模板配置
    api_response = api_instance.create_lsw_auth(lsw_auth_config_core, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->create_lsw_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lsw_auth_config_core** | [**LswAuthConfigCore**](LswAuthConfigCore.md)| 交换机认证模板配置信息。 | 
 **site_id** | **str**| 站点标识，UUID格式。 | 

### Return type

[**LswAuthConfigResponse**](LswAuthConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lsw_auth**
> DeleteAuthResponse delete_lsw_auth(site_id, ids)

删除站点下交换机有线认证模板配置

## 典型场景 ##  批量删除站点下交换机有线认证模板。<br> ## 接口功能 ##  批量删除站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
ids = cloudcampus.LswAuthDeleteDto() # LswAuthDeleteDto | 待删除的有线认证模板。

try: 
    # 删除站点下交换机有线认证模板配置
    api_response = api_instance.delete_lsw_auth(site_id, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->delete_lsw_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **ids** | [**LswAuthDeleteDto**](LswAuthDeleteDto.md)| 待删除的有线认证模板。 | 

### Return type

[**DeleteAuthResponse**](DeleteAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lsw_auth**
> LswAuthConfigResponse get_lsw_auth(site_id, profile_name=profile_name, policy_id=policy_id)

查询站点下交换机有线认证模板配置

## 典型场景 ##  查询指定站点内交换机有线认证模板列表。<br> ## 接口功能 ##  查询站点下交换机有线认证模板列表。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
profile_name = 'policy' # str | 认证模板名称，支持模糊查询。 (optional)
policy_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 认证模板ID，UUID格式。 (optional)

try: 
    # 查询站点下交换机有线认证模板配置
    api_response = api_instance.get_lsw_auth(site_id, profile_name=profile_name, policy_id=policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->get_lsw_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **profile_name** | **str**| 认证模板名称，支持模糊查询。 | [optional] 
 **policy_id** | **str**| 认证模板ID，UUID格式。 | [optional] 

### Return type

[**LswAuthConfigResponse**](LswAuthConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lsw_auth**
> LswAuthConfigResponse update_lsw_auth(site_id, profile_id, lsw_auth_config)

修改站点下交换机有线认证模板配置

## 典型场景 ##  修改站点下交换机有线认证模板。<br> ## 接口功能 ##  修改站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
profile_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 认证模板ID，UUID格式。
lsw_auth_config = cloudcampus.LswAuthConfig() # LswAuthConfig | 有线认证配置。

try: 
    # 修改站点下交换机有线认证模板配置
    api_response = api_instance.update_lsw_auth(site_id, profile_id, lsw_auth_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->update_lsw_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **profile_id** | **str**| 认证模板ID，UUID格式。 | 
 **lsw_auth_config** | [**LswAuthConfig**](LswAuthConfig.md)| 有线认证配置。 | 

### Return type

[**LswAuthConfigResponse**](LswAuthConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lsw_auth_inc**
> LswAuthConfigResponse update_lsw_auth_inc(site_id, profile_id, lsw_device_info)

增量绑定交换机无线认证模板配置

## 典型场景 ##  交换机无线认证配置增量绑定设备。<br> ## 接口功能 ##  交换机无线认证配置增量绑定设备。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
profile_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 认证模板ID，UUID格式。
lsw_device_info = cloudcampus.LswDeviceInfo() # LswDeviceInfo | 设备接口列表。

try: 
    # 增量绑定交换机无线认证模板配置
    api_response = api_instance.update_lsw_auth_inc(site_id, profile_id, lsw_device_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->update_lsw_auth_inc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **profile_id** | **str**| 认证模板ID，UUID格式。 | 
 **lsw_device_info** | [**LswDeviceInfo**](LswDeviceInfo.md)| 设备接口列表。 | 

### Return type

[**LswAuthConfigResponse**](LswAuthConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lsw_auth_pro_inc**
> LswAuthConfigResponse update_lsw_auth_pro_inc(site_id, profile_id, lsw_auth_config_profile)

修改站点交换机有线认证部分模板配置

## 典型场景 ##  修改站点交换机有线认证部分模板配置。<br> ## 接口功能 ##  修改站点交换机有线认证部分模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.LswauthApi()
site_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 站点标识，UUID格式。
profile_id = 'fbde1c5d-5b94-49e3-a912-48641015e45c' # str | 认证模板ID，UUID格式。
lsw_auth_config_profile = cloudcampus.LswAuthConfigProfile() # LswAuthConfigProfile | 有线认证配置。

try: 
    # 修改站点交换机有线认证部分模板配置
    api_response = api_instance.update_lsw_auth_pro_inc(site_id, profile_id, lsw_auth_config_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LswauthApi->update_lsw_auth_pro_inc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **profile_id** | **str**| 认证模板ID，UUID格式。 | 
 **lsw_auth_config_profile** | [**LswAuthConfigProfile**](LswAuthConfigProfile.md)| 有线认证配置。 | 

### Return type

[**LswAuthConfigResponse**](LswAuthConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

