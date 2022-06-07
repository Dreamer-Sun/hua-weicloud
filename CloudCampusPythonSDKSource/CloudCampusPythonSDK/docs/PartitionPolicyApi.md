# swagger_client.PartitionPolicyApi

All URIs are relative to *https://localhost/secm/public/services/fwaas/v1/threatdefense*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_threat_defense**](PartitionPolicyApi.md#delete_threat_defense) | **DELETE** /secm/public/services/fwaas/v1/threatdefense/{blockId} | 撤销CIS阻断/隔离
[**interdiction**](PartitionPolicyApi.md#interdiction) | **POST** /secm/public/services/fwaas/v1/threatdefense/interdiction | 创建CIS阻断策略
[**isolate_vm**](PartitionPolicyApi.md#isolate_vm) | **POST** /secm/public/services/fwaas/v1/threatdefense/isolation | 创建CIS隔离策略
[**query_hits**](PartitionPolicyApi.md#query_hits) | **POST** /secm/public/services/fwaas/v1/threatdefense/policyhits | CIS策略命中率查询
[**query_status**](PartitionPolicyApi.md#query_status) | **GET** /secm/public/services/fwaas/v1/threatdefense/status/{blockId} | 查询阻断/隔离应用状态


# **delete_threat_defense**
> CisResponseDto delete_threat_defense(block_id)

撤销CIS阻断/隔离

## 操作场景 ##   威胁解除，撤销阻断/隔离。 ## 接口功能 ##   撤销CIS阻断/隔离。 ## 接口约束 ##   拥有北向管理员角色的用户才有权限使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PartitionPolicyApi()
block_id = '85de427a-cf26-4fa8-8678-ee7dd192d012' # str | CIS阻断/隔离ID，UUID格式。

try: 
    # 撤销CIS阻断/隔离
    api_response = api_instance.delete_threat_defense(block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionPolicyApi->delete_threat_defense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| CIS阻断/隔离ID，UUID格式。 | 

### Return type

[**CisResponseDto**](CisResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interdiction**
> CisResponseDto interdiction(interdiction_dto)

创建CIS阻断策略

## 操作场景 ##   向防火墙/交换机下发阻断策略，阻断攻击源。 ## 接口功能 ##   创建CIS阻断策略。 ## 接口约束 ##   拥有北向管理员角色的用户才有权限使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PartitionPolicyApi()
interdiction_dto = cloudcampus.InterdictionDTO() # InterdictionDTO | 创建CIS阻断输入。

try: 
    # 创建CIS阻断策略
    api_response = api_instance.interdiction(interdiction_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionPolicyApi->interdiction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interdiction_dto** | [**InterdictionDTO**](InterdictionDTO.md)| 创建CIS阻断输入。 | 

### Return type

[**CisResponseDto**](CisResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isolate_vm**
> CisResponseDto isolate_vm(isolation_dto)

创建CIS隔离策略

## 操作场景 ##   向防火墙/交换机下发创建隔离策略，隔离攻击源。 ## 接口功能 ##   创建CIS隔离策略。 ## 接口约束 ##   拥有北向管理员角色的用户才有权限使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PartitionPolicyApi()
isolation_dto = cloudcampus.IsolationDTO() # IsolationDTO | 创建CIS隔离输入。

try: 
    # 创建CIS隔离策略
    api_response = api_instance.isolate_vm(isolation_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionPolicyApi->isolate_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isolation_dto** | [**IsolationDTO**](IsolationDTO.md)| 创建CIS隔离输入。 | 

### Return type

[**CisResponseDto**](CisResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_hits**
> QueryHitsResponseDTO query_hits(policy_hits_dto)

CIS策略命中率查询

## 操作场景 ##   查询设定时间内CIS策略的命中率。 ## 接口功能 ##   CIS策略命中率查询。 ## 接口约束 ##   拥有北向管理员角色的用户才有权限使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PartitionPolicyApi()
policy_hits_dto = cloudcampus.PolicyHitsDTO() # PolicyHitsDTO | CIS策略命中率查询输入。

try: 
    # CIS策略命中率查询
    api_response = api_instance.query_hits(policy_hits_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionPolicyApi->query_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_hits_dto** | [**PolicyHitsDTO**](PolicyHitsDTO.md)| CIS策略命中率查询输入。 | 

### Return type

[**QueryHitsResponseDTO**](QueryHitsResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_status**
> QueryStatusResponseDTO query_status(block_id)

查询阻断/隔离应用状态

## 操作场景 ##   查询阻断隔离策略的下发状态。 ## 接口功能 ##   阻断隔离应用状态查询。 ## 接口约束 ##   拥有北向管理员角色的用户才有权限使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.PartitionPolicyApi()
block_id = '85de427a-cf26-4fa8-8678-ee7dd192d012' # str | CIS阻断/隔离ID，UUID格式。

try: 
    # 查询阻断/隔离应用状态
    api_response = api_instance.query_status(block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionPolicyApi->query_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| CIS阻断/隔离ID，UUID格式。 | 

### Return type

[**QueryStatusResponseDTO**](QueryStatusResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

