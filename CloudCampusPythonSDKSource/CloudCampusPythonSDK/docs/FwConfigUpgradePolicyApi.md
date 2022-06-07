# swagger_client.FwConfigUpgradePolicyApi

All URIs are relative to *https://localhost/controller/campus/v1/oamservice/saupgrade*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_upgrade_policy**](FwConfigUpgradePolicyApi.md#config_upgrade_policy) | **POST** /controller/campus/v1/oamservice/saupgrade/sites | 配置防火墙站点特征库升级策略
[**get_upgrade_policy**](FwConfigUpgradePolicyApi.md#get_upgrade_policy) | **GET** /controller/campus/v1/oamservice/saupgrade/sites/{siteId} | 查询防火墙站点特征库升级策略


# **config_upgrade_policy**
> ConfigPolicyResponse config_upgrade_policy(config_upgrade_policy_list_dto)

配置防火墙站点特征库升级策略

## 典型场景 ##   提供配置防火墙站点特征库升级策略接口。 ## 接口功能 ##   配置防火墙站点特征库升级策略。 ## 接口约束 ##   该接口必须在存在防火墙的站点下使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwConfigUpgradePolicyApi()
config_upgrade_policy_list_dto = cloudcampus.ConfigUpgradePolicyListDto() # ConfigUpgradePolicyListDto | 防火墙站点特征库升级策略配置信息。

try: 
    # 配置防火墙站点特征库升级策略
    api_response = api_instance.config_upgrade_policy(config_upgrade_policy_list_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwConfigUpgradePolicyApi->config_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_upgrade_policy_list_dto** | [**ConfigUpgradePolicyListDto**](ConfigUpgradePolicyListDto.md)| 防火墙站点特征库升级策略配置信息。 | 

### Return type

[**ConfigPolicyResponse**](ConfigPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_policy**
> GetPolicyResponse get_upgrade_policy(site_id)

查询防火墙站点特征库升级策略

## 典型场景 ##   提供查询防火墙站点特征库升级策略接口。 ## 接口功能 ##   查询防火墙站点特征库升级策略。 ## 接口约束 ##   该接口必须在存在防火墙的站点下使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.FwConfigUpgradePolicyApi()
site_id = 'ea25fdbf-8dee-4823-bac2-5bfe8e3359cad' # str | 站点标识，UUID格式。

try: 
    # 查询防火墙站点特征库升级策略
    api_response = api_instance.get_upgrade_policy(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FwConfigUpgradePolicyApi->get_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 

### Return type

[**GetPolicyResponse**](GetPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

